"""Cache Manager for handling application-level caching."""

import time
from abc import ABC, abstractmethod
from functools import wraps
from typing import Any, Callable

from aiml_studio.utilities.logger import get_logger


class CacheManager(ABC):
    """Abstract base class for managing application cache.

    This class provides a framework for:
    - Caching expensive computations
    - Managing cache entries with TTL (time-to-live)
    - Implementing cache eviction policies (LRU)
    - Providing cache statistics
    """

    def __init__(self) -> None:
        """Initialize the CacheManager."""
        self._logger = get_logger(__name__)
        self._cache: dict[str, Any] = {}
        self._stats = {"hits": 0, "misses": 0, "sets": 0, "evictions": 0}

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the cache manager."""
        pass

    @abstractmethod
    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from cache.

        Args:
            key: Cache key
            default: Default value if key doesn't exist or is expired

        Returns:
            Cached value or default
        """
        pass

    @abstractmethod
    def set(self, key: str, value: Any, ttl: int | None = None) -> bool:
        """Set a value in cache.

        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (None for no expiration)

        Returns:
            True if successful
        """
        pass

    @abstractmethod
    def delete(self, key: str) -> bool:
        """Delete a value from cache.

        Args:
            key: Cache key

        Returns:
            True if successful
        """
        pass

    @abstractmethod
    def clear(self) -> bool:
        """Clear all cache entries.

        Returns:
            True if successful
        """
        pass

    @abstractmethod
    def has_key(self, key: str) -> bool:
        """Check if a key exists in cache and is not expired.

        Args:
            key: Cache key

        Returns:
            True if key exists and is valid
        """
        pass

    def get_stats(self) -> dict[str, int]:
        """Get cache statistics.

        Returns:
            Dictionary of cache statistics
        """
        return dict(self._stats)

    def reset_stats(self) -> None:
        """Reset cache statistics."""
        self._stats = {"hits": 0, "misses": 0, "sets": 0, "evictions": 0}


class LRUCacheManager(CacheManager):
    """LRU (Least Recently Used) cache manager implementation."""

    def __init__(self, max_size: int = 100, default_ttl: int | None = 3600) -> None:
        """Initialize the LRU cache manager.

        Args:
            max_size: Maximum number of cache entries
            default_ttl: Default TTL in seconds (None for no expiration)
        """
        super().__init__()
        self._max_size = max_size
        self._default_ttl = default_ttl
        self._cache: dict[str, dict[str, Any]] = {}
        self._access_times: dict[str, float] = {}

    def initialize(self) -> None:
        """Initialize the LRU cache manager."""
        self._logger.info(f"LRUCacheManager initialized (max_size={self._max_size}, default_ttl={self._default_ttl})")

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from cache.

        Args:
            key: Cache key
            default: Default value if key doesn't exist or is expired

        Returns:
            Cached value or default
        """
        if key not in self._cache:
            self._stats["misses"] += 1
            return default

        entry = self._cache[key]
        current_time = time.time()

        # Check if entry is expired
        if entry["expires_at"] is not None and current_time > entry["expires_at"]:
            self.delete(key)
            self._stats["misses"] += 1
            return default

        # Update access time for LRU
        self._access_times[key] = current_time
        self._stats["hits"] += 1
        return entry["value"]

    def set(self, key: str, value: Any, ttl: int | None = None) -> bool:
        """Set a value in cache.

        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (None uses default_ttl)

        Returns:
            True if successful
        """
        try:
            # Evict least recently used entry if cache is full
            if len(self._cache) >= self._max_size and key not in self._cache:
                self._evict_lru()

            current_time = time.time()
            ttl = ttl if ttl is not None else self._default_ttl
            expires_at = current_time + ttl if ttl is not None else None

            self._cache[key] = {"value": value, "expires_at": expires_at, "created_at": current_time}
            self._access_times[key] = current_time
            self._stats["sets"] += 1

            self._logger.debug(f"Cached {key} with TTL={ttl}")
            return True
        except Exception:
            self._logger.exception(f"Error setting cache key {key}")
            return False

    def delete(self, key: str) -> bool:
        """Delete a value from cache.

        Args:
            key: Cache key

        Returns:
            True if successful
        """
        if key in self._cache:
            del self._cache[key]
            if key in self._access_times:
                del self._access_times[key]
            self._logger.debug(f"Deleted cache key {key}")
            return True
        return False

    def clear(self) -> bool:
        """Clear all cache entries.

        Returns:
            True if successful
        """
        self._cache.clear()
        self._access_times.clear()
        self._logger.info("Cache cleared")
        return True

    def has_key(self, key: str) -> bool:
        """Check if a key exists in cache and is not expired.

        Args:
            key: Cache key

        Returns:
            True if key exists and is valid
        """
        if key not in self._cache:
            return False

        entry = self._cache[key]
        current_time = time.time()

        # Check if entry is expired
        if entry["expires_at"] is not None and current_time > entry["expires_at"]:
            self.delete(key)
            return False

        return True

    def _evict_lru(self) -> None:
        """Evict the least recently used entry from cache."""
        if not self._access_times:
            return

        # Find the key with the oldest access time
        lru_key = min(self._access_times.items(), key=lambda x: x[1])[0]
        self.delete(lru_key)
        self._stats["evictions"] += 1
        self._logger.debug(f"Evicted LRU key {lru_key}")

    def get_size(self) -> int:
        """Get current cache size.

        Returns:
            Number of entries in cache
        """
        return len(self._cache)


def cached(cache_manager: CacheManager, ttl: int | None = None, key_prefix: str = "") -> Callable:
    """Decorator for caching function results.

    Args:
        cache_manager: Cache manager instance
        ttl: Time-to-live in seconds (None for default)
        key_prefix: Prefix for cache keys

    Returns:
        Decorated function
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Generate cache key from function name and arguments
            key_parts = [key_prefix, func.__name__]
            if args:
                key_parts.append(str(args))
            if kwargs:
                key_parts.append(str(sorted(kwargs.items())))
            cache_key = ":".join(filter(None, key_parts))

            # Try to get from cache
            result = cache_manager.get(cache_key)
            if result is not None:
                return result

            # Call function and cache result
            result = func(*args, **kwargs)
            cache_manager.set(cache_key, result, ttl=ttl)
            return result

        return wrapper

    return decorator

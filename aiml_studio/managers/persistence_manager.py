"""Persistence Manager for handling browser-based storage and state persistence."""

import json
from abc import ABC, abstractmethod
from typing import Any

from aiml_studio.utilities.logger import get_logger


class PersistenceManager(ABC):
    """Abstract base class for managing persistence of application state.

    This class provides a framework for:
    - Storing data in browser localStorage
    - Storing data in browser sessionStorage
    - Managing persistence of user preferences
    - Handling serialization and deserialization
    """

    def __init__(self) -> None:
        """Initialize the PersistenceManager."""
        self._logger = get_logger(__name__)
        self._storage: dict[str, Any] = {}

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the persistence manager."""
        pass

    @abstractmethod
    def save(self, key: str, value: Any, storage_type: str = "local") -> bool:
        """Save a value to storage.

        Args:
            key: Storage key
            value: Value to store
            storage_type: Type of storage ('local' or 'session')

        Returns:
            True if successful, False otherwise
        """
        pass

    @abstractmethod
    def load(self, key: str, storage_type: str = "local", default: Any = None) -> Any:
        """Load a value from storage.

        Args:
            key: Storage key
            storage_type: Type of storage ('local' or 'session')
            default: Default value if key doesn't exist

        Returns:
            Stored value or default
        """
        pass

    @abstractmethod
    def delete(self, key: str, storage_type: str = "local") -> bool:
        """Delete a value from storage.

        Args:
            key: Storage key
            storage_type: Type of storage ('local' or 'session')

        Returns:
            True if successful, False otherwise
        """
        pass

    @abstractmethod
    def clear(self, storage_type: str = "local") -> bool:
        """Clear all values from storage.

        Args:
            storage_type: Type of storage ('local' or 'session')

        Returns:
            True if successful, False otherwise
        """
        pass


class BrowserPersistenceManager(PersistenceManager):
    """Browser-based implementation of PersistenceManager using dcc.Store."""

    def initialize(self) -> None:
        """Initialize the browser persistence manager."""
        self._logger.info("BrowserPersistenceManager initialized")
        self._storage = {
            "local": {},  # localStorage equivalent
            "session": {},  # sessionStorage equivalent
            "memory": {},  # in-memory only
        }

    def save(self, key: str, value: Any, storage_type: str = "local") -> bool:
        """Save a value to storage.

        Args:
            key: Storage key
            value: Value to store
            storage_type: Type of storage ('local', 'session', or 'memory')

        Returns:
            True if successful
        """
        try:
            if storage_type not in self._storage:
                self._logger.warning(f"Invalid storage type: {storage_type}")
                return False

            # Serialize complex objects to JSON
            serialized_value = self._serialize(value)
            self._storage[storage_type][key] = serialized_value
            self._logger.debug(f"Saved {key} to {storage_type} storage")
            return True
        except Exception:
            self._logger.exception(f"Error saving {key} to {storage_type} storage")
            return False

    def load(self, key: str, storage_type: str = "local", default: Any = None) -> Any:
        """Load a value from storage.

        Args:
            key: Storage key
            storage_type: Type of storage ('local', 'session', or 'memory')
            default: Default value if key doesn't exist

        Returns:
            Stored value or default
        """
        try:
            if storage_type not in self._storage:
                self._logger.warning(f"Invalid storage type: {storage_type}")
                return default

            if key not in self._storage[storage_type]:
                return default

            serialized_value = self._storage[storage_type][key]
            return self._deserialize(serialized_value)
        except Exception:
            self._logger.exception(f"Error loading {key} from {storage_type} storage")
            return default

    def delete(self, key: str, storage_type: str = "local") -> bool:
        """Delete a value from storage.

        Args:
            key: Storage key
            storage_type: Type of storage ('local', 'session', or 'memory')

        Returns:
            True if successful
        """
        try:
            if storage_type not in self._storage:
                return False

            if key in self._storage[storage_type]:
                del self._storage[storage_type][key]
                self._logger.debug(f"Deleted {key} from {storage_type} storage")
                return True
            return False
        except Exception:
            self._logger.exception(f"Error deleting {key} from {storage_type} storage")
            return False

    def clear(self, storage_type: str = "local") -> bool:
        """Clear all values from storage.

        Args:
            storage_type: Type of storage ('local', 'session', or 'memory')

        Returns:
            True if successful
        """
        try:
            if storage_type not in self._storage:
                return False

            self._storage[storage_type].clear()
            self._logger.info(f"Cleared {storage_type} storage")
            return True
        except Exception:
            self._logger.exception(f"Error clearing {storage_type} storage")
            return False

    def _serialize(self, value: Any) -> Any:
        """Serialize a value for storage.

        Args:
            value: Value to serialize

        Returns:
            Serialized value
        """
        try:
            # Try to convert to JSON-serializable format
            json.dumps(value)
            return value
        except (TypeError, ValueError):
            # If not serializable, convert to string
            return str(value)

    def _deserialize(self, value: Any) -> Any:
        """Deserialize a value from storage.

        Args:
            value: Value to deserialize

        Returns:
            Deserialized value
        """
        return value

    def get_all(self, storage_type: str = "local") -> dict[str, Any]:
        """Get all values from storage.

        Args:
            storage_type: Type of storage ('local', 'session', or 'memory')

        Returns:
            Dictionary of all stored values
        """
        if storage_type not in self._storage:
            return {}
        return dict(self._storage[storage_type])

    def has_key(self, key: str, storage_type: str = "local") -> bool:
        """Check if a key exists in storage.

        Args:
            key: Storage key
            storage_type: Type of storage ('local', 'session', or 'memory')

        Returns:
            True if key exists
        """
        if storage_type not in self._storage:
            return False
        return key in self._storage[storage_type]

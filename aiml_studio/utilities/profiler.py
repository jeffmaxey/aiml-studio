"""Profiler utility for performance monitoring."""

import time
from collections.abc import Generator
from contextlib import contextmanager
from datetime import datetime

from aiml_studio.utilities.logger import get_logger


class Profiler:
    """Profiler for monitoring performance and timing operations."""

    def __init__(self) -> None:
        """Initialize the profiler."""
        self._logger = get_logger(__name__)
        self._timings: dict[str, list[float]] = {}

    @contextmanager
    def profile(self, operation_name: str) -> Generator[None, None, None]:
        """Context manager for profiling an operation.

        Args:
            operation_name: Name of the operation to profile

        Yields:
            None

        Example:
            with profiler.profile("data_fetch"):
                fetch_data()
        """
        start_time = time.perf_counter()
        try:
            yield
        finally:
            elapsed = time.perf_counter() - start_time
            self.record_timing(operation_name, elapsed)
            self._logger.debug(f"{operation_name} took {elapsed:.4f} seconds")

    def record_timing(self, operation_name: str, elapsed_time: float) -> None:
        """Record timing for an operation.

        Args:
            operation_name: Name of the operation
            elapsed_time: Elapsed time in seconds
        """
        if operation_name not in self._timings:
            self._timings[operation_name] = []
        self._timings[operation_name].append(elapsed_time)

    def get_stats(self, operation_name: str) -> dict[str, float]:
        """Get statistics for an operation.

        Args:
            operation_name: Name of the operation

        Returns:
            Dictionary with min, max, avg, total times
        """
        if operation_name not in self._timings:
            return {"count": 0, "min": 0, "max": 0, "avg": 0, "total": 0}

        timings = self._timings[operation_name]
        return {
            "count": len(timings),
            "min": min(timings),
            "max": max(timings),
            "avg": sum(timings) / len(timings),
            "total": sum(timings),
        }

    def get_all_stats(self) -> dict[str, dict[str, float]]:
        """Get statistics for all profiled operations.

        Returns:
            Dictionary mapping operation names to their statistics
        """
        return {name: self.get_stats(name) for name in self._timings}

    def clear(self) -> None:
        """Clear all recorded timings."""
        self._timings.clear()

    def get_timestamp(self) -> str:
        """Get current timestamp as ISO format string.

        Returns:
            ISO format timestamp string
        """
        return datetime.now().isoformat()

    def format_duration(self, seconds: float) -> str:
        """Format duration in human-readable format.

        Args:
            seconds: Duration in seconds

        Returns:
            Formatted duration string
        """
        if seconds < 0.001:
            return f"{seconds * 1_000_000:.2f} µs"
        elif seconds < 1:
            return f"{seconds * 1000:.2f} ms"
        elif seconds < 60:
            return f"{seconds:.2f} s"
        else:
            minutes = int(seconds // 60)
            remaining_seconds = seconds % 60
            return f"{minutes}m {remaining_seconds:.2f}s"

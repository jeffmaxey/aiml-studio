"""Application Manager for handling application state, sessions, and utilities."""

import logging
from abc import ABC, abstractmethod
from typing import Any

from aiml_studio.utilities.logger import get_logger
from aiml_studio.utilities.profiler import Profiler


class ApplicationManager(ABC):
    """Abstract base class for managing application state, sessions, and utilities.

    This class provides a framework for managing:
    - Application state and configuration
    - User sessions and authentication
    - Logging and profiling utilities
    - Settings management
    """

    def __init__(self) -> None:
        """Initialize the ApplicationManager."""
        self._state: dict[str, Any] = {}
        self._sessions: dict[str, dict[str, Any]] = {}
        self._logger = get_logger(__name__)
        self._profiler = Profiler()
        self._settings: dict[str, Any] = {}

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the application manager.

        This method should be implemented to set up any necessary
        resources, connections, or configurations.
        """
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown the application manager.

        This method should be implemented to clean up resources,
        close connections, and perform any necessary cleanup.
        """
        pass

    def get_state(self, key: str, default: Any = None) -> Any:
        """Get a value from the application state.

        Args:
            key: The state key to retrieve
            default: Default value if key doesn't exist

        Returns:
            The state value or default
        """
        return self._state.get(key, default)

    def set_state(self, key: str, value: Any) -> None:
        """Set a value in the application state.

        Args:
            key: The state key to set
            value: The value to store
        """
        self._state[key] = value
        self._logger.debug(f"State updated: {key} = {value}")

    def clear_state(self) -> None:
        """Clear all application state."""
        self._state.clear()
        self._logger.info("Application state cleared")

    def create_session(self, session_id: str, user_data: dict[str, Any]) -> None:
        """Create a new user session.

        Args:
            session_id: Unique session identifier
            user_data: User data to store in session
        """
        self._sessions[session_id] = {
            "user_data": user_data,
            "created_at": self._profiler.get_timestamp(),
        }
        self._logger.info(f"Session created: {session_id}")

    def get_session(self, session_id: str) -> dict[str, Any] | None:
        """Get session data.

        Args:
            session_id: Session identifier

        Returns:
            Session data or None if not found
        """
        return self._sessions.get(session_id)

    def delete_session(self, session_id: str) -> None:
        """Delete a user session.

        Args:
            session_id: Session identifier
        """
        if session_id in self._sessions:
            del self._sessions[session_id]
            self._logger.info(f"Session deleted: {session_id}")

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a setting value.

        Args:
            key: Setting key
            default: Default value if not found

        Returns:
            Setting value or default
        """
        return self._settings.get(key, default)

    def set_setting(self, key: str, value: Any) -> None:
        """Set a setting value.

        Args:
            key: Setting key
            value: Setting value
        """
        self._settings[key] = value
        self._logger.debug(f"Setting updated: {key} = {value}")

    def get_logger(self) -> logging.Logger:
        """Get the application logger.

        Returns:
            Logger instance
        """
        return self._logger

    def get_profiler(self) -> Profiler:
        """Get the application profiler.

        Returns:
            Profiler instance
        """
        return self._profiler


class DefaultApplicationManager(ApplicationManager):
    """Default implementation of ApplicationManager."""

    def initialize(self) -> None:
        """Initialize the default application manager."""
        self._logger.info("DefaultApplicationManager initialized")
        self.set_state("initialized", True)
        self.set_state("theme", "light")
        self.set_state("rtl", False)
        self.set_state("navbar_collapsed", False)
        self.set_state("aside_collapsed", True)

    def shutdown(self) -> None:
        """Shutdown the default application manager."""
        self._logger.info("DefaultApplicationManager shutting down")
        self.clear_state()
        self._sessions.clear()

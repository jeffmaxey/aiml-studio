"""Logger utility for AIML Studio."""

import logging
import sys
from typing import Any


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Get a configured logger instance.

    Args:
        name: Logger name (typically __name__)
        level: Logging level (default: INFO)

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Only configure if no handlers exist
    if not logger.handlers:
        logger.setLevel(level)

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


class LoggerMixin:
    """Mixin class to add logging capabilities to any class."""

    @property
    def logger(self) -> logging.Logger:
        """Get logger for this class.

        Returns:
            Logger instance
        """
        if not hasattr(self, "_logger"):
            self._logger = get_logger(self.__class__.__name__)
        return self._logger

    def log_info(self, message: str, **kwargs: Any) -> None:
        """Log an info message.

        Args:
            message: Message to log
            **kwargs: Additional context
        """
        self.logger.info(message, extra=kwargs)

    def log_warning(self, message: str, **kwargs: Any) -> None:
        """Log a warning message.

        Args:
            message: Message to log
            **kwargs: Additional context
        """
        self.logger.warning(message, extra=kwargs)

    def log_error(self, message: str, **kwargs: Any) -> None:
        """Log an error message.

        Args:
            message: Message to log
            **kwargs: Additional context
        """
        self.logger.error(message, extra=kwargs)

    def log_debug(self, message: str, **kwargs: Any) -> None:
        """Log a debug message.

        Args:
            message: Message to log
            **kwargs: Additional context
        """
        self.logger.debug(message, extra=kwargs)

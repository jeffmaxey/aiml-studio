"""Data Manager for handling all application data operations."""

from abc import ABC, abstractmethod
from typing import Any

from aiml_studio.utilities.logger import get_logger


class DataManager(ABC):
    """Abstract base class for managing application data.

    This class provides a framework for:
    - Creating new data records
    - Retrieving data records
    - Updating existing records
    - Deleting records
    - Storing and managing data
    """

    def __init__(self) -> None:
        """Initialize the DataManager."""
        self._logger = get_logger(__name__)
        self._data_store: dict[str, dict[str, Any]] = {}

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the data manager.

        This method should be implemented to set up data storage,
        connections, or any necessary resources.
        """
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Shutdown the data manager.

        This method should be implemented to clean up resources
        and close connections.
        """
        pass

    @abstractmethod
    def create(self, entity_type: str, entity_id: str, data: dict[str, Any]) -> bool:
        """Create a new data record.

        Args:
            entity_type: Type of entity (e.g., 'project', 'data_source')
            entity_id: Unique identifier for the entity
            data: Data to store

        Returns:
            True if successful, False otherwise
        """
        pass

    @abstractmethod
    def retrieve(self, entity_type: str, entity_id: str) -> dict[str, Any] | None:
        """Retrieve a data record.

        Args:
            entity_type: Type of entity
            entity_id: Entity identifier

        Returns:
            Entity data or None if not found
        """
        pass

    @abstractmethod
    def update(self, entity_type: str, entity_id: str, data: dict[str, Any]) -> bool:
        """Update an existing data record.

        Args:
            entity_type: Type of entity
            entity_id: Entity identifier
            data: Updated data

        Returns:
            True if successful, False otherwise
        """
        pass

    @abstractmethod
    def delete(self, entity_type: str, entity_id: str) -> bool:
        """Delete a data record.

        Args:
            entity_type: Type of entity
            entity_id: Entity identifier

        Returns:
            True if successful, False otherwise
        """
        pass

    @abstractmethod
    def list_all(self, entity_type: str) -> list[dict[str, Any]]:
        """List all records of a given entity type.

        Args:
            entity_type: Type of entity

        Returns:
            List of entity records
        """
        pass

    @abstractmethod
    def search(self, entity_type: str, filters: dict[str, Any]) -> list[dict[str, Any]]:
        """Search for records matching filters.

        Args:
            entity_type: Type of entity
            filters: Search filters

        Returns:
            List of matching records
        """
        pass


class InMemoryDataManager(DataManager):
    """In-memory implementation of DataManager for development and testing."""

    def initialize(self) -> None:
        """Initialize the in-memory data manager."""
        self._logger.info("InMemoryDataManager initialized")
        self._data_store = {
            "projects": {},
            "data_sources": {},
            "logs": {},
            "users": {},
        }

    def shutdown(self) -> None:
        """Shutdown the in-memory data manager."""
        self._logger.info("InMemoryDataManager shutting down")
        self._data_store.clear()

    def create(self, entity_type: str, entity_id: str, data: dict[str, Any]) -> bool:
        """Create a new data record.

        Args:
            entity_type: Type of entity
            entity_id: Unique identifier
            data: Data to store

        Returns:
            True if successful
        """
        try:
            if entity_type not in self._data_store:
                self._data_store[entity_type] = {}

            if entity_id in self._data_store[entity_type]:
                self._logger.warning(f"Entity {entity_type}/{entity_id} already exists")
                return False

            self._data_store[entity_type][entity_id] = data
            self._logger.info(f"Created {entity_type}/{entity_id}")
            return True
        except Exception:
            self._logger.exception(f"Error creating {entity_type}/{entity_id}")
            return False

    def retrieve(self, entity_type: str, entity_id: str) -> dict[str, Any] | None:
        """Retrieve a data record.

        Args:
            entity_type: Type of entity
            entity_id: Entity identifier

        Returns:
            Entity data or None
        """
        if entity_type not in self._data_store:
            return None
        return self._data_store[entity_type].get(entity_id)

    def update(self, entity_type: str, entity_id: str, data: dict[str, Any]) -> bool:
        """Update an existing data record.

        Args:
            entity_type: Type of entity
            entity_id: Entity identifier
            data: Updated data

        Returns:
            True if successful
        """
        try:
            if entity_type not in self._data_store:
                self._logger.warning(f"Entity type {entity_type} not found")
                return False

            if entity_id not in self._data_store[entity_type]:
                self._logger.warning(f"Entity {entity_type}/{entity_id} not found")
                return False

            self._data_store[entity_type][entity_id].update(data)
            self._logger.info(f"Updated {entity_type}/{entity_id}")
            return True
        except Exception:
            self._logger.exception(f"Error updating {entity_type}/{entity_id}")
            return False

    def delete(self, entity_type: str, entity_id: str) -> bool:
        """Delete a data record.

        Args:
            entity_type: Type of entity
            entity_id: Entity identifier

        Returns:
            True if successful
        """
        try:
            if entity_type not in self._data_store:
                return False

            if entity_id in self._data_store[entity_type]:
                del self._data_store[entity_type][entity_id]
                self._logger.info(f"Deleted {entity_type}/{entity_id}")
                return True
            else:
                return False
        except Exception:
            self._logger.exception(f"Error deleting {entity_type}/{entity_id}")
            return False

    def list_all(self, entity_type: str) -> list[dict[str, Any]]:
        """List all records of a given entity type.

        Args:
            entity_type: Type of entity

        Returns:
            List of entity records
        """
        if entity_type not in self._data_store:
            return []
        return list(self._data_store[entity_type].values())

    def search(self, entity_type: str, filters: dict[str, Any]) -> list[dict[str, Any]]:
        """Search for records matching filters.

        Args:
            entity_type: Type of entity
            filters: Search filters

        Returns:
            List of matching records
        """
        all_records = self.list_all(entity_type)
        if not filters:
            return all_records

        results = []
        for record in all_records:
            match = True
            for key, value in filters.items():
                if key not in record or record[key] != value:
                    match = False
                    break
            if match:
                results.append(record)

        return results

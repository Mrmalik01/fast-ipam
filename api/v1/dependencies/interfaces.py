from abc import ABC, abstractmethod
from typing import Any


class CreateModelInterface(ABC):

    @abstractmethod
    def _validate(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def create(self, *args, **kwargs) -> Any:
        pass


class UpdateModelInterface(ABC):

    @abstractmethod
    def update(self, *args, **kwargs) -> Any:
        pass


class QueryModelInterface(ABC):

    @abstractmethod
    def query(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def get_item_by_pk(self, pk: str, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def get_item_by_pks(self, pk: str, sk: str, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def get_count(self, *args, **kwargs) -> int:
        pass

    @abstractmethod
    def get_all_items(self, limit: int = 10, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def get_next_page(self, last_evaluated_key: str, limit: int = 10, *args, **kwargs) -> Any:
        pass

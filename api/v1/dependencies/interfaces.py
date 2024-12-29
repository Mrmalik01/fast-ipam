from abc import ABC, abstractmethod
from typing import Any


class FactoryInterface(ABC):

    @abstractmethod
    def validate(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def create(self, *args, **kwargs) -> Any:
        pass

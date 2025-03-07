from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass  # pragma: no cover


class BaseOrderCategory(ABC):

    @abstractmethod
    def print_info(self, *args, **kwargs):
        pass  # pragma: no cover

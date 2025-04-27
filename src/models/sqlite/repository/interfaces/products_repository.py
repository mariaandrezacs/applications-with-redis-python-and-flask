from abc import ABC, abstractmethod


class ProductsRepositoryInterface(ABC):

    @abstractmethod
    def fin_product_by_name(self, product_name: str) -> tuple:
        pass

    @abstractmethod
    def insert_product(self, name: str, prince: float, quantity: int) -> None:
        pass

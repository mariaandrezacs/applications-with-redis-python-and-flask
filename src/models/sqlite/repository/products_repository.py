from sqlite3 import Connection as SqliteConnection
from .interfaces.products_repository import ProductsRepositoryInterface

class ProductsRepository(ProductsRepositoryInterface):
    def __init__(self, conn: SqliteConnection) -> None:
        self.__conn = conn

    def fin_product_by_name(self, product_name: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE name = ?",
            (product_name, )
        )
        product = cursor.fetchone()
        return product

    def insert_product(self, name: str, prince: float, quantity: int) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO products
                    (name, price, quantity)
                VALUES
                    (?, ?, ?)
            """,
            (name, prince, quantity)
        )
        self.__conn.commit()

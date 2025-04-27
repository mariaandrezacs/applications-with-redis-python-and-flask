import pytest

from src.models.sqlite.settings.connection import SqliteConnectionHandle

from .products_repository import ProductsRepository

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()

@pytest.mark.skip(reason="interacao com o banco")
def test_insert_products():
    repo = ProductsRepository(conn)

    name = "AlgumaCOisa2"
    price = 12.32
    quantity = 8

    repo.insert_product(name, price, quantity)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_product():
    repo = ProductsRepository(conn)
    name = "AlgumaCOisa2"
    response = repo.fin_product_by_name(name)
    print(response)
    print(type(response))

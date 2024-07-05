import pytest
from bun import Bun
from data import DataForTests


class TestBun:
    @pytest.mark.parametrize(
        "name,price",
        [
            (DataForTests.BLACK_BUN, DataForTests.PRICE_BLACK_BUN),
            (DataForTests.WHITE_BUN, DataForTests.PRICE_WHITE_BUN),
            (DataForTests.RED_BUN, DataForTests.PRICE_RED_BUN),
        ],
    )
    def test_method_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name,price",
        [
            (DataForTests.BLACK_BUN, DataForTests.PRICE_BLACK_BUN),
            (DataForTests.WHITE_BUN, DataForTests.PRICE_WHITE_BUN),
            (DataForTests.RED_BUN, DataForTests.PRICE_RED_BUN),
        ],
    )
    def test_method_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

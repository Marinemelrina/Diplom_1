from conftest import*
class TestBun:

    def test_bun_return_name(self, bun_choice):
        bun_name = bun_choice.name
        bun_get_name = bun_choice.get_name()

        assert bun_get_name == bun_name
    def test_bun_return_price(self, bun_choice):
        bun_price = bun_choice.price
        bun_get_price = bun_choice.get_price()

        assert bun_get_price == bun_price
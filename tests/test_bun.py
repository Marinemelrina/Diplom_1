from conftest import*
class TestBun:

    def test_bun_return_name(self, bun_choice):
        bun_name = bun_choice.name
        bun_get_name = bun_choice.get_name()

        assert bun_get_name == bun_name
    def test_bun_return_name111(self):
        bun = Bun(name="123", price=123)

        x = bun.get_name()

        assert x == "123"

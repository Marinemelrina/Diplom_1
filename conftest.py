import pytest
from bun import Bun
from helpers import Help

@pytest.fixture
def bun_choice():
    help = Help()
    bun_choice = help.bun_choice_method()
    name_bun_choice = bun_choice.name
    price_bun_choice = bun_choice.price
    return Bun(name_bun_choice, price_bun_choice)



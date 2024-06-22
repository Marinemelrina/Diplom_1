import random
from database import Database
class Help:
    def bun_choice_method(self):
        data_base = Database()
        return random.choice(data_base.available_buns())
import unittest
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame("card1", "card2")

    def test_card_has_first_card(self):
        self.assertEqual("card1", self.card_game.first_card)

    def test_card_has_second_card(self):
        self.assertEqual("card2", self.card_game.second_card)

    def test_card_has_cards(self):
        self.assertEqual("['card1', card2']", self.card_game.cards)





        
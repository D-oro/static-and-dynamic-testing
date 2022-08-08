import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("Spade", "Ace")

    def test_card_has_suit(self):
        self.assertEqual("Spade", self.card.suit)

    def test_card_has_value(self):
        self.assertEqual("Ace", self.card.value)
        








        
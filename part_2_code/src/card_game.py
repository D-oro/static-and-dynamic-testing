### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:

  def __init__(self, first_card, second_card):
    self.first_card = first_card
    self.second_card = second_card
    self.cards = [first_card, second_card]


  def check_for_ace(card):
    if card.value == 1:
      return True
    else:
      return False
   

  def highest_card(card1, card2):
    if card1.value > card2.value:
      return card1
    else:
      return card2
  

  def cards_total(cards):
    total = 0
    for card in cards:
      total += card.value
    return "You have a total of" + total8
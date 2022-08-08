### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

#all writing until this point needs to be commented out for the code to run. 

class CardGame:
#we're missing a def __init__() function. it should define card, cards, card1, card2, card.value, card1.value, card2.value, and total.

  def check_for_ace(self, card):  
    if card.value = 1: # two equal signs == needed instead of one
      return True
    else #The else statement needs a colon : at the end
      return False
  

  dif highest_card(self, card1 card2): #def is misspelled. commas between card1 and card2 are missing.
  if card1.value > card2.value: #the entire if and else statement needs to be indented one step to the right.
    return card
  else:
    return card2



def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total #the return statement needs to be indented one step to the left
  
```#these signs need to be deleted or commented out. 

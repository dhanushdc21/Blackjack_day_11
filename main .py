############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo
lets_play=input("Do you want to play a game of Blackjack ?")
if lets_play[0]=='y':
  def play():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    def compare(user,computer):
      print(f"The computer's hand {computer_cards}, total score is {computer}")
      print(f"Your hand {user_cards}, your total score is {user}")
      size_user = sum(1 for use in user_cards)
      size_computer = sum(1 for comp in computer_cards)
      if user == computer:
          print("Its a Draw.")
      if user == 0 and size_user==2:
          print("Blackjack, You Win!!!💥")
      elif computer == 0 and size_computer==2:
          print("The computer got a Blackjack, You lose.")
      elif user > 21:
          print("You lose. You gave it away 🪦")
      elif computer > 21:
          print("You Win!!!💥")
      elif computer > user:
          print("You lose.")
      elif user > computer:
          print("You Win!!!💥")
    def calculate_score(user):
        sum_of_draws = 0
        length = len(user)
        for i in range(0, length):
            sum_of_draws += user[i]
        for i in range(0, length):
            if user[i] == 11 and sum_of_draws > 21:
                user.remove(11)
                user.append(1)
                sum_of_draws -= 10
        if sum_of_draws == 21:
            return 0
        else:
            return sum_of_draws
    def deal_card(user):
        random_position1 = random.randint(0, 12)
        user.append(cards[random_position1])
    
    
    deal_card(user_cards)
    deal_card(user_cards)
    deal_card(computer_cards)
    deal_card(computer_cards)
    print(f"You chose {user_cards}.")
    print(f"Computer's first choice is {computer_cards[0]}.")
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    should_draw_again=True
    while should_draw_again:
          if computer_score <17 and computer_score!=0:
              deal_card(computer_cards)
              computer_score = calculate_score(computer_cards)
              if computer_score>=17 :
                 should_draw_again=False
    while user_score < 21:
      response = input("Do you want to draw again? Type 'y' to draw and 'n' to pass :")
      if response[0] == 'y':
        clear()
        deal_card(user_cards)
        user_score = calculate_score(user_cards)
        print(f"You chose {user_cards}, your total score is {user_score}")
      else:
        break
    compare(user_score, computer_score)
    again=input("Do you want to go go another round ?")
    if again[0]=='y':
      clear()
      play()
  play()


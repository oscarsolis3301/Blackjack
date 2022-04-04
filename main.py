import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

from art import logo

def start(menu, playing):
  play_again = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
  if (play_again).lower() == 'y':
    os.system('cls||clear')
    print(logo)
    playing = True
    return playing
  elif play_again.lower() == 'n':
    menu = False
    return menu

def player_cards(deck, score):
  for x in user_deck:
    score += x
  print (f"Your cards are: {deck}, current score: {score}")

def hit(deck, score):
  deck.append(cards[random.randint(2, 11)])
    
def bust(deck, score):
   print (f"You have bust with a score of {score}. Your cards were: {deck}")
  

while True:
    play = input("Do you want to play Blackjack? Type 'y' or 'n' ")
    if play == 'y':
        score = 0
        user_deck = []
        user_deck.append(cards[random.randint(2,11)])
        user_deck.append(cards[random.randint(2,11)])
        player_cards(user_deck, score)

        while score <= 21:
          for x in user_deck:
            score += x
          print(f'THE SCOREEEEE: {score}')
          user_hit = input('Would you like to hit? ')
          if user_hit == 'y':
            hit(user_deck, score)
        
        bust(user_deck, score)
          





# menu = True
# playing = True

# while menu:
  
#   start(menu, playing)
#   user_deck = []
#   user_deck.append(cards[random.randint(2, 11)])
#   user_deck.append(cards[random.randint(2, 11)])
#   score = 0



  
#   while playing:
#     print(f'Your cards: ' + player_cards(user_deck, score))
#     if input('Would you like to hit? ').lower() == 'y':
#       score = hit(user_deck, score)
#       print(f'THE SCORE IS {score}')
#       if score <= 21:
#         player_cards(user_deck, score)
#       elif score > 21:
#         print('Test')
#         bust(user_deck, score)
#         playing = False
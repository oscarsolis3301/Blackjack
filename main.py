import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

from art import logo

def start(playing, first_game):
  play = ' '
  while play != 'y' or 'n':
    if first_game == True:
      play = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
    else:
      play = str(input("Do you want to play again? Type 'y' or 'n': "))
    if play == 'y':
      os.system('cls||clear')
      print(logo)
      return playing
    elif play == "n":
      playing = False
      return playing
    else:
      print ('Please enter a valid response.')

def player_cards(deck, score):
  for x in deck:
    score += x
  print (f"Your cards are: {deck}, current score: {score}")

def hit(deck, score, busted):
  deck.append(cards[random.randint(2, 11)])
  for x in deck:
    score += x

  if score > 21:
    print(f'Darn! You have busted. Your final deck was {deck} with a score of {score}.')
    busted = True
    return busted
  else:
    print(f'Your new cards are: {deck}, current score: {score}')
    return busted


playing = True
first_game = True
while playing:
    playing = start(playing, first_game)
    if playing == True:
      user_deck = []
      score = 0
      busted = False
      user_deck.append(cards[random.randint(2,11)])
      user_deck.append(cards[random.randint(2,11)])
      player_cards(user_deck, score)
      while True:
        user_hit = input('Would you like to hit? ')
        if user_hit == 'y':
          busted = hit(user_deck, score, busted)
          if busted == True:
            break
          else:
            continue
        elif user_hit == 'n':
          first_game = False
          for x in user_deck:
            score += x
          print(f'Your final deck was {user_deck} with a score of {score}!')
          break
    else:
      break
print('Thank you for playing!')


#     play = input("Do you want to play Blackjack? Type 'y' or 'n' ")
#     if play == 'y':
#         user_deck = []
#         score = 0
#         user_deck.append(cards[random.randint(2,11)])
#         user_deck.append(cards[random.randint(2,11)])
#         player_cards(user_deck, score)

    #       user_hit = input('Would you like to hit? ')
    #       if user_hit == 'y':
    #         hit(user_deck, score)
    # else:
    #   playing = False

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
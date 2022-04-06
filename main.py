import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

from art import logo

def start(playing, first_game):
  """checks if the user wants to play or not"""
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
  """Checks the cards in the given deck"""
  for x in deck:
    score += x
  print (f"Your cards are: {deck}, current score: {score}")

def hit(deck, score, busted):
  """Adds a card to the deck"""
  deck.append(cards[random.randint(2, 11)])
  for x in deck:
    score += x

  if score > 21:
    busted = True
    return busted
  elif score == 21:
    return
  elif score < 21:
    print(f'Your new cards are: {deck}, current score: {score}')
    return busted

def check(u_deck, u_score, c_deck, c_score):
  """Verifies the score for the user and the computer"""
  for x in u_deck:
    u_score += x
  for y in c_deck:
    c_score += y
  return (u_score, c_score)

playing = True
first_game = True
while playing:
    """Main while loop that handles the game"""
    playing = start(playing, first_game)
    if playing == True:
      user_deck = []
      user_score = 0
      busted = False
      user_deck.append(cards[random.randint(2,11)])
      user_deck.append(cards[random.randint(2,11)])
      player_cards(user_deck, user_score)

      computer_deck = []
      computer_score = 0
      computer_deck.append(cards[random.randint(2,11)])
      computer_deck.append(cards[random.randint(2,11)])
      print(f"Computer's first card: {computer_deck[0]}")
      while True and user_score != 21 and computer_score != 21:
        user_hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_hit == 'y':
          busted = hit(user_deck, user_score, busted)
          computer_deck.append(cards[random.randint(2,11)])
          if sum(computer_deck) > 21:
            computer_score = sum(computer_deck)
            print(f"Computer's final hand: {computer_deck}, final score: {computer_score}")
            print("THE COMPUTER WENT OVER 21, YOU WIN")

            break

          if busted == True:
            user_score, computer_score = check(user_deck, user_score, computer_deck, computer_score)
            print(f"Your final hand: {user_deck}, final score: {user_score}")
            print(f"Computer's final hand: {computer_deck}, final score: {computer_score}")
            print('You went over. You lose 😭')
            break
          else:
            continue
          
        elif user_hit == 'n':
          first_game = False
          for x in user_deck:
            user_score += x
          for x in computer_deck:
            computer_score += x
          print(f'Your final hand: {user_deck}, final score: {user_score}')
          print(f"Computer's final hand: {computer_deck}, final score: {computer_score}")
          if user_score > computer_score:
            print ('You win! 😋')
          elif computer_score > user_score and computer_score <= 21:
            print ('You lose. 😭')
          elif computer_score > 21:
            print('Opponent went over. You win 👌')
          elif computer_score == user_score:
            print("YOU TIED!")
          break
      if user_score == 21:
            print('YOU GOT A BLACKJACK, YOU WIN!')
    else:
      break
print('Thank you for checking out the blackjack!')


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
import random
from art import logo
import os

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_of_players = {
  "player": [],
  "computer": []
}
score_of_player = 0
score_of_computer = 0

def dealing_cards():
  '''Method that will deal the cards
  Parameters: None
  Output: None
  '''
  cards_of_players["player"].append(random.choice(cards))
  cards_of_players["player"].append(random.choice(cards))
  cards_of_players["computer"].append(random.choice(cards))
  cards_of_players["computer"].append(random.choice(cards))

def draw_one_card_player(list):
  '''
  Method that will draw only one card
  Parameters: list
  Output: None
  '''
  card_drawn = random.choice(cards)
  current_score = calculating_score(cards_of_players['player'])
  card_drawn = random.choice(cards)
  if card_drawn == 11:
    if (current_score + 11) > 21:
      card_drawn = 1
    else: 
      card_drawn = 11
  list.append(card_drawn)

def draw_one_card_computer(list):
  current_score = calculating_score(cards_of_players['computer'])
  card_drawn = random.choice(cards)
  if card_drawn == 11:
    if (current_score + 11) > 21:
      card_drawn = 1
    else: 
      card_drawn = 11
  list.append(card_drawn)
    
  
def displaying_score_of_players():
  '''
  Method that will display the score of the player and the first card of the computer
  Parameters: None
  Output: None
  '''
  score_of_player = calculating_score(cards_of_players['player'])
  score_of_computer = calculating_score(cards_of_players['computer'])
  print(f"\tYou cards: {cards_of_players['player']}, current score: {score_of_player}")
  print(f"\tComputer's first card: {cards_of_players['computer'][0]}")

def calculating_score(cards):
  '''Calculating the score of the cards
  Parameters: List of cards
  Output: return a score
  '''
  total_score = 0
  for card in cards:
    total_score = total_score + card
  return total_score

def checking_if_computer_needs_another_card():
  '''
  Method that checks if the computer should draw another card or not
  Parameters: None
  Output: Boolean value
  '''
  if score_of_computer < 17:
    return True
  else: 
    return False

def checking_if_score_under_21():
  '''
  Checking if the score of one of the player is over 21
  Parameters: None
  Output: Boolean value
  '''
  if calculating_score(cards_of_players['player']) > 21 or calculating_score(cards_of_players['computer']) > 21:
    return False
  else: 
    return True

def display_final_score():
  '''
  Method that displays the final score of the computer and the player
  Parameters: None
  Output: None
  '''
  print(f"Your final hand: {cards_of_players['player']}, final score: {calculating_score(cards_of_players['player'])}")
  print(f"Computer's final hand: {cards_of_players['computer']}, final score: {calculating_score(cards_of_players['computer'])}")

def comparing_final_score():
  '''
  Method that compares the final score to determine who's the winner
  Parameter: None
  Output: Boolean value
  '''
  if calculating_score(cards_of_players['player']) > 21:
    print("You went over 21. You lose 😤")
    return
  if calculating_score(cards_of_players['computer']) > 21:
    print("Opponent went over 21. You win! 😁")
    return
  if calculating_score(cards_of_players['player']) > calculating_score(cards_of_players['computer']):
    print("Win with a BlackJack! 😎")
    return
  if calculating_score(cards_of_players['player']) < calculating_score(cards_of_players['computer']):
    print("You lose, opponent win with a BlackJack 😱")
    return
  if calculating_score(cards_of_players['player']) == calculating_score(cards_of_players['computer']):
    print("Draw 🙃")
    return

def checking_if_computer_can_get_another_card():
  if calculating_score(cards_of_players['computer']) < 17: 
    return True
  else: 
    return False
    
playing = input("Do you want to play a game of BlackJack, type 'y' for yes and 'n' for no: ")
while playing == "y":
  clear_console()
  cards_of_players = {
  "player": [],
  "computer": []
}
  print(logo)
  dealing_cards()
  displaying_score_of_players()
  player_decision = input("Type 'y' to get another card, type 'n' to pass: ")
  while checking_if_score_under_21() and (player_decision == "y" or         checking_if_computer_can_get_another_card()):
    if player_decision == "y" and checking_if_computer_can_get_another_card():
      draw_one_card_player(cards_of_players['player'])
      draw_one_card_computer(cards_of_players['computer'])
      displaying_score_of_players()
      if not(checking_if_score_under_21()):
        break
      player_decision = input("Type 'y' to get another card, type 'n' to pass: ")
      continue
    if player_decision == "y" and not(checking_if_computer_can_get_another_card()):
      draw_one_card_player(cards_of_players['player'])
      displaying_score_of_players()
      if not(checking_if_score_under_21()):
        break
      player_decision = input("Type 'y' to get another card, type 'n' to pass: ")
      continue
    if player_decision == "n" and checking_if_computer_can_get_another_card():
      draw_one_card_computer(cards_of_players['computer'])
      displaying_score_of_players()
      if not(checking_if_score_under_21()):
        break
      player_decision = input("Type 'y' to get another card, type 'n' to pass: ")
      continue
    
  display_final_score()
  comparing_final_score()
  playing = input("Do you want to play a game of BlackJack, type 'y' for yes and 'n' for no: ")
  
print("Thank you for using our BlackJack game!")




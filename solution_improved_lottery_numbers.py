import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))
print(f"Lottery numbers: {lottery_numbers}")
# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
highest_match_player=players[0]
highest_player_name = players[0]["name"]

for player in players:
  numbers_matched = len(player["numbers"].intersection(lottery_numbers))
  player_name = player["name"]
  if numbers_matched > len(highest_match_player["numbers"].intersection(lottery_numbers)):
    highest_match_player = player
    highest_player_name = player["name"]
    print(f"PlayerName {player_name}")
    #print(f"Player: {player["name"]}")
winnings = 100 ** numbers_matched
print(f"{highest_player_name} won ${winnings}. {numbers_matched}")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

## Uncomment print statements to see outputs to terminal

# Create a dictionary mapping letters in alphabet to corresponding scrabble points value
letter_points_zip = zip(letters, points)
letter_to_points = {k:v for k,v in letter_points_zip}
# print(letters_to_points)

# Add value for blank tiles
letter_to_points[" "] = 0
# print(letters_to_points)

# Create function that takes in a word and returns its Scrabble score
def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letter_to_points.get(letter, 0)
  return point_total

# Test score_word function
brownie_points = score_word("BROWNIE")
# print(brownie_points) # should return 15


## Score a game

# Create dictionary mapping each player to their words:
players = ["player1", "wordNerd", "Lexi Con", "Prof Reader"]
player_words = [
  ["BLUE", "TENNIS", "EXIT"],
  ["EARTH", "EYES", "MACHINE"],
  ["ERASER", "BELLY", "HUSKY"],
  ["ZAP", "COMA", "PERIOD"]
]
player_to_words = {
  k:v for k,v in zip(players, player_words)
}
# print(player_to_words)

# Create dictionary mapping players to the number of points they score
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# Print player points to console
# print(player_to_points)


## Create a function that takes in a player-s word and adds it to thier list of words played

def play_word(player, word):
  player_to_words[player] = player_to_words.get(player, [])
  player_to_words[player].append(word.upper())

## Create function that updates point totals when a word is played

def update_point_totals(game_dict):
  for player, words in game_dict.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return(f"""The current game totals are as follows:
  {player_to_points}
  """)

## Test new functions
play_word("player1", "godetia") # score: 9
play_word("wordNerd", "outages") # score: 8
play_word("Lexi Con", "darioles") # score: 9
play_word("Prof Reader", "autopen") # score: 9
# print(update_point_totals(player_to_words)) 
  # Scores should be: player1=38, wordNerd=40, Lexi Con=40, Prof Reader=43

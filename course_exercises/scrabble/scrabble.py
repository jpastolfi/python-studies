letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter: point for letter, point in zip(letters, points)}

letter_to_points.update({" ": 0})

def score_word(word):
  point_total = 0
  for letter in word:
    if letter.upper() not in letter_to_points:
      point_total += 0
      print(letter)
    else:
      point_total += letter_to_points[letter.upper()]
  return point_total

player_to_words = {
  "player1": ["blue", "tennis", "exit"],
  "wordNerd": ["earth", "eyes", "machine"],
  "Lexi Con": ["eraser", "belly", "husky"],
  "Prof Reader": ["zap", "coma", "period"]
}

player_to_points= {}

for player in player_to_words:
  player_points = 0
  for word in player_to_words[player]:
    player_points += score_word(word)
    player_to_points.update({player: player_points})

def play_word(player, word):
  player_to_words[player].append(word)

def update_point_total():
  for player in player_to_words:
    player_points = 0
    for word in player_to_words[player]:
      player_points += score_word(word)
      player_to_points.update({player: player_points})
  print(player_to_points)

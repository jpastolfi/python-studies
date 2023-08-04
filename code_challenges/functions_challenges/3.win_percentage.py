def win_percentage(wins, losses):
  total_games = wins + losses
  return int((wins / total_games) * 100)
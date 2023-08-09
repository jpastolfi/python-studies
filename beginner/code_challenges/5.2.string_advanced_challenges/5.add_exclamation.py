def add_exclamation(word):
  if len(word) > 20:
    return word
  while len(word) < 20:
    word += '!'
  return word
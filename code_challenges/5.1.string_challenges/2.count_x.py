def count_char_x(word, x):
  occurences = 0
  for letter in word:
    if letter == x:
      occurences += 1
  return occurences
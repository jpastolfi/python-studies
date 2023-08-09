def count_multi_char_x(word, x):
  remaining_letters = 0
  for section in word.split(x):
    remaining_letters += len(section)
  occurences_length = len(word) - remaining_letters
  occurences = occurences_length / len(x)
  return int(occurences)
def reverse_string(word):
  reversed_word = ''
  index = len(word) - 1
  while index >= 0:
    reversed_word += word[index]
    index -= 1
  return reversed_word
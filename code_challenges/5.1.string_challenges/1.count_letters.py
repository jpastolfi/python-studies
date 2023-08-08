def unique_english_letters(word):
  unique_letters = 0
  counted_letters = ''
  all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  for letter in word:
    if letter in all_letters and not letter in counted_letters:
      unique_letters += 1
      counted_letters += letter
  return unique_letters
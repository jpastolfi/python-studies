def word_length_dictionary(words):
  new_dict = {}
  for word in words:
    new_dict[word] = len(word)
  return new_dict
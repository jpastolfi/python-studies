def frequency_dictionary(words):
  new_dict = {}
  for word in words:
    frequency = 0
    for occurrence in words:
      if occurrence == word:
        frequency += 1
    new_dict[word] = frequency
  return new_dict
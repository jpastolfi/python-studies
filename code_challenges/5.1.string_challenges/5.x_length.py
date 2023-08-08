def x_length_words(sentence, x):
  sentence_words = sentence.split(' ')
  for word in sentence_words:
    if (len(word) < x):
      return False
  return True
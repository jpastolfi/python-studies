def every_other_letter(word):
  if len(word) == 0: return word
  occurences = ''
  for index in range(len(word)):
    if index % 2 == 0:
      occurences += word[index]
  return occurences
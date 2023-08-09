def substring_between_letters(word, start, end):
  if not start in word or not end in word:
    return word
  substring = ''
  initial = word.find(start)
  end = word.find(end)
  for index in range(len(word)):
    if index > initial and index < end:
      substring += word[index]
  return substring
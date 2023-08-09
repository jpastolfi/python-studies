def check_for_name(sentence, name):
  sentence_name = sentence.split(' ')[-1]
  return sentence_name.title() in name.title()
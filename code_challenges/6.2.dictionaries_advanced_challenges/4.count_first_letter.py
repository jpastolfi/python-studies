def count_first_letter(names):
  occurrences = {}
  for key in names.keys():
    if key[0] not in occurrences:
      occurrences[key[0]] = len(names[key])
    else:
      occurrences[key[0]] += len(names[key])
  
  return occurrences
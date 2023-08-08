def unique_values(my_dictionary):
  occurrences = []
  for value in my_dictionary.values():
    if value not in occurrences:
      occurrences.append(value)
  return len(occurrences)
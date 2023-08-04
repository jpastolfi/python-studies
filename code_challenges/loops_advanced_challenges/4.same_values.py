def same_values(list1, list2):
  length = len(list1) - 1
  current = 0
  matches = []
  while current <= length:
    if list1[current] == list2[current]:
      matches.append(current)
    current += 1
  return matches
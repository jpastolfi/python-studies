def reversed_list(list1, list2):
  length = len(list1) - 1
  initial = 0
  while initial <= length:
    if list1[initial] != list2[length]:
      return False
    initial += 1
    length -= 1
  return True
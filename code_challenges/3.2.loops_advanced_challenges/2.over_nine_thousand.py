def over_nine_thousand(list):
  total = 0
  for number in list:
    if total <= 9000:
      total += number
  return total
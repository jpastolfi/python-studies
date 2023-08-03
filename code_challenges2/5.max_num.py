def max_num(num1, num2, num3):
  sorted_list = sorted([num1, num2, num3])
  if sorted_list.count(sorted_list[-1]) >= 2:
    return "It's a tie!"
  return sorted_list[-1]
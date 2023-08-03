import math
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    one_before = int((len(my_list) / 2) - 1)
    one_after = int(len(my_list) / 2)
    middle = (my_list[one_before] + my_list[one_after]) / 2
  else:
    middle = my_list[math.floor(len(my_list) / 2)]
  return middle
def delete_starting_evens(my_list):
  while len(my_list) > 0 and my_list[0] % 2 == 0:
    my_list.pop(0)
  return my_list
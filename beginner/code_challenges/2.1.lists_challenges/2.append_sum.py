def append_sum(my_list):
  for i in range(3):
    num_to_add = my_list[-1] + my_list[-2]
    my_list.append(num_to_add)
  return my_list
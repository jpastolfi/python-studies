def double_index(my_list, index):
  if index >= len(my_list):
    return my_list
  doubled_element = my_list[index] * 2
  list = my_list[:index] + [doubled_element] + my_list[index + 1:]
  return list
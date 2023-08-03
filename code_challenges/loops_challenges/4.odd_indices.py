def odd_indices(my_list):
  odd_list = []
  for index in range(len(my_list)):
    if index % 2 != 0:
      odd_list.append(my_list[index])
  return odd_list
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item2) > my_list.count(item1):
    return item2
  return item1
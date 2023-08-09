def max_key(my_dictionary):
  max_value = max(my_dictionary.values())
  for key in my_dictionary:
    if my_dictionary[key] == max_value:
      return key
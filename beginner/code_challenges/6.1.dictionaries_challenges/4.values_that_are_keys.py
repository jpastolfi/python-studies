def values_that_are_keys(my_dictionary):
  twins = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      twins.append(value)
  return twins
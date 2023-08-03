def divisible_by_ten(nums):
  counter = 0
  for number in nums:
    if number % 10 == 0:
      counter += 1
  return counter
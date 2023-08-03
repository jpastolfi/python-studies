def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  total_expenses = sum([food_bill, electricity_bill, internet_bill, rent])
  print(total_expenses)
  print(budget)
  if budget < total_expenses:
    return True
  else:
    return False
def exponents(bases, powers):
  raised = []
  for base in bases:
    for power in powers:
      raised.append(base ** power)
  return raised
def swap(a,b):
  print(f"Before: a = {a}, b = {b})

  a , b = b , a

  print(f"After: a = {a}, b = {b})

  return a, b

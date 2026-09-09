# Direct recursion (_rec)

def sum_of_first_n_rec(n):
  if n <= 0:
    return 0
  else:
    return n + sum_of_first_n_rec(n - 1)

def factorial_rec(n):
  if n <= 0:
    return 1
  else:
    return n * factorial_rec(n - 1)

def fibonacci_rec(n):
  if n <= 1:
    return n
  else:
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def greatest_common_divisor_rec(a, b):
  if b == 0:
    return a
  else:
    return greatest_common_divisor_rec(b, a % b)

def least_common_multiple_rec(a, b):
  return (a // greatest_common_divisor_rec(a, b)) * b

# Accumulator recursion (_acc): educational bridge, no TCO in Python

def sum_of_first_n_acc(n):
  return sum_of_first_n_acc_help(n, 0)

def sum_of_first_n_acc_help(n, acc):
  if n <= 0:
    return acc
  else:
    return sum_of_first_n_acc_help(n - 1, n + acc)

def factorial_acc(n):
  return factorial_acc_help(n, 1)

def factorial_acc_help(n, acc):
  if n <= 1:
    return acc
  else:
    return factorial_acc_help(n - 1, n * acc)

def fibonacci_acc(n):
  return fibonacci_acc_help(n, 0, 1)

def fibonacci_acc_help(n, acc2, acc1):
  if n <= 0:
    return acc2
  elif n <= 2:
    return acc1 + acc2
  else:
    return fibonacci_acc_help(n - 1, acc1, acc1 + acc2)

def greatest_common_divisor_acc(a, b):
  return greatest_common_divisor_acc_help(a, b)

def greatest_common_divisor_acc_help(a, b):
  if b == 0:
    return a
  else:
    return greatest_common_divisor_acc_help(b, a % b)

def least_common_multiple_acc(a, b):
  return (a // greatest_common_divisor_acc(a, b)) * b

# Iterative (_ite)

def sum_of_first_n_ite(n):
  result = 0
  for i in range(1, n + 1):
    result += i
  return result

def factorial_ite(n):
  acc = 1
  for i in range(2, n + 1):
    acc *= i
  return acc

def fibonacci_ite(n):
  if n <= 1:
    return n
  else:
    acc2 = 0
    acc1 = 1
    for _ in range(2, n):
      acc2, acc1 = acc1, acc1 + acc2
    return acc1 + acc2

def greatest_common_divisor_ite(a, b):
  while b:
    a, b = b, a % b
  return a

def least_common_multiple_ite(a, b):
  return (a // greatest_common_divisor_ite(a, b)) * b

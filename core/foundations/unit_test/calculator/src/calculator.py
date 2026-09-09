def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    result = 0
    for _ in range(b):
        result = addition(result, a)
    return result

def division(a, b):
    remaining = a
    quotient = 0
    while remaining >= b:
        remaining = subtraction(remaining, b)
        quotient = addition(quotient, 1)
    return quotient

def modulus(a, b):
    q = division(a, b)
    p = multiplication(q, b)
    return subtraction(a, p)

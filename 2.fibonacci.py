def pertence_fibonacci(n):
    a, b = 0, 1
    if n == a or n == b:
        return True
    while b < n:
        a, b = b, a + b
        if b == n:
            return True
    return False

numero = 34

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
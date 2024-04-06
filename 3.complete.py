
def sequencia_a(n):
    return [1 + 2*i for i in range(n)]

def sequencia_b(n):
    return [2**i for i in range(1, n+1)]

def sequencia_c(n):
    return [i**2 for i in range(n)]

def sequencia_d(n):
    return [(2*i + 2)**2 for i in range(n)]

def sequencia_e(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def sequencia_f(n):
    seq = [2, 10, 12, 16, 17, 18, 19]
    if n <= len(seq):
        return seq[:n]
    else:
        for i in range(len(seq), n):
            seq.append(seq[-1] + 1)  
    return seq

print("Sequência a) próximo número:", sequencia_a(5)[-1])
print("Sequência b) próximo número:", sequencia_b(7)[-1])
print("Sequência c) próximo número:", sequencia_c(8)[-1])
print("Sequência d) próximo número:", sequencia_d(5)[-1])
print("Sequência e) próximo número:", sequencia_e(7)[-1])
print("Sequência f) próximo número:", sequencia_f(8)[-1])
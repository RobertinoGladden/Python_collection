def fibonacci(n):
    urutan = []
    a, b = 0, 1
    while a < n:
        urutan.append(a)
        a, b = b, a + b
    return urutan

n = 100  #Bisa diganti
fib_sequence = fibonacci(n)
print(fib_sequence)
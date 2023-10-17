def fibonacci(n):
    urutan = []
    a, b = 0, 1
    while a < n:
        urutan.append(a)
        a, b = b, a + b
    return urutan

n = 50  #Bisa diganti
hasil = fibonacci(n)
print(hasil)
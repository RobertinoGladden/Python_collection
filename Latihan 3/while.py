iter = 0  #inisiasi iterasi
a = int(input("Enter any value of A: "))
b = int(input("Enter any value of B(should be less than A): "))

while b < a: #loop akan terus jika b kurang dari a
    print("a = ", a)
    print("b = ", b)
    b = b + (a % 2) #penghitungan b
    a = a - 1 #penghitungan a
    iter = iter + 1 
print("iter = ", iter)
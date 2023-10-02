num = int(input("Enter any number of people: "))
accum = 0

for i in range(1, num + 1, 1):
    text = "height for person-" + str(i) + " = "
    price = int(input(text)) #input nilai height sementara setiap orang sebelum dikalkukasi
    accum = accum + price #kalkulasi nilai height semua orang
print("The average height is = ", accum/num)
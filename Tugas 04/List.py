# Robertino Gladden Narendra
# 1101223309
# List Bilangan Ganjil dan Genap

# Buat list terlebih dahulu
ListGenap = []
ListGanjil = []

# Sorting
for i in range (1,21):
    if i % 2 == 0:
        ListGenap.append(i)
    else:
        ListGanjil.append(i)

#Print hasil
print('List pada Bilangan Genap', ListGenap)
print('List pada Bilangan Ganjil', ListGanjil)
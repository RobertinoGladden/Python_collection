# Check Number
# Robertino Gladden Narendra
# TT-46-11

# Start
nilai = int(input("Masukkan Nilai yang akan dicek :"))

# Check Number
# Nilai >= 10 dan <= 20
# Nilai bilangan genap
if nilai >= 10 and nilai <= 20 and nilai % 2 == 0:
    print(f"Bilangan {nilai} antara 10 sampai 20 dan bilangan genap")
else:
    print(f"{nilai} bukan bilangan antara 10 sampai 20 atau bilangan genap")
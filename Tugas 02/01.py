# Hitung Volume dan Luas Permukaan Tabung
# Robertino Gladden Narendra (1101223309)
# TT-46-11

# Menetapkan nilai variabel
phi = 3.14
r = int(input("Jari-Jari Tabung :"))
h = int(input("Tinggi Tabung :"))

# Hitung Volume Tabung
volume = phi * r**2 * h

# Hitung Luas Permukaan
luas_permukaan = 2 * phi * r * (r + h)

# Tampilkan Hasil
print(f"Volume tabung dengan jari-jari 7 dan tinggi tabung 28 = {volume:.2f}")
print(f"Luas permukaan tabung dengan jari-jari 7 dan tinggi tabung 28 = {luas_permukaan: f}")
# Robertino Gladden Narendra
# 1101223309
# List Bilangan Ganjil dan Genap

# Dictionary Album AC/DC
albumSong = {
    "Thriller":1982,
    "Back in Black":1980,
    "The Dark Side of the Moon":1973,
    "The Bodyguard":1992,
    "Bat Out of Hell":1977,
    "Their Greatest Hits(1971-1975)":1976
}

# Tampilkan setiap nilai yang ada pada dictionary tersebut
print("Lagu-lagu dalam Album AC/DC:")
for album, year in albumSong.items():
    print(f"{album}: {year}")

# Tampilkan nilai untuk data "The Dark Side of the Moon"
yearSong = albumSong.get("The Dark Side of the Moon")
if yearSong is not None:
    print(f"Tahun Rilis: {yearSong}")
else:
    print("Tidak Ditemukan")

# Tambahkan data pada dictionary “Soulvaki” dengan nilai 1993
albumSong['Soulvaki'] = 1993
print(albumSong)

# Hitung banyaknya value pada dictionary
print(len(albumSong))

# Check 1992 terdapat pada dictionary kemudian print pesan “Data 1992 ditemukan”
if 1992 in albumSong.values() :
    print('Data 1992 ditemukan')
else :
    print('Data 1992 tidak ditemukan')
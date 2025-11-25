# Membuat sebuah list berisi beberapa data
nama_temans = ["Budi", "Siti", "Rina", "Andi", "Nina"]

# Menampilkan seluruh isi list
print(nama_temans)  

# Mengambil data berdasarkan index
# Index dimulai dari 0, jadi 0=Budi, 1=Siti, 2=Rina, dst.
print(nama_temans[2])  # Mengambil data ke-3 yaitu "Rina"

# Menambahkan data baru ke list
nama_temans.append("Tono")  
print(nama_temans)  # Tono ditambahkan di akhir list

# Mengubah isi list
nama_temans[1] = "Putri"  # Mengubah Siti menjadi Putri
print(nama_temans)

# Menghapus data dari list
nama_temans.remove("Andi")
print(nama_temans)

# Menghitung jumlah data dalam list
print(len(nama_temans))  # len() = menghitung panjang list

# Looping untuk menampilkan semua isi list
for nama in nama_temans:
    print(nama)

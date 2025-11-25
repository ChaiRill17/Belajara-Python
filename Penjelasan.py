# TIPE DATA PYTHON
# Kode ini menampilkan semua tipe data dasar pada Python

print("--- TIPE DATA PYTHON ---\n")

# 1. Integer (bilangan bulat)
angka_bulat = 10
print("Integer:", angka_bulat, "=> tipe:", type(angka_bulat))

# 2. Float (bilangan desimal)
angka_desimal = 3.14
print("Float:", angka_desimal, "=> tipe:", type(angka_desimal))

# 3. String (teks)
teks = "Hello Python"
print("String:", teks, "=> tipe:", type(teks))

# 4. Boolean (True/False)
benar = True
print("Boolean:", benar, "=> tipe:", type(benar))

# 5. List (kumpulan data yang bisa diubah)
buah = ["apel", "jeruk", "mangga"]
print("List:", buah, "=> tipe:", type(buah))

# 6. Tuple (kumpulan data yang tidak bisa diubah)
angka_tuple = (1, 2, 3)
print("Tuple:", angka_tuple, "=> tipe:", type(angka_tuple))

# 7. Dictionary (data pasangan key : value)
orang = {"nama": "Dika", "umur": 18}
print("Dictionary:", orang, "=> tipe:", type(orang))

# 8. Set (kumpulan data unik, tidak ada duplikat)
unik = {1, 2, 3, 3, 2}
print("Set:", unik, "=> tipe:", type(unik))

print("\n--- PENJELASAN SINGKAT ---")
print("int      = bilangan bulat")
print("float    = bilangan desimal")
print("str      = teks")
print("bool     = True/False")
print("list     = data bisa diubah")
print("tuple    = data tidak bisa diubah")
print("dict     = data key:value")
print("set      = data unik (tidak duplikat)")

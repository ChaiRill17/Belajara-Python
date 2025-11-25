# Ringkasan Operator / Method List Python
# Versi singkat, jelas, dan rapi

# append(x)  -> Menambah elemen ke akhir list
buah = ["apel", "jeruk"]
buah.append("mangga")

# insert(i, x) -> Menambah elemen pada index tertentu
buah.insert(1, "kiwi")

# remove(x) -> Hapus elemen berdasarkan nilai
buah.remove("jeruk")

# pop(i) -> Hapus elemen berdasarkan index
buah.pop(0)

# pop() -> Hapus elemen terakhir
buah.pop()

# clear() -> Menghapus semua isi list
buah.clear()

# copy() -> Menyalin list
angka = [1, 2, 3]
salin = angka.copy()

# extend(list) -> Menggabungkan dua list
a = [1, 2]
b = [3, 4]
a.extend(b)

# count(x) -> Menghitung jumlah kemunculan nilai
angka2 = [1, 2, 2, 3]
angka2.count(2)

# index(x) -> Mencari posisi elemen dalam list
buah2 = ["apel", "mangga", "nanas"]
buah2.index("mangga")

# sort() -> Mengurutkan list (kecil ke besar)
angka3 = [5, 1, 4]
angka3.sort()

# sort(reverse=True) -> Urut besar ke kecil
angka3.sort(reverse=True)

# reverse() -> Membalik urutan list
angka4 = [1, 2, 3]
angka4.reverse()

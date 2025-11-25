# =========================================================
# FUNGSI (FUNCTION) PYTHON — VERSI RINGKAS & LENGKAP
# =========================================================

# Fungsi = blok kode yang bisa dipanggil berkali-kali.
# Tujuan: menghindari pengulangan kode, membuat program rapi.

# ---------------------------------------------------------
# 1. FUNGSI DASAR
# ---------------------------------------------------------
def halo():
    print("Halo dunia!")

halo()   # Memanggil fungsi


# ---------------------------------------------------------
# 2. FUNGSI DENGAN PARAMETER
# ---------------------------------------------------------
def sapa(nama):
    print("Halo", nama)

sapa("Chairil")


# ---------------------------------------------------------
# 3. FUNGSI DENGAN NILAI BALIK (return)
# ---------------------------------------------------------
def tambah(a, b):
    return a + b

hasil = tambah(3, 2)
print("Hasil =", hasil)


# ---------------------------------------------------------
# 4. PARAMETER DENGAN NILAI DEFAULT
# ---------------------------------------------------------
def sapa_default(nama="User"):
    print("Halo", nama)

sapa_default()
sapa_default("Dirga")


# ---------------------------------------------------------
# 5. *ARGS = banyak nilai (tanpa batas)
# ---------------------------------------------------------
def total(*angka):
    jumlah = 0
    for i in angka:
        jumlah += i
    return jumlah

print(total(1, 2, 3, 4))   # Output: 10


# ---------------------------------------------------------
# 6. **KWARGS = banyak nilai dengan nama (key=value)
# ---------------------------------------------------------
def info_user(**data):
    for key, value in data.items():
        print(key, ":", value)

info_user(nama="Chairil", umur=20, kota="Padang")


# ---------------------------------------------------------
# 7. FUNGSI DI DALAM FUNGSI
# ---------------------------------------------------------
def luar():
    print("Ini fungsi luar")

    def dalam():
        print("Ini fungsi dalam")

    dalam()

luar()


# ---------------------------------------------------------
# 8. LAMBDA (fungsi cepat 1 baris)
# ---------------------------------------------------------
kali = lambda x, y: x * y
print(kali(4, 2))


# ---------------------------------------------------------
# 9. PASS (fungsi kosong untuk sementara)
# ---------------------------------------------------------
def fitur_belum_jadi():
    pass   # Tidak error, tapi belum ada isi


# ---------------------------------------------------------
# RINGKASAN CEPAT:
# def = membuat fungsi
# nama_fungsi() = memanggil
# parameter = data masuk
# return = mengembalikan nilai
# *args = banyak data
# **kwargs = banyak data dengan nama
# lambda = fungsi satu baris
# pass = isi kosong
# ---------------------------------------------------------

# IF: digunakan untuk mengecek kondisi pertama. Jika True, kode di dalamnya dijalankan.
# ELIF: digunakan jika kondisi IF sebelumnya False. Bisa ada banyak elif.
# ELSE: dijalankan jika semua kondisi sebelumnya False. Tidak punya syarat.

# Program akan membaca kondisi dari atas ke bawah dan berhenti ketika menemukan kondisi True.

# CONTOH PROGRAM GABUNGAN IF–ELIF–ELSE
# Program menentukan status nilai berdasarkan angka


nilai = 85  # kamu bisa ubah angkanya untuk mencoba

print("Nilai kamu:", nilai)

if nilai >= 90:
    print("Hasil: Sangat Baik (A)")
elif nilai >= 75:
    print("Hasil: Baik (B)")
elif nilai >= 60:
    print("Hasil: Cukup (C)")
elif nilai >= 40:
    print("Hasil: Kurang (D)")
else:
    print("Hasil: Sangat Kurang (E)")

print("Program selesai.")

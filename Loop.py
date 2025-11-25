# For loop digunakan ketika jumlah perulangannya sudah jelas.
# Misalnya ingin mengulang sebanyak 5 kali.
# range(5) artinya menghasilkan angka 0 sampai 4 (total 5 kali).
print("=== FOR LOOP ===")

for i in range(5):  # i akan berubah dari 0,1,2,3,4
    print(f"Perulangan ke-{i}")  # Menampilkan angka i setiap perulangan


# While loop digunakan ketika kita ingin mengulang
# SELAMA kondisi bernilai True.
# Pada contoh ini, loop akan berjalan selama count <= 5.
print("\n=== WHILE LOOP ===")

count = 1  # nilai awal
while count <= 5:  # kondisi loop
    print(f"Perulangan ke-{count}")  # tampilkan nilai count
    count += 1  # meningkatkan nilai count agar loop berhenti
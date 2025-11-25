height = int(input("Berapa tinggi mu? "))
credits = int(input("Berapa jumlah uang mu? "))

if height >= 165 and credits >=10:
  print('Tinggi dan uang anda mencukupi')

elif height <=165 and credits >=10:
  print('Maaf tinggi mu tidak mencukupi')

elif height >=165 and credits <= 10:
  print("Kamu tidak memiliki uang yg cukup")

else:
  print("kamu tidak memenuhi semua kriteria") 

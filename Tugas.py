# Ini variabel / dats
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# Pertanyaan
print('Q1) Anda lebih suka Fajar atau senja?')
print('1) Dawn')
print('2) Dusk')

# ini input Pertanyaan 1
P1 = int(input('Masukkan jawaban anda (1-2):    '))

# True/False | ==(Sama dengan) | +=(Nilai ditambah dengan nilai sebelumnya)
if P1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif P1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Error')

# Hasil skor
print('Gryffindor:', Gryffindor)
print('Ravenclaw:', Ravenclaw)
print('Hufflepuff:', Hufflepuff)
print('Slytherin:', Slytherin )

print('Q2) Kapan saya mati, Aku ingin orang-orang mengingat ku sebagai: ')
print('1) Orang baik')
print('2) Orang hebat')
print('3) Orang bijak')
print('4) Orang berani')

P2 = int(input('Masukkan jawaban anda (1-4)'))

if P2 == 1:
    Hufflepuff += 2
elif P2 == 2:
    Slytherin += 2
elif P2 == 3:
    Ravenclaw += 2
elif P2 == 4:
    Gryffindor += 2
else:
    print('Error')

print('Gryffindor:', Gryffindor)
print('Ravenclaw:', Ravenclaw)
print('Hufflepuff:', Hufflepuff)
print('Slytherin:', Slytherin )

print('Q3) Alat musik jenis apa yang paling enak didengar')
print('1) Violin')
print('2) Trumpet')
print('3) Piano')
print('4) Drum')

P3 = int(input('Masukkan jawaban anda (1-4)'))

if P3 == 1:
    Slytherin += 4
elif P3 == 2:
    Hufflepuff += 4
elif P3 == 3:
    Ravenclaw += 4
elif P3 == 4:
    Gryffindor += 4
else:
    print('Error')

print('Gryffindor:', Gryffindor)
print('Ravenclaw:', Ravenclaw)
print('Hufflepuff:', Hufflepuff)
print('Slytherin:', Slytherin )

# Ini adalah output skor total
print('SKOR TOTAL')

print('Gryffindor:', Gryffindor)
print('Ravenclaw:', Ravenclaw)
print('Hufflepuff:', Hufflepuff)
print('Slytherin:', Slytherin )

max_score = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

if max_score == Gryffindor:
    print("🦁 Gryffindor!")
elif max_score == Ravenclaw:
    print("🦅 Ravenclaw!")
elif max_score == Hufflepuff:
    print("🦡 Hufflepuff!")
else:
    print("🐍 Slytherin!")
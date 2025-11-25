import random

pertanyaan = input("Pertanyaan:     ")
game = random.randint(1, 9)
if game == 1:
  jawaban = ("Yes - definitely")
elif game == 2:
  jawaban = ("It is decidedly so")
elif game == 3:
  jawaban = ("Without a doubt")
elif game == 4:
  jawaban = ("reply hazy, try again")
elif game == 5:
  jawaban = ("Ask again later")
elif game == 6:
  jawaban = ("Better not tell you now")
elif game == 7:
  jawaban = ("My sources say no")
elif game == 8:
  jawaban = ("Outlook not so good")
elif game == 9:
  jawaban = ("Very doubtful")

else:
  print("Ulangi")

print('Magic 8 Ball:  ' + jawaban)
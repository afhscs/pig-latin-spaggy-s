# pig latin translator by spencer smart
print("Welcome to pig latin translator, please enter the english you would like to translate into pig latin")
English = input("English: ")

eng = English.split()
print(eng)
letter = list(eng[0])
print(letter)

if letter[0] in ('a', 'e', 'i', 'o', 'u'):
 vowel = True
else:
  vowel = False

if vowel == True:
  letter.append("yay")
  print(eng)
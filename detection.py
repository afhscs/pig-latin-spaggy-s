original = input('Enter a word:')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    if first in ('a', 'e', 'i', 'o', 'u'):
        print ("vowel")
    else:
        print ("consonant")
else:
    print ("empty")
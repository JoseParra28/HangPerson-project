import random
from words import mainwords
username = input("Welcome to HangPerson! \nPlease insert your name\n")
while len(username) < 1 or username.isalpha() is False:
    print('Please insert letters only \n')
    username = input('Please inser ypu name\n')

picked = random.choice(mainwords)
print('The word has', len(picked), 'letters.')
correct = ['_'] * len(picked)
wrong = []
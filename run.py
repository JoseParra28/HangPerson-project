import random
from words import mainwords
from time import sleep

username = input("Welcome to HangPerson! \nPlease insert your name\n")
while len(username) < 1 or username.isalpha() is False:
    print('Please insert letters only \n')
    username = input('Please inser ypu name\n')

picked = random.choice(mainwords)
print('The word has', len(picked), 'letters.')
correct = ['_'] * len(picked)
wrong = []

def update():
    for i in correct:
        print(i, end='')
        print('Ok!',username, 'let me think of a word')

def loadig():
    for i in range(5):
        print('.', end='')
        sleep(0.4)
        print()        

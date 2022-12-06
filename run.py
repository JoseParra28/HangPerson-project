import random
from words import mainwords
from bodyparts import parts
from time import sleep

username = input("Welcome to HangPerson! \nPlease insert your name\n")
while len(username) < 1 or username.isalpha() is False:
    print('Please insert letters only \n')
    username = input('Please inser ypu name\n')


def update():
    for i in correct:
        print(i, end='')
        print('Ok!',username, 'let me think of a word')

def loadig():
    for i in range(4):
        print('.', end='')
        sleep(0.4)
        print()  

    loadig()              

picked = random.choice(mainwords)
print('The word has', len(picked), 'letters.')
correct = ['_'] * len(picked)
wrong = []

update()
parts(len(wrong))

while True:

    guess = input('Please guess a letter\n')
    print('Let me check...')
    loadig()

    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                correct[index] = guess
                print("That's correct", username)
                index += 1 
                update()
                parts(len(wrong))

            else:
                if guess not in wrong:
                    wrong.append(guess)
                    parts(len(wrong))
                    print("That's not correct")
                else:
                    print('You already guessed that!')
                if len(wrong) > 4:
                    print('Oh no' , username , "you didn't win this time\n Game over !!")
                    print('I picked', [picked])
                    break 
                if '_' not in correct:
                    print('Yay' , username , 'you won!')
                    break 



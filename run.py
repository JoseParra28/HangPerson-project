import random
from words import mainwords
from bodyparts import parts
from time import sleep


class Welcome:
  """
  Main class, prints out a welcome message as well as the game rules
  """
  def __init__(self, message,rules):
    self.message = message
    self.rules = rules


pregame = Welcome('hello', 'gamerules')
print('\nWelcome to HangPerson\n')
print('Game rules: I will randomly pick a word\n and you will have to guess each letter of the word,\n if the letter is correct, it will be added to the correct letters,\n but if is not correct, you will be slowly hung\n Good Luck!!')

"""
 Username is validated, it can only contain at least on letter, no numbers
"""
username = input("Please insert your name\n")
while len(username) < 1 or username.isalpha() is False:
  print('Please insert letters only 💀 \n')
  username = input("Please insert you name\n")

""" 
Main funtion, it checks for correct or wrong letters
"""
def update():
   for i in correct:
    print(i, end=' ')
   print()
print('Let me think of a word', username)

"""
Time delay funtion, simulates interaction with the user, making it look like the game in thinking.
"""
def loading():
  for i in range(6):
    print('-', end = '' )
    sleep(0.4)
  print() 

loading() 

"""
this variable picks a random word from the external list.
There are also 2 lists one for correct and one fro wrong
the correct list multiplies and amount of letters in the selected word
"""
picked = random.choice(mainwords)
print('Ok',username,'the word has', len(picked), 'letters.')
correct = ['_'] * len(picked)
wrong = []

update() 
parts(len(wrong)) 
"""
 Main game loop, it asks for an input, it also validates if the user types the wrong letter twice
 if the user looses, it will display the picked word at the end of the loop
"""
while True:

  guess = input("Please guess a letter\n")
  print("Let me see if if that's correct...")
  loading()

  if guess in picked:
    index = 0 
    for i in picked:
      if i == guess:
        correct[index] = guess
        print("That's correct 🤟 Well done",username)
      index += 1
    update()  
    parts(len(wrong))
   
  else:
      if guess not in wrong:
          wrong.append(guess)
          parts(len(wrong))
          print("That's not correct 🥺 try another letter.\n You wrote:", wrong)
      else:
          print('You already guessed that!🤯') 
  if len(wrong) > 4:
    print("Oh no",username,"you didn't win this time 💀\n Game over! 🎮")
    print(' I picked', {picked})
    break      
  if '_' not in correct:
       print('Yay!',username,'you won!!! 🙌') 
       break

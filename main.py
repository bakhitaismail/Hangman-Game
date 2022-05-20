import random


words = ['python', 'program']

picked = random.choice(words)
print(picked)

right = []
wrong = []

while True:
    print('======================')

    guess = input("Guess a letter")
    print(guess)

    if guess in picked:
      right.append(guess)
      print('Right:', right)
    else:
     wrong.append(guess)
    print('Wrong:', wrong)   
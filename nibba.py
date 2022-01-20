import random

stages=['''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']








list=['hi','hell','harmony']
chosen_word=random.choice(list)
life=6


display=[]
for i in range(len(chosen_word)):
    display+="_"


end=False
while not end:
    guess=input("guess a word").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position]=letter

    if guess not in chosen_word:
        life=life-1
        if life==0:
            end=True
            print("lose")




    print(f"{' '.join(display)}")
    print(stages[life])
    if "_" not in display:
        end=True
        print("win")



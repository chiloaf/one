print('hello')
from random import randint
opt = ['Rock','Paper','Scissors']
comp = opt[randint(0,2)]
player = False

while player == False:
  player = input('Rock, paper or scissors?')
  if player == comp:
    print('Tie!')
  elif player == 'Rock':
    if comp == 'Paper':
      print('You lost! ',comp' covers ',player)
    else:
      print('You won! ',player' covers ',comp)
    elif player == "Paper":
        if comp == "Scissors":
            print("You lose!", comp, "cut", player)
        else:
            print("You win!", player, "covers", comp)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", comp, "smashes", player)
        else:
            print("You win!", player, "cut", comp)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]

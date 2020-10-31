# TIC TAC TOE

import random

row=0
column=0
move = '0'
choice = [0,1,2,3,4,5,6,7,8]

game = [
    ['0', '1', '2'],
    ['3', '4', '5'],
    ['6', '7', '8']
]


def print_matrix(game):
    print(' '*10)
    print(' ' * 9 + '|' + ' ' * 9 + ' ' + '|' + ' ' * 9)
    print(' ' * 9 + '|' + ' ' * 9 + ' ' + '|' + ' ' * 9)
    print(' ' * 4 + game[0][0] + ' ' * 4 + '|' + ' ' * 4 + game[0][1] + ' ' * 5 + '|' + ' ' * 4 + game[0][2] + ' ' * 4)
    print(' ' * 9 + '|' + ' ' * 9 + ' ' + '|' + ' ' * 9)
    print('-' * 30)
    print(' ' * 9 + '|' + ' ' * 9 + ' ' + '|' + ' ' * 9)
    print(' ' * 9 + '|' + ' ' * 9 + ' ' + '|' + ' ' * 9)
    print(' ' * 4 + game[1][0] + ' ' * 4 + '|' + ' ' * 4 + game[1][1] + ' ' * 5 + '|' + ' ' * 4 + game[1][2] + ' ' * 4)
    print(' ' * 9 + '|' + ' ' * 9 + ' ' + '|' + ' ' * 9)
    print('-' * 30)
    print(' ' * 9 + '|' + ' ' * 9 + ' ' + '|' + ' ' * 9)
    print(' ' * 9 + '|' + ' ' * 9 + ' ' + '|' + ' ' * 9)
    print(' ' * 4 + game[2][0] + ' ' * 4 + '|' + ' ' * 4 + game[2][1] + ' ' * 5 + '|' + ' ' * 4 + game[2][2] + ' ' * 4)
    print(' ' * 9 + '|' + ' ' * 9 + ' ' + '|' + ' ' * 9)


def moves():
 global row
 global column
 global choice
 global move

 try:
  if int(move)== 0 :
        choice.remove(int(move))
        row = 0
        column = 0
  elif int(move)== 1:
        choice.remove(int(move))
        row=0
        column=1
  elif int(move) == 2:
        choice.remove(int(move))
        row = 0
        column = 2
  elif int(move) == 3:
        choice.remove(int(move))
        row = 1
        column = 0
  elif int(move) == 4:
        choice.remove(int(move))
        row = 1
        column = 1
  elif int(move) == 5:
        choice.remove(int(move))
        row = 1
        column = 2
  elif int(move) == 6:
        choice.remove(int(move))
        row = 2
        column = 0
  elif int(move) == 7:
        choice.remove(int(move))
        row = 2
        column = 1
  elif int(move) == 8:
        choice.remove(int(move))
        row = 2
        column = 2
  else :
        print("WRONG MOVE")
        move=input("CHOOSE CORRECT MOVE")
        moves()

 except ValueError:
   print("Invalid Value")
   move=input("CHOOSE AN INTEGER")
   moves()


def moved(player):
 global row
 global column
 global move
 computerweapon = 'O'
 if player == 'user':
    if game[row][column] != 'X' or 'O':
        game[row][column] = weapon
    else:
        print("MOVE TAKEN")
        move=input("CHOOSE ANOTHER MOVE")
        moves()
        moved(player)

 elif player == 'computer':
     if weapon == 'X':
         computerweapon='O'
     elif weapon == 'O':
         computerweapon='X'
     game[row][column]=computerweapon


def comp_move(game):
    global row
    global column
    global choice


    cmove = random.choice(choice)

    if int(cmove) == 0:
            choice.remove(cmove)
            row = 0
            column = 0
    elif int(cmove) == 1:
            choice.remove(cmove)
            row = 0
            column = 1
    elif int(cmove) == 2:
            choice.remove(cmove)
            row = 0
            column = 2
    elif int(cmove) == 3:
            choice.remove(cmove)
            row = 1
            column = 0
    elif int(cmove) == 4:
            choice.remove(cmove)
            row = 1
            column = 1
    elif int(cmove) == 5:
            choice.remove(cmove)
            row = 1
            column = 2
    elif int(cmove) == 6:
            choice.remove(cmove)
            row = 2
            column = 0
    elif int(cmove) == 7:
            choice.remove(cmove)
            row = 2
            column = 1
    elif int(cmove) == 8:
            choice.remove(cmove)
            row = 2
            column = 2

    moved('computer')


def checkwin(game):
    if game[0][0]==game[0][1]==game[0][2] or game[0][0]==game[1][1]==game[2][2] or game[0][0]==game[1][0]==game[2][0] :
        if game[0][0]== weapon :
            print(f"Congratulations {name} ,you have won!")
            exit()
        else:
            print("SORRY, COMPUTER HAS WON")
            exit()
    elif game[2][2]==game[1][1]==game[0][0] or game[2][2]==game[2][0]==game[2][1] or game[0][2] ==game[1][2]==game[2][2]:
        if game[2][2]== weapon :
            print(f"Congratulations {name} ,you have won!")
            exit()
        else:
            print("SORRY, COMPUTER HAS WON")
            exit()
    elif game[1][0] == game[1][1] == game[1][2] or game[0][1] == game[1][1] == game[2][1] or game[0][2]==game[1][1]==game[2][0]:
        if game[1][1]== weapon :
            print(f"Congratulations {name} ,you have won!")
            exit()
        else:
            print("SORRY, COMPUTER HAS WON")
            exit()
    elif len(choice)==0:
        print("IT IS A DRAW")



print("HI THERE")
name = input("PLEASE ENTER YOUR NAME : ")
print(f"HI {name}")
print("LETS START ")
weapon = input('CHOOSE YOUR "WEAPON" (X/O) : ')
if weapon.upper() == "X":
    weapon = 'X'
elif weapon.upper() == 'O':
    weapon = 'O'
print_matrix(game)
while len(choice)!=0:

 move = input("CHOOSE YOUR MOVE ")
 moves()
 moved('user')
 print_matrix(game)
 checkwin(game)
 comp_move(game)
 print_matrix(game)
 checkwin(game)






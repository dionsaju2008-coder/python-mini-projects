import sys
print ('if you want to play this game you want to inset a number between 1-9 which determines your position')
print()
def latest():
    print(display_board)
board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']
def display_board():
    print("+---+---+---+")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("+---+---+---+")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("+---+---+---+")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("+---+---+---+")
    print()
display_board()
def check_winner():
    if board[0]==board[1]==board[2]:
        return True
    if board[3]==board[4]==board[5]:
        return True
    if board[6]==board[7]==board[8]:
        return True
    if board[0]==board[3]==board[6]:
        return True
    if board[1]==board[4]==board[7]:
        return True
    if board[2]==board[5]==board[8]:
        return True
    if board[0]==board[4]==board[8]:
        return True
    if board[2]==board[4]==board[6]:
        return True
    else:
        return False
    
def statment_1():
    if check_winner()==True:
        print('\U0001F389 \U0001F525 Player 1 X is the winner \U0001F525 \U0001F389')
        sys.exit()
    
def statment_2():
    if check_winner()==True:
        print('\U0001F389 \U0001F525 Player 2 O is the winner \U0001F525 \U0001F389')
        sys.exit()
    
move1=int(input('what is your move x : '))
board[move1-1]='x'
display_board()

move2=int(input('what is your move o : '))
board[move2-1]='o'
display_board()

move3=int(input('what is your move x : '))
board[move3-1]='x'
display_board()

move4=int(input('what is your move o : '))
board[move4-1]='o'
display_board()
statment_1()
statment_2()

move5=int(input('what is your move x : '))
board[move5-1]='x'
display_board()
statment_1()
statment_2()

move6=int(input('what is your move o : '))
board[move6-1]='o'
display_board()
statment_1()
statment_2()

move7=int(input('what is your move x : '))
board[move7-1]='x'
display_board()
statment_1()
statment_2()

move8=int(input('what is your move o : '))
board[move8-1]='o'
display_board()
statment_1()
statment_2()

move9=int(input('what is your move x : '))
board[move9-1]='x'
display_board()
statment_1()
statment_2()

print("\U0001F600 The game is tie \U0001F600")



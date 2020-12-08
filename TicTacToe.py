board = { 'A1':'A1','B1':'B1','C1':'C1',\
          'A2':'A2','B2':'B2','C2':'C2',\
          'A3':'A3','B3':'B3','C3':'C3' }

status= 'Playing'
turn = 1

def print_board(b):
    print()
    print(b['A1'] + '|' + b['B1'] + '|' + b['C1'])
    print('--+--+--')
    print(b['A2'] + '|' + b['B2'] + '|' + b['C2'])
    print('--+--+--')
    print(b['A3'] + '|' + b['B3'] + '|' + b['C3'])
    print()

def outcome(b):
    
    global status
    status = 'Playing'

    if   b['A1'] == b['B1'] == b['C1']:
         print(f'{player} Wins!')
         status ='Game Over'
    elif b['A1'] == b['A2'] == b['A3']:
         print(f'{player} Wins!')
         status ='Game Over'
    elif b['A2'] == b['B2'] == b['C2']:
         print(f'{player} Wins!')
         status ='Game Over'
    elif b['B1'] == b['B2'] == b['B3']:
         print(f'{player} Wins!')
         status ='Game Over'
    elif b['A3'] == b['B3'] == b['C3']:
         print(f'{player} Wins!')
         status ='Game Over'
    elif b['C1'] == b['C2'] == b['C3']:
         print(f'{player} Wins!')
         status ='Game Over'
    elif b['A1'] == b['B2'] == b['C3']:
         print(f'{player} Wins!')
         status ='Game Over'
    elif b['A3'] == b['B2'] == b['C1']:
         print(f'{player} Wins!')
         status ='Game Over'
    elif turn == 9:
        print("It's a Tie! That's worse than losing!")
        status = 'Game Over'
    else:
        status = 'Playing'

while status == 'Playing':
    if turn % 2 == 1:
        player = 'X '
    else:
        player = 'O '
    
    print_board(board)
    
    print(f"It is {player}'s turn to play")
    
    play = input('Choose a position: ')
    if (play in ['A1','A2','A3','B1','B2','B3','C1','C2','C3']):
        if (board[play] in ['X ','O ']):
            print('Invalid Choice\nTry Again!')
        else:
            board[play] = player
            print_board(board)
            outcome(board)
            turn +=1
    else:        
        print('Invalid Choice\nTry Again!')

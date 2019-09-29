import random

def availspots(board):
    cells = []
    for i in range(len(board)):
        if board[i] != 'X' and board[i] != 'O':
            cells.append(board[i])
    return cells

def win(board, player):
    win_state = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def calculate_score(board):
    if win(board, cpu):
        return 1
    elif win(board, user):
        return -1
    else:
        return 0

def game_over(board):
    return win(board, cpu) or win(board, user)

def minmax(board, depth, player):
    if player == cpu:
        best = [-1, -10000]
    else:
        best = [-1, +10000]

    if depth == 0 or game_over(board):
        score =  calculate_score(board)
        return [-1, score]
    for cell in availspots(board):
        board[cell] = player
        if player == cpu:
            next_player = user
        else:
            next_player = cpu
        score = minmax(board, depth - 1, next_player)
        board[cell] = cell
        score[0] = cell
        if player == cpu:
            if score[1] > best[1]:
                #print("max score",score)
                best = score
        else:
            if score[1] < best[1]:
                best = score
    return best

def cpu_turn(board, player):
    depth = len(availspots(board))
    if depth == 0 or game_over(board):
        return
    print("Turn X")
    if depth == 9:
        move = random.randint(0,8)
        board[move] = player
    else:
        move = minmax(board, depth, player)
        board[move[0]] =  player

def user_turn(board, player):
    depth = len(availspots(board))
    if depth == 0 or game_over(board):
        return
    print("Turn O")
    move = int(input("Choose between 0 to 8"))
    if board[move] != move:
        while board[move] != move:
            move = int(input("Enter valid input"))
    board[move] = player

def print_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print("")
    return



user = 'O'
cpu = 'X'
board = [0,1,2,3,4,5,6,7,8]
while len(availspots(board)) > 0 and not game_over(board):
    cpu_turn(board,cpu)
    print_board(board)
    user_turn(board,user)
    print_board(board)

if win(board, user):
    print("User Wins")
elif win(board,cpu):
    print("Cpu Wins")
else:
    print("Draw")
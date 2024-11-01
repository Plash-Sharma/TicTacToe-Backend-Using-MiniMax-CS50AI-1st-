"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count=0
    o_count=0
    for i in board:
        for j in i:
            if j=="X":
                x_count+=1
            if j=="O":
                o_count+=1
    if(o_count < x_count):
        return "O"
    else:
        return "X"



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==None :
                action.append((i,j))
    return set(action)





def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    play=player(board)
    board1=deepcopy(board)
    i=action[0]
    j=action[1]
    if(play=="X" and 0<=i<3 and 0<=j<3 and board1[i][j]==EMPTY):
        board1[i][j]="X"
    elif(play=="O" and 0<=i<3 and 0<=j<3 and board1[i][j]==EMPTY):
        board1[i][j]="O"
    else:
        raise ValueError
    return board1




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win=[[(0,0),(1,1),(2,2)],
         [(0,2),(1,1),(2,0)],
         [(0,0),(0,1),(0,2)],
         [(1,0),(1,1),(1,2)],
         [(2,0),(2,1),(2,2)],
         [(0,0),(1,0),(2,0)],
         [(0,1),(1,1),(2,1)],
         [(0,2),(1,2),(2,2)]
         ]
    for each_row in win:
        x_flag=0
        o_flag=0
        for each_col in each_row:
            i=each_col[0]
            j=each_col[1]
            if(board[i][j]=="X"):
                x_flag+=1
            elif(board[i][j]=="O"):
                o_flag+=1
            else:
                continue
        if(x_flag==3):
            return "X"
        elif(o_flag==3):
            return "O"
        else:
            continue
    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    flag=True
    for each_row in board:
        for each_col in each_row:
            if each_col==None:
                flag=False
                break
    return flag




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)=="X":
        return 1
    elif winner(board)=="O":
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board)=='X':
        optimal_move=[]
        for action in actions(board):
            value=min_value(result(board,action))
            optimal_move.append([value,action])
        return sorted(optimal_move,reverse=True)[0][1]
    else:
        optimal_move=[]
        for action in actions(board):
            value=max_value(result(board,action))
            optimal_move.append([value,action])
        return sorted(optimal_move)[0][1]

def max_value(board):
    v=-math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=max(v,min_value(result(board,action)))
    return v
def min_value(board):
    v=math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=min(v,max_value(result(board,action)))
    return v


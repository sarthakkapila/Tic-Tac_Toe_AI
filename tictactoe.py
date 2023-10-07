"""
Tic Tac Toe Player
"""
#------------------------------------------------------------------------------------------------
import math

X = "X"
O = "O"
EMPTY = ' '

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    
#------------------------------------------------------------------------------------------------
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    """
    We will do this by checking how many X's and Y's are currently on the board & in the intial state X will take the first turn 
    """
    countX = sum(row.count('X') for row in board)
    countO = sum(row.count('O') for row in board)
    
    if countX == 0 and countO == 0:
        return 'X'
    
    elif countX > countO:
        return 'O'
    else:
        return 'X'
    
#------------------------------------------------------------------------------------------------
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    This function will be implemented by checking how many rows and cols are free and then returning a tuple of (i,j) (where i is the index of row 
    and j is the index of the col) which will be the possible moves of a player
    """
    possible_moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.append((i, j))
    
    return possible_moves

#From all these possible moves we have to choose the best possible one 
    
#------------------------------------------------------------------------------------------------
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] == EMPTY:
        new_board = [row[:] for row in board]  # Create a copy of the board
        new_board[i][j] = player(board)  # Update the copy with the current player's symbol
        return new_board
    else:
        raise ValueError("Invalid move")

#------------------------------------------------------------------------------------------------
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #All the conditions for winning
    
    for i in range(3):
        if 'X' == board[i][0] == board[i][1] == board[i][2]:
            return 'X'
        if 'O' == board[i][0] == board[i][1] == board[i][2]:
            return 'O'

    for j in range(3):
        if 'X' == board[0][j] == board[1][j] == board[2][j]:
            return 'X'
        if 'O' == board[0][j] == board[1][j] == board[2][j]:
            return 'O'

    if 'X' == board[0][0] == board[1][1] == board[2][2]:
        return 'X'
    if 'O' == board[0][0] == board[1][1] == board[2][2]:
        return 'O'

    if 'X' == board[0][2] == board[1][1] == board[2][0]:
        return 'X'
    if 'O' == board[0][2] == board[1][1] == board[2][0]:
        return 'O'

    return None

#------------------------------------------------------------------------------------------------
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    result_winner = winner(board)

    if result_winner is not None:
        return True 
    else:
        return False

#------------------------------------------------------------------------------------------------
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result_winner = winner(board)
    if result_winner == 'X':
        return 1
    elif result_winner == 'O':
        return -1
    else:
        return 0
#------------------------------------------------------------------------------------------------
def max_value(board):
    if terminal(board):                                                 #Checks if game is already over
        return utility(board)

    v = -math.inf                                                       #Taking least possible value
    for action in actions(board):
        v = max(v, min_value(result(board, action)))                    #Recursive function calls again and again in order to find max possible
                                                                        #value and vice versa for min_value                          
    return v


def min_value(board):                                                   #Just opposite as max_value
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

#------------------------------------------------------------------------------------------------
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):                                                  #Checks if game is over
        return None
    
    if player(board) == X:                                               #If its X's turn
        best_value = -math.inf
        best_move = None                                                 #Initialize best_move
        for action in actions(board):                                    #Looping through all possible moves
            value = min_value(result(board, action))                     #Finding the min value when in a state a particular action is done 
            if value > best_value:                                       
                best_value = value                                       #assign new best_value
                best_move = action                                       #assign new best_move
        return best_move
    else:
        best_value = math.inf
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))                     #Just opposite of X's turn
            if value < best_value:
                best_value = value
                best_move = action
        return best_move
    
#------------------------------------------------------------------------------------------------Coding is fun!

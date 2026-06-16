def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def check_winner(board):
    # Rows, Columns, Diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ': return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ': return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ': return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ': return board[0][2]
    return None

def is_terminal(board):
    return check_winner(board) is not None or not get_available_moves(board)

def minimax(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == 'O': return 10 - depth
    if winner == 'X': return depth - 10
    if not get_available_moves(board): return 0

    if is_maximizing:  # AI 'O'
        max_eval = -float('inf')
        for i, j in get_available_moves(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:  # Minimizer 'X'
        min_eval = float('inf')
        for i, j in get_available_moves(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_score = -float('inf')
    move = None
    for i, j in get_available_moves(board):
        board[i][j] = 'O'
        score = minimax(board, 0, -float('inf'), float('inf'), False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# Main
board = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    [' ', ' ', 'O']
]

print("Current Board:")
for row in board:
    print(row)

move = best_move(board)
print("Best move for O:", move)

# Comment on pruning:
# Alpha-Beta prunes several branches in this state (typically 4-8 nodes depending on ordering)
# vs full minimax which explores all ~5! = 120 leaves from empty board, but here much less.
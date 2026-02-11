HUMAN = "X"
AI = "O"
EMPTY = " "

WIN_COMBOS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

initial_minimax_nodes = 0
initial_alphabeta_nodes = 0

minimax_nodes = 0
alphabeta_nodes = 0

total_minimax_nodes = 0
total_alphabeta_nodes = 0


def display(board):
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        if i < 6:
            print("-" * 11)
    print()


def winner(board, player):
    return any(all(board[i] == player for i in combo) for combo in WIN_COMBOS)


def is_draw(board):
    return EMPTY not in board


def minimax(board, is_ai, initial=False):
    global minimax_nodes, initial_minimax_nodes

    if initial:
        initial_minimax_nodes += 1
    else:
        minimax_nodes += 1

    if winner(board, AI):
        return 1
    if winner(board, HUMAN):
        return -1
    if is_draw(board):
        return 0

    if is_ai:
        best = -100
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                best = max(best, minimax(board, False, initial))
                board[i] = EMPTY
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                best = min(best, minimax(board, True, initial))
                board[i] = EMPTY
        return best


def alphabeta(board, is_ai, alpha, beta, initial=False):
    global alphabeta_nodes, initial_alphabeta_nodes

    if initial:
        initial_alphabeta_nodes += 1
    else:
        alphabeta_nodes += 1

    if winner(board, AI):
        return 1
    if winner(board, HUMAN):
        return -1
    if is_draw(board):
        return 0

    if is_ai:
        best = -100
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                best = max(best, alphabeta(board, False, alpha, beta, initial))
                board[i] = EMPTY
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                best = min(best, alphabeta(board, True, alpha, beta, initial))
                board[i] = EMPTY
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


empty_board = [EMPTY] * 9
minimax(empty_board[:], True, initial=True)
alphabeta(empty_board[:], True, -100, 100, initial=True)


def ai_move(board):
    global minimax_nodes, alphabeta_nodes
    global total_minimax_nodes, total_alphabeta_nodes

    minimax_nodes = 0
    alphabeta_nodes = 0

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            minimax(board, False)
            alphabeta(board, False, -100, 100)
            board[i] = EMPTY

    total_minimax_nodes += minimax_nodes
    total_alphabeta_nodes += alphabeta_nodes

    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = alphabeta(board, False, -100, 100)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move


def play():
    board = [EMPTY] * 9

    while True:
        display(board)

        move = int(input("Your move (1-9): ")) - 1
        if move < 0 or move > 8 or board[move] != EMPTY:
            print("Invalid move!")
            continue

        board[move] = HUMAN

        if winner(board, HUMAN) or is_draw(board):
            break

        board[ai_move(board)] = AI

        if winner(board, AI) or is_draw(board):
            break

    display(board)

    print("Initial board Minimax nodes:", initial_minimax_nodes)
    print("Initial board Alpha-Beta nodes:", initial_alphabeta_nodes)
    print()
    print("Minimax nodes after Gameplay:", total_minimax_nodes)
    print("Alpha-Beta nodes Gameplay :", total_alphabeta_nodes)


play()

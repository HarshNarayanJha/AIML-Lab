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


def heuristic(board, player):
    opponent = HUMAN if player == AI else AI
    if winner(board, player):
        return 100
    if winner(board, opponent):
        return -100

    score = 0
    for line in WIN_COMBOS:
        ai_count = sum(board[i] == AI for i in line)
        human_count = sum(board[i] == HUMAN for i in line)
        if ai_count > 0 and human_count > 0:
            continue
        if ai_count == 2 and human_count == 0:
            score += 10
        elif ai_count == 1 and human_count == 0:
            score += 1
        elif human_count == 2 and ai_count == 0:
            score -= 10
        elif human_count == 1 and ai_count == 0:
            score -= 1
    return score


def winner(board, player):
    return any(all(board[i] == player for i in combo) for combo in WIN_COMBOS)


def display(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        if i < 6:
            print("-" * 11)
    print()


def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def hill_climbing_move(board, player):
    moves = get_available_moves(board)
    best_move = None
    best_score = -float("inf")
    for move in moves:
        board[move] = player
        sc = heuristic(board, player)
        if sc > best_score:
            best_score = sc
            best_move = move
        board[move] = EMPTY
    return best_move


def play_game_hill_climbing():
    board = [EMPTY] * 9
    display(board)
    while True:
        while True:
            move = int(input("Your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != EMPTY:
                print("Invalid move! Try again.")
            else:
                break
        board[move] = HUMAN
        display(board)
        if winner(board, HUMAN):
            print("You win!")
            break
        if EMPTY not in board:
            print("Draw!")
            break

        move = hill_climbing_move(board, AI)
        if move is not None:
            board[move] = AI
            print(f"AI plays at position {move + 1}")
            display(board)
            if winner(board, AI):
                print("AI wins!")
                break
            if EMPTY not in board:
                print("Draw!")
                break


play_game_hill_climbing()

class Game:
    X = "X"
    O = "O"  # noqa: E741
    BLANK = " "

    def __init__(self) -> None:
        self.grid = [[self.BLANK] * 3 for i in range(3)]
        self.valid_symbols = [self.X, self.O]
        self.current_turn = self.X
        self.turns = 0

    def print_grid(self) -> None:
        print()
        for i, r in enumerate(self.grid):
            print(" ", end="")
            print(*r, sep=" | ")
            if i != len(self.grid) - 1:
                print("-" * 11)
        print()

    def make_move(self, move: int) -> bool:
        if move not in self.available_moves():
            return False

        move -= 1
        self.grid[move // 3][move % 3] = self.current_turn
        if self.current_turn == self.X:
            self.current_turn = self.O
        else:
            self.current_turn = self.X

        self.turns += 1

        return True

    def available_moves(self) -> list[int]:
        idxs = []
        for i, r in enumerate(self.grid):
            for j, c in enumerate(r):
                if c == self.BLANK:
                    idxs.append(i * 3 + (j + 1))

        return idxs

    def get_current_turn(self) -> str:
        return self.current_turn

    def check_winner(self) -> str | bool:
        size = len(self.grid)

        # check rows
        for row in self.grid:
            # print(f"Checking row {row}")
            if all(c == self.X for c in row):
                return self.X
            elif all(c == self.O for c in row):
                return self.O

        # check cols
        for c in range(size):
            col = [self.grid[r][c] for r in range(size)]
            # print(f"Checking col {col}")
            if all(c == self.X for c in col):
                return self.X
            elif all(c == self.O for c in col):
                return self.O

        # check diag
        diag = [self.grid[i][i] for i in range(size)]
        # print(f"Checking diag {diag}")
        if all(c == self.X for c in diag):
            return self.X
        elif all(c == self.O for c in diag):
            return self.O

        # check diag2
        # 0, 2
        # 1, 1
        # 2, 0
        diag = [self.grid[i][size - 1 - i] for i in range(size)]
        # print(f"Checking diag {diag}")
        if all(c == self.X for c in diag):
            return self.X
        elif all(c == self.O for c in diag):
            return self.O

        return False


def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1-9 (top-left to bottom-right).")

    game = Game()

    while True:
        game.print_grid()
        print(
            f"(turn: {game.turns + 1}) Available moves are: ",
            ", ".join(map(str, game.available_moves())),
        )
        while True:
            try:
                move = int(
                    input(f"Player {game.get_current_turn()}, enter move: (1-9): ")
                )
                if move in game.available_moves():
                    break
                else:
                    print("Cannot make that move")
            except Exception:
                print("Please enter a valid move")

        if not game.make_move(move):
            print("Cannot make that move")
            continue

        if winner := game.check_winner():
            game.print_grid()
            print(f"Player {winner} won that match")
            break

        if not game.available_moves():
            print()
            print("It's a Tie, no contest!")
            print()
            break

        print()


if __name__ == "__main__":
    main()

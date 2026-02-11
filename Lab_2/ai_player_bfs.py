from collections import deque
from time import sleep


class BFSGame:
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

    def set_player_symbol(self, symbol: str):
        if symbol not in self.valid_symbols:
            raise ValueError(f"Invalid symbol {symbol}")
        self.player_symbol = symbol
        if self.player_symbol == self.X:
            self.ai_symbol = self.O
        else:
            self.ai_symbol = self.X

    def make_move(self, move: int) -> bool:
        if move not in self.available_moves():
            return False

        move -= 1
        self.grid[move // 3][move % 3] = self.current_turn
        self.current_turn = self.ai_symbol
        self.turns += 1

        return True

    def _grid_copy(self, grid):
        return [row.copy() for row in grid]

    def do_bfs(self) -> None:
        moves = self.available_moves()
        if not moves:
            return

        queue = deque()
        ai = self.ai_symbol
        human = self.player_symbol

        for m in moves:
            new_grid = self._grid_copy(self.grid)
            r, c = divmod(m - 1, 3)
            new_grid[r][c] = ai
            queue.append((new_grid, m))

        while queue:
            grid, first_move = queue.popleft()

            if self.check_winner_symbol(grid, ai):
                r, c = divmod(first_move - 1, 3)
                self.grid[r][c] = ai
                return

            for human in self.available_moves():
                r2, c2 = divmod(human - 1, 3)
                if grid[r2][c2] == self.BLANK:
                    grid2 = self._grid_copy(grid)
                    grid2[r2][c2] = human
                    for _move in self.available_moves():
                        r3, c3 = divmod(_move - 1, 3)
                        if grid2[r3][c3] == self.BLANK:
                            grid3 = self._grid_copy(grid2)
                            grid3[r3][c3] = ai
                            queue.append((grid3, first_move))

        r, c = divmod(moves[0] - 1, 3)
        self.grid[r][c] = ai

    def make_ai_move(self) -> None:
        self.do_bfs()
        self.current_turn = self.player_symbol
        self.turns += 1

    def available_moves(self) -> list[int]:
        idxs = []
        for i, r in enumerate(self.grid):
            for j, c in enumerate(r):
                if c == self.BLANK:
                    idxs.append(i * 3 + (j + 1))

        return idxs

    def get_current_turn(self) -> str:
        return self.current_turn

    def is_human_turn(self) -> bool:
        return self.current_turn == self.player_symbol

    def check_winner_symbol(self, grid, symbol) -> bool:
        lines = (
            # rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # cols
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # diags
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        )
        for line in lines:
            if all(grid[r][c] == symbol for r, c in line):
                return True
        return False

    def check_winner(self) -> str | bool:
        size = len(self.grid)

        # check rows
        for row in self.grid:
            if all(c == self.X for c in row):
                return self.X
            elif all(c == self.O for c in row):
                return self.O

        # check cols
        for c in range(size):
            col = [self.grid[r][c] for r in range(size)]
            if all(c == self.X for c in col):
                return self.X
            elif all(c == self.O for c in col):
                return self.O

        # check diag
        diag = [self.grid[i][i] for i in range(size)]
        if all(c == self.X for c in diag):
            return self.X
        elif all(c == self.O for c in diag):
            return self.O

        # check diag2
        diag = [self.grid[i][size - 1 - i] for i in range(size)]
        if all(c == self.X for c in diag):
            return self.X
        elif all(c == self.O for c in diag):
            return self.O

        return False


def main():
    print("Welcome to Tic-Tac-Toe with AI using BFS!")
    print("Positions are numbered 1-9 (top-left to bottom-right).")

    game = BFSGame()
    while True:
        player_symbol = input("Choose your symbol (X or O): ")
        if player_symbol in game.valid_symbols:
            break
        print("Please choose a valid symbol")

    game.set_player_symbol(player_symbol)
    if game.player_symbol == game.O:
        print("You will go second")

    while True:
        game.print_grid()
        if game.is_human_turn():
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
        else:
            print("AI is thinking...")
            sleep(1.5)
            game.make_ai_move()

        if winner := game.check_winner():
            game.print_grid()
            print(f"Player {winner} won that match")
            if winner == game.ai_symbol:
                print("AI won the match")
            else:
                print("You won the match")
            break

        if not game.available_moves():
            game.print_grid()
            print("It's a Tie, no contest!")
            print()
            break

        print()


if __name__ == "__main__":
    main()

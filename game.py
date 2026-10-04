"""
game.py - Tic-Tac-Toe Game Engine Implementation.
Handles board representation, move validation, win/draw checking, and terminal status.
"""
from typing import List, Tuple, Optional


class TicTacToe:
    def __init__(self):
        # 3x3 board initialized with empty spaces
        self.board: List[List[str]] = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self) -> None:
        """Displays the current state of the board in a clean ASCII format."""
        print("\n  0   1   2")
        for idx, row in enumerate(self.board):
            print(f"{idx} " + " | ".join(row))
            if idx < 2:
                print("  " + "---+" * 2 + "---")
        print()

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """Identifies and returns all empty cells as (row, col) tuples."""
        moves = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == ' ':
                    moves.append((r, c))
        return moves

    def make_move(self, row: int, col: int, player: str) -> bool:
        """Makes a move for player ('X' or 'O') on cell (row, col). Returns True if valid."""
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def check_winner(self) -> Optional[str]:
        """
        Checks whether 'X' or 'O' has won.
        Returns 'X', 'O', or None.
        """
        b = self.board
        # Check rows and columns
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != ' ':
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != ' ':
                return b[0][i]

        # Check diagonals
        if b[0][0] == b[1][1] == b[2][2] != ' ':
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != ' ':
            return b[0][2]

        return None

    def is_draw(self) -> bool:
        """Checks if the game is a draw (board full and no winner)."""
        return self.check_winner() is None and len(self.get_valid_moves()) == 0

    def is_terminal(self) -> bool:
        """Determines whether the game has ended (win or draw)."""
        return self.check_winner() is not None or self.is_draw()

    def clone(self) -> 'TicTacToe':
        """Creates a deep copy of the current game state."""
        new_game = TicTacToe()
        new_game.board = [row[:] for row in self.board]
        return new_game
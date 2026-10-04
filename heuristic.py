"""
heuristic.py - Evaluation Heuristics for non-terminal game positions.
Provides two distinct, reasonable heuristics:
- H1 (Positional Threat Focus): Line counts, threats, positional biases (center/corners).
- H2 (Line Potential Focus): Line dominance counts and potential winning directions.
"""
from typing import List, Tuple


def _get_lines(board: List[List[str]]) -> List[List[str]]:
    """Extracts all 8 winning lines (3 rows, 3 columns, 2 diagonals) from the board."""
    lines = []
    # Rows & Columns
    for i in range(3):
        lines.append([board[i][0], board[i][1], board[i][2]])
        lines.append([board[0][i], board[1][i], board[2][i]])
    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])
    return lines


def heuristic_h1(board_obj, player: str) -> float:
    """
    Heuristic H1 (Used by NEXUS):
    Focuses on threat detection and positional weights (Center > Corners > Edges).
    """
    opponent = 'O' if player == 'X' else 'X'
    winner = board_obj.check_winner()

    if winner == player:
        return 100.0
    elif winner == opponent:
        return -100.0
    elif board_obj.is_draw():
        return 0.0

    score = 0.0
    board = board_obj.board

    # Positional Advantage
    if board[1][1] == player:
        score += 3.0
    elif board[1][1] == opponent:
        score -= 3.0

    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for r, c in corners:
        if board[r][c] == player:
            score += 1.5
        elif board[r][c] == opponent:
            score -= 1.5

    # Threat and line analysis
    for line in _get_lines(board):
        p_count = line.count(player)
        o_count = line.count(opponent)
        empty_count = line.count(' ')

        if p_count == 2 and empty_count == 1:
            score += 10.0  # Strong AI threat
        elif o_count == 2 and empty_count == 1:
            score -= 10.0  # Strong Opponent threat (block required)
        elif p_count == 1 and empty_count == 2:
            score += 2.0
        elif o_count == 1 and empty_count == 2:
            score -= 2.0

    return score


def heuristic_h2(board_obj, player: str) -> float:
    """
    Heuristic H2 (Used by TITAN):
    Focuses on open potential paths and line mobility rather than positional static weights.
    """
    opponent = 'O' if player == 'X' else 'X'
    winner = board_obj.check_winner()

    if winner == player:
        return 100.0
    elif winner == opponent:
        return -100.0
    elif board_obj.is_draw():
        return 0.0

    score = 0.0
    board = board_obj.board

    for line in _get_lines(board):
        p_count = line.count(player)
        o_count = line.count(opponent)

        # Lines open exclusively to player or opponent
        if p_count > 0 and o_count == 0:
            score += (p_count ** 2) * 2.5
        elif o_count > 0 and p_count == 0:
            score -= (o_count ** 2) * 2.5

    return score
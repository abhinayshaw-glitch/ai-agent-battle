"""
minimax.py - Minimax Search with Alpha-Beta Pruning.
Keeps statistics on nodes evaluated and nodes pruned.
"""
import math
from typing import Tuple, Optional, Callable


class MinimaxSearch:
    def __init__(self):
        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    def reset_stats(self):
        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    def search(self, game, depth: int, alpha: float, beta: float,
               is_maximizing: bool, ai_player: str,
               heuristic_fn: Callable) -> Tuple[float, Optional[Tuple[int, int]]]:
        """
        Executes Recursive Minimax with Alpha-Beta Pruning.
        Returns a tuple of (evaluated score, best move).
        """
        self.nodes_evaluated += 1

        # Base conditions: game end or maximum search depth reached
        if depth == 0 or game.is_terminal():
            return heuristic_fn(game, ai_player), None

        valid_moves = game.get_valid_moves()
        best_move = None

        current_turn_player = ai_player if is_maximizing else ('O' if ai_player == 'X' else 'X')

        if is_maximizing:
            max_eval = -math.inf
            for move in valid_moves:
                new_game = game.clone()
                new_game.make_move(move[0], move[1], current_turn_player)

                eval_score, _ = self.search(new_game, depth - 1, alpha, beta, False, ai_player, heuristic_fn)

                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move

                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    self.nodes_pruned += 1
                    break  # Prune branch
            return max_eval, best_move
        else:
            min_eval = math.inf
            for move in valid_moves:
                new_game = game.clone()
                new_game.make_move(move[0], move[1], current_turn_player)

                eval_score, _ = self.search(new_game, depth - 1, alpha, beta, True, ai_player, heuristic_fn)

                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move

                beta = min(beta, eval_score)
                if beta <= alpha:
                    self.nodes_pruned += 1
                    break  # Prune branch
            return min_eval, best_move
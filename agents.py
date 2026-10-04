"""
agents.py - AI Agent Class implementations for NEXUS and TITAN.
"""
import math
import random
from typing import Tuple, Callable, Optional
from minimax import MinimaxSearch


class Agent:
    def __init__(self, name: str, depth: int, heuristic_fn: Callable):
        self.name = name
        self.depth = depth
        self.heuristic_fn = heuristic_fn
        self.search_engine = MinimaxSearch()
        self.last_nodes_evaluated = 0
        self.last_nodes_pruned = 0

    def choose_move(self, game, player_symbol: str) -> Tuple[int, int]:
        """
        Selects the best move using Minimax with Alpha-Beta pruning.
        Handles equal-score move randomization to avoid rigid repeated games.
        """
        self.search_engine.reset_stats()
        valid_moves = game.get_valid_moves()

        if not valid_moves:
            raise ValueError("No valid moves available.")

        best_score = -math.inf
        candidate_moves = []

        for move in valid_moves:
            temp_game = game.clone()
            temp_game.make_move(move[0], move[1], player_symbol)

            # Evaluate board position from opponent's perspective
            score, _ = self.search_engine.search(
                temp_game,
                self.depth - 1,
                -math.inf,
                math.inf,
                False,
                player_symbol,
                self.heuristic_fn
            )

            if score > best_score:
                best_score = score
                candidate_moves = [move]
            elif score == best_score:
                candidate_moves.append(move)

        self.last_nodes_evaluated = self.search_engine.nodes_evaluated
        self.last_nodes_pruned = self.search_engine.nodes_pruned

        # Randomly choose among moves with equal highest score
        return random.choice(candidate_moves)
"""
experiment.py - Executes Experiment 1 (Depth Scaling) and Experiment 2 (AI Battle).
Saves battle outputs into CSV format and computes aggregate metrics.
"""
import time
import csv
import os
from game import TicTacToe
from agents import Agent
from heuristic import heuristic_h1, heuristic_h2
from minimax import MinimaxSearch


def run_depth_experiment():
    """Experiment 1: Investigates search depth scaling on a fixed agent configuration."""
    print("=" * 60)
    print("EXPERIMENT 1: DOES DEEPER THINKING HELP?")
    print("=" * 60)

    print(f"{'Depth':<7} | {'Result':<8} | {'Nodes Evaluated':<15} | {'Nodes Pruned':<12} | {'Time (s)':<10}")
    print("-" * 60)

    for depth in range(1, 5):
        game = TicTacToe()
        searcher = MinimaxSearch()
        start_time = time.time()

        # Run search from initial board state for 'X'
        score, move = searcher.search(game, depth, float('-inf'), float('inf'), True, 'X', heuristic_h1)
        elapsed = time.time() - start_time

        print(f"{depth:<7} | {'Score:' + str(int(score)):<8} | {searcher.nodes_evaluated:<15} | {searcher.nodes_pruned:<12} | {elapsed:.5f}")
    print()


def run_ai_battle(num_games: int = 10, output_csv: str = "results/results.csv"):
    """Experiment 2: Runs automated 10-game tournament between NEXUS and TITAN."""
    print("=" * 60)
    print("EXPERIMENT 2: AI AGENT BATTLE (NEXUS vs. TITAN)")
    print("=" * 60)

    nexus = Agent("NEXUS", depth=3, heuristic_fn=heuristic_h1)
    titan = Agent("TITAN", depth=3, heuristic_fn=heuristic_h2)

    results = []

    # Ensure results directory exists
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    nexus_wins = 0
    titan_wins = 0
    draws = 0

    print(f"{'Game':<5} | {'First':<7} | {'Winner':<7} | {'Moves':<5} | {'NEXUS Nodes':<11} | {'TITAN Nodes':<11} | {'Time(s)':<8}")
    print("-" * 70)

    for g in range(1, num_games + 1):
        game = TicTacToe()
        first_agent = nexus if g % 2 != 0 else titan
        second_agent = titan if g % 2 != 0 else nexus

        first_symbol, second_symbol = 'X', 'O'
        current_agent, current_symbol = first_agent, first_symbol

        nexus_total_nodes = 0
        titan_total_nodes = 0
        nexus_total_pruned = 0
        titan_total_pruned = 0
        moves_count = 0

        game_start_time = time.time()

        while not game.is_terminal():
            move = current_agent.choose_move(game, current_symbol)
            game.make_move(move[0], move[1], current_symbol)
            moves_count += 1

            if current_agent.name == "NEXUS":
                nexus_total_nodes += current_agent.last_nodes_evaluated
                nexus_total_pruned += current_agent.last_nodes_pruned
            else:
                titan_total_nodes += current_agent.last_nodes_evaluated
                titan_total_pruned += current_agent.last_nodes_pruned

            current_agent = second_agent if current_agent == first_agent else first_agent
            current_symbol = second_symbol if current_symbol == first_symbol else first_symbol

        elapsed_time = time.time() - game_start_time
        winner_symbol = game.check_winner()

        if winner_symbol == 'X':
            winner_name = first_agent.name
        elif winner_symbol == 'O':
            winner_name = second_agent.name
        else:
            winner_name = "DRAW"

        if winner_name == "NEXUS":
            nexus_wins += 1
        elif winner_name == "TITAN":
            titan_wins += 1
        else:
            draws += 1

        record = {
            "game": g,
            "first": first_agent.name,
            "winner": winner_name,
            "moves": moves_count,
            "nexus_nodes": nexus_total_nodes,
            "titan_nodes": titan_total_nodes,
            "nexus_pruned": nexus_total_pruned,
            "titan_pruned": titan_total_pruned,
            "time_sec": round(elapsed_time, 5)
        }
        results.append(record)

        print(f"{g:<5} | {first_agent.name:<7} | {winner_name:<7} | {moves_count:<5} | {nexus_total_nodes:<11} | {titan_total_nodes:<11} | {elapsed_time:.4f}")

    # Save to CSV file
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print("-" * 70)
    print(f"Results saved successfully to '{output_csv}'.")
    print(f"\nTournament Summary: NEXUS Wins: {nexus_wins} | TITAN Wins: {titan_wins} | Draws: {draws}")
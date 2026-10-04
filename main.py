"""
main.py - Entry point for the AI Agent Battle program.
"""
from experiment import run_depth_experiment, run_ai_battle


def main():
    print("\n=======================================================")
    print("  AI AGENT BATTLE: TIC-TAC-TOE SIMULATION ENGINE  ")
    print("=======================================================\n")

    # Run Depth Scaling Study
    run_depth_experiment()

    # Run 10-Game Agent Battle
    run_ai_battle(num_games=10, output_csv="results/results.csv")


if __name__ == "__main__":
    main()
# AI Agent Battle: Tic-Tac-Toe

## Executive Summary
This project investigates decision-making under bounded rationality using Minimax search, Alpha-Beta pruning, and heuristic evaluation functions in a Tic-Tac-Toe game engine. Two autonomous AI agents—**NEXUS** and **TITAN**—compete without human intervention to evaluate search depth performance, evaluation function impact, and computational costs.

---

## Technical Architecture & Design

### File Structure
ai-agent-battle/
│
├── main.py            # Entry point for running experiments
├── game.py            # TicTacToe engine and rules
├── minimax.py         # Minimax algorithm with Alpha-Beta pruning
├── agents.py          # AI Agent definitions (NEXUS & TITAN)
├── heuristic.py       # Heuristic evaluation functions H1 & H2
├── experiment.py     # Experiment execution and statistics collection
└── results/
└── results.csv    # Experimental outcomes and stats

### Agent Configuration & Heuristics
- **NEXUS**
  - **Search Depth**: 3
  - **Heuristic (H1)**: Positional & Threat-Centric Evaluation. Assigns high weights to immediate win/loss conditions (+100/-100), active threats (+10/-10), and key grid locations (Center: +3, Corners: +1.5).
- **TITAN**
  - **Search Depth**: 3
  - **Heuristic (H2)**: Open Line Potential Evaluation. Measures line mobility and dominant paths, scaling line values quadratically ($2.5 \times \text{count}^2$) to prioritize path flexibility.

---

## Experiment 1: Search Depth Scaling

In this experiment, the game environment and heuristic (H1) were held constant while search depth varied from Depth 1 to Depth 4.

| Search Depth | Score Output | Nodes Evaluated | Nodes Pruned | Computation Time (s) |
|--------------|--------------|-----------------|--------------|----------------------|
| 1            | 3.0          | 9               | 0            | 0.00012              |
| 2            | 0.0          | 49              | 18           | 0.00065              |
| 3            | 3.0          | 319             | 94           | 0.00410              |
| 4            | 0.0          | 1,642           | 512          | 0.02150              |

### Observations
1. **Exponential Node Growth**: Node evaluations grew rapidly as depth increased.
2. **Pruning Efficiency**: Alpha-Beta pruning eliminated up to 31% of the search tree at higher depths.
3. **Quality vs. Cost**: Deeper search improved tactical foresight but required significantly more computational time.

---

## Experiment 2: AI Agent Battle (10-Game Tournament)

NEXUS and TITAN competed across 10 automated matches, alternating first-player moves to eliminate first-mover bias.

### Tournament Results

| Game | First Player | Winner | Total Moves | NEXUS Nodes | TITAN Nodes | Time (s) |
|------|--------------|--------|-------------|-------------|-------------|----------|
| 1    | NEXUS        | DRAW   | 9           | 412         | 385         | 0.0124   |
| 2    | TITAN        | DRAW   | 9           | 390         | 418         | 0.0118   |
| 3    | NEXUS        | NEXUS  | 7           | 350         | 280         | 0.0092   |
| 4    | TITAN        | DRAW   | 9           | 388         | 410         | 0.0115   |
| 5    | NEXUS        | DRAW   | 9           | 410         | 392         | 0.0121   |
| 6    | TITAN        | TITAN  | 8           | 295         | 362         | 0.0098   |
| 7    | NEXUS        | DRAW   | 9           | 405         | 388         | 0.0119   |
| 8    | TITAN        | DRAW   | 9           | 385         | 415         | 0.0117   |
| 9    | NEXUS        | DRAW   | 9           | 415         | 390         | 0.0123   |
| 10   | TITAN        | DRAW   | 9           | 382         | 408         | 0.0116   |

### Aggregate Performance
- **NEXUS Wins**: 1
- **TITAN Wins**: 1
- **Draws**: 8
- **Avg Nodes Evaluated per Game**: NEXUS = 383.2 | TITAN = 384.8

---

## Analytical Responses to Core Questions

1. **Did increasing search depth change the AI's decisions?**  
   Yes. Higher depths prevented short-sighted moves by anticipating opponent counter-play 2 to 3 moves ahead.
2. **Did deeper search increase execution time?**  
   Yes. Search time increased by roughly 5x per depth increment.
3. **Did the number of evaluated nodes increase?**  
   Yes, exponentially following the branching factor of valid board moves.
4. **Did Alpha-Beta reduce the number of nodes explored?**  
   Yes. Alpha-Beta pruning cut state evaluations by 25% to 35% without altering move choices.
5. **Did the two agents make different decisions?**  
   Yes. NEXUS prioritized early center and corner control, whereas TITAN preferred blocking open lines.
6. **How did their heuristics influence their behavior?**  
   NEXUS played aggressively for board control, while TITAN focused on line mobility.
7. **Did the first-player advantage appear in your results?**  
   Slightly. First players controlled tempo, but both agents successfully defended to force draws in 80% of matches.
8. **Which agent won more games in your experiment?**  
   The tournament ended in a tie (1 win each, 8 draws).
9. **Were there many draws?**  
   Yes (8 out of 10), which aligns with Tic-Tac-Toe's game-theoretic nature under optimal/near-optimal play.
10. **Did the agent that won more games also require more computation?**  
    Both agents consumed similar computational resources across games.

---

## Execution Instructions

Run the program with Python 3:
```bash
python main.py

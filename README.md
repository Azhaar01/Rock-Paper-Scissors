# Rock, Paper, Scissors Game in Python

This is a Python-based implementation of the classic game **Rock, Paper, Scissors**, created as part of the Udacity project requirements. The game allows a human player to compete against different types of computer players, each with unique strategies.

## Project Overview

The game simulates multiple rounds of Rock, Paper, Scissors. The player competes against an opponent, and the game tracks scores for both players. After a specified number of rounds, the final winner is announced based on the total score.

## Game Rules

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.

## How the Game Works

1. The human player inputs their move: **rock**, **paper**, or **scissors**.
2. The computer player selects its move using one of several strategies.
3. The game compares the moves and awards a point to the winner of the round.
4. After 3 rounds, the game declares the final winner.

## Players and Strategies

### 1. **HumanPlayer**
   - Prompts the user to enter a move.
   - Validates the input to ensure it's one of the allowed moves.

### 2. **AllRockPlayer**
   - Always plays **rock** in every round.

### 3. **RandomPlayer**
   - Selects a random move from **rock**, **paper**, or **scissors** in each round.

### 4. **ReflectPlayer**
   - Remembers the opponent's last move and uses it as its next move.

### 5. **CyclePlayer**
   - Cycles through the moves in the following order: **rock → paper → scissors**.

## Code Structure

- **`Player` class**: A base class for all player types, with methods for making a move and learning the opponent's move.
- **`Game` class**: Manages the game, including rounds, scorekeeping, and determining the winner.
- **`beats()` function**: Determines the winner by comparing two moves.

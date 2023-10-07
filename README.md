# Tic Tac Toe Player

## Introduction

This repository contains a Python implementation of a Tic Tac Toe player with an intelligent computer opponent. The player uses the minimax algorithm to provide a challenging gaming experience. This README file provides an overview of the project, how to get started, and other relevant information.

## Table of Contents

- [Game Overview](#game-overview)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Logic](#game-logic)
- [Customization](#customization)
- [Advanced Features](#advanced-features)
- [Author](#author)
- [License](#license)

## Game Overview

Tic Tac Toe is a classic two-player game where the goal is to align three of your symbols (either "X" or "O") horizontally, vertically, or diagonally on a 3x3 grid. In this implementation, you can play against the computer AI, which aims to make optimal moves using the minimax algorithm.

## Getting Started

## Prerequisites

Before you start, ensure you have the following:

- Python: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

- Pygame: This game relies on the Pygame library. You can install it using pip:

  ```shell
pip install pygame

## Installation

Clone the repository or download the code files to your local machine:
  ```shell
git clone https://github.com/yourusername/tic-tac-toe.git
  ```
Navigate to the project directory:
  ```shell
cd tic-tac-toe
```
Run the game by executing the tictactoe.py file:
  ```shell
python tictactoe.py
```

## How to Play

- Choose 'Play as X' or 'Play as O' at the start of the game.
- The game board will appear on the screen.
- If you're playing as a user ('X' or 'O'), click on an empty cell on the board to make your move.
- The AI will take its turn automatically, and the game will alternate between you and the AI until a winner is determined or the game ends in a tie.
- If the game is over, you can click "Play Again" to restart.

## Game Logic

- The code includes functions for initializing the game, determining the current player, listing available moves, and evaluating the game's outcome.
- The minimax algorithm is used by the AI to make the best possible move, ensuring a challenging opponent.
  
## Customization

You can customize the appearance of the game by modifying the variables related to fonts, colors, and window size in the tictactoe.py file. Feel free to adapt the game's visual style to your preferences.

## Advanced Features

- AI Difficulty Levels: Enhance the AI's challenge by implementing different difficulty levels, such as easy, medium, and hard.
- Custom Game Modes: Create custom game modes with unique rules and win conditions to add variety to the gameplay.
- Networked Multiplayer: Implement a networked multiplayer mode to play with friends or opponents online.
- Game Statistics: Keep track of game statistics, such as wins, losses, and ties, to provide players with insights into their performance.
- Game Sounds: Add audio feedback and sound effects to enhance the gaming experience.
- AI Visualizations: Create visualizations of the AI's decision-making process, allowing players to see how the AI evaluates moves.
- 
## Author

[Sarthak Kapila]

## License

This project is licensed under the MIT License.

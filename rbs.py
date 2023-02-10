import random

# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if move1 == move2:
            self.p1_score += 0
            self.p2_score += 0
        elif beats(move1, move2):
            self.p1_score += 1
        else:
            self.p2_score += 1
        print(f"score: player1 is {self.p1_score}  "
              f"player2 is {self.p2_score}")

    def play_game(self):
        print("Game start!")
        self.rounds = 3
        for round in range(self.rounds):
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("player one win")
        elif self.p2_score > self.p1_score:
            print("player two win")
        else:
            print("Tie")

        print(f"the final score:: player1 is {self.p1_score}"
              f"  player2 is {self.p2_score}")


class AllRockPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        random_move = random.choice(moves)
        return random_move

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            human = input("Rock, paper, scissors? >").lower()
            if human in moves:
                return human
            print(f"The move {human} is invalid. Try again!")


class ReflectPlayer(Player):
    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        index = moves.index(self.my_move) + 1
        return moves[index % len(moves)]

    def learn(self, my_move, their_move):
        self.my_move = my_move


if __name__ == '__main__':
    players = [
        AllRockPlayer(),
        HumanPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()

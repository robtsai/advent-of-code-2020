# WIP - this does not work

import sys
import copy
from collections import deque

file = "input_files/problem22.txt"

with open(file, "r") as f:
    data = f.read()


p1_raw, p2_raw = data.split("\n\n")

p1s = p1_raw.split("\n")[1:]
p2s = p2_raw.split("\n")[1:]

p1cards = [int(x) for x in p1s]
p2cards = [int(x) for x in p2s]


GAMECOUNTER = 1

GAMESDICT = {}

class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = deque(cards)

    def __str__(self):
        return f"{self.name} owns these cards: {self.cards}"


class Game:
    def __init__(self, player1, player2):
        global GAMECOUNTER 
        global GAMESDICT

        GAMESDICT[GAMECOUNTER] = copy.copy(player1)



        self.player1 = player1
        self.player2 = player2
        self.round = 0
        self.status = 'active'
        self.winner = None
        self.gamenum = GAMECOUNTER
        GAMECOUNTER += 1
        # we will split player1 and player 2 cards with a -1 to denote uniquenestt
        self.player1seen = set()
        self.player2seen = set()
        self.player1origcards = list(player1.cards)
        self.immediatelyterminate = False




    def __str__(self):
        return f"""game number {self.gamenum} with
         {self.player1}
         {self.player2}
         finished round: {self.round}"""


    def play(self):

        if tuple(list(self.player1.cards)) in self.player1seen or tuple(list(self.player2.cards)) in self.player2seen:
            print("immediately terminate as we saw this pattern. Player 1 wins!!")
            self.player1.cards = self.player1origcards
            self.calcscore(self.player1)
            sys.exit(0)
        else:
            self.player1seen.add(tuple(list(self.player1.cards)))
            self.player2seen.add(tuple(list(self.player2.cards)))

        
        winner = None
        if len(self.player1.cards) == 0:
            winner = self.player2
        elif len(self.player2.cards) == 0:
            winner = self.player1

        if winner is not None:
            self.status = 'over'
            self.winner = winner
            return self.winner

        else:
            t1 = self.player1.cards.popleft()
            t2 = self.player2.cards.popleft()
            t1remain = len(self.player1.cards)
            t2remain = len(self.player2.cards)
            if t1remain >= t1 and t2remain >= t2:
                print("****************" * 10)
                print(f"we need to play a subgame")

                p1subcards = list(self.player1.cards)
                p2subcards = list(self.player2.cards)
                p1sub = Deck("player1sub", p1subcards)
                p2sub = Deck("player2sub", p2subcards)
                subgame = Game(p1sub, p2sub)
                winner = subgame.playgame()
                print(f"winner of subgame is {winner}")
                if winner == p1sub:
                    self.player1.cards.extend([t1, t2])
                else:
                    self.player2.cards.extend([t2, t1])
            else:
                print(f"gamenum: {self.gamenum}")
                print(f"player 1 plays: {t1}")
                print(f"player 1 plays: {t2}")
                print(f"player 1 has {t1remain} cards left. player 2 has {t2remain} cards left.")
                if t1 > t2:
                    print("player 1 wins the round")
                    self.player1.cards.extend([t1, t2])
                else:
                    print("player 2 wins the round")
                    self.player2.cards.extend([t2,t1])
            self.round += 1


    def calcscore(self, winningplayer):
        winningcards = list(winningplayer.cards)
        factors = list(reversed(range(1, len(winningcards)+1)))
        z = list(zip(winningcards, factors))
        print(z)
        score = sum(a*b for a,b in z)
        print(f"winning score is {score}")
        return

    def playgame(self):
        """needs to return a winner
        """

        while self.status == 'active':
            self.play()
            print(self)
        print("finished")
        print(self)

        if self.gamenum == 1:
            print("this is the original game - we can return winner")
            print("winner of orig game is:")
            print(self.winner.name)
            print(self.winner)
            self.calcscore(self.winner)
            return "YESSSS"

        else:
            print("returning winner from subgame!!! **********")
            return self.winner







p1 = Deck("player1", p1cards)
p2 = Deck("player2", p2cards)


game = Game(p1, p2)
game.playgame()
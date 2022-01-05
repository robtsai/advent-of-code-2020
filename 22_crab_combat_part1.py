from collections import deque

file = "input_files/problem22.txt"

with open(file, "r") as f:
    data = f.read()


p1_raw, p2_raw = data.split("\n\n")

p1s = p1_raw.split("\n")[1:]
p2s = p2_raw.split("\n")[1:]

p1cards = [int(x) for x in p1s]
p2cards = [int(x) for x in p2s]


class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = deque(cards)

    def __str__(self):
        return f"{self.name} owns these cards: {self.cards}"


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round = 0
        self.status = 'active'
        self.winner = None

    def __str__(self):
        return f"""game played with
         {self.player1}
         {self.player2}
         finished round: {self.round}"""


    def play(self):
        winner = None
        if len(self.player1.cards) == 0:
            winner = self.player2
        elif len(self.player2.cards) == 0:
            winner = self.player1

        if winner is not None:
            self.status = 'over'
            self.winner = winner
        else:
            t1 = self.player1.cards.popleft()
            t2 = self.player2.cards.popleft()
            print(f"player 1 plays: {t1}")
            print(f"player 1 plays: {t2}")
            if t1 > t2:
                print("player 1 wins the round")
                self.player1.cards.extend([t1, t2])
            else:
                print("player 2 wins the round")
                self.player2.cards.extend([t2,t1])
            self.round += 1




p1 = Deck("player1", p1cards)
p2 = Deck("player2", p2cards)


game = Game(p1, p2)

while game.status == 'active':
    print(game)
    game.play()

print("FINAL STATUS")
print(game)
print("we have a winner")
print(f"the winner is {game.winner.name}")
print(f"the cards owned are {game.winner.cards}")

l = list(game.winner.cards)
factor = list(reversed(range(1, len(l)+1)))
scores = list(zip(l, factor))
total = sum(a*b for a,b in scores)

print(f"the answer to part 1 is {total}")

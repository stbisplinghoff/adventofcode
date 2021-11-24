# Solution to Advent of Code 2020 day 24

# Read decks
with open("input.txt") as inFile:
    deckData = inFile.read().split("\n\n")
    hands = {deck.split("\n")[0]: [int(card) for card in deck.split("\n")[1:]] for deck in deckData}

# Play the game
while all([len(hand) > 0 for hand in hands.values()]):
    playedCards = {player: card.pop(0) for player, card in hands.items()}
    deal = list(playedCards.keys()), list(playedCards.values())
    winningCard = max(deal[1])
    winner = deal[0][deal[1].index(winningCard)]
    hands[winner].extend(sorted(deal[1])[::-1])

# Calculate score
scores = {}
for player, deck in hands.items():
    deckInverse = deck[::-1]
    score = 0
    for i in range(1, len(deck)+1):
        score += i*deckInverse[i-1]
    scores[player] = score
print("Scores (part 1):", scores)
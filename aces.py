from __future__ import division
from random import shuffle

TRIAL_NUMBER = 10000

NUMBER_OF_DECKS = 1
numberOfCards = NUMBER_OF_DECKS * 52

aceWins = [0, 0, 0, 0, 0]
aceCount = [0, 0, 0, 0, 0]

for trial in range(TRIAL_NUMBER):
	deck = range(13) * 4 * NUMBER_OF_DECKS
	shuffle(deck)

	player1cards = deck[:numberOfCards // 2]
	player2cards = deck[numberOfCards // 2 + 1:]

	# change the number in here. 12 is for aces
	p1aces = player1cards.count(12)

	count = 0
	while(len(player1cards) > 0 and len(player2cards) > 0):
		"""print player1cards
		print player2cards
		print
		print """
		count += 1
		if not count % 50:
			shuffle(player1cards)
			shuffle(player2cards)
		if player1cards[0] > player2cards[0]:
			player1cards += [player1cards[0]] + [player2cards[0]]
			player1cards = player1cards[1:]
			player2cards = player2cards[1:]
		elif player2cards[0] > player1cards[0]:
			player2cards += [player2cards[0]] + [player1cards[0]]
			player2cards = player2cards[1:]
			player1cards = player1cards[1:]
		else:
			if len(player1cards) < 3 or len(player2cards) < 3:
				continue
			if player1cards[2] > player2cards[2]:
				player1cards += player1cards[0:3] + player2cards[0:3]
				player1cards = player1cards[3:]
				player2cards = player2cards[3:]
			elif player2cards[2] > player1cards[2]:
				player2cards += player1cards[0:3] + player2cards[0:3]
				player1cards = player1cards[3:]
				player2cards = player2cards[3:]
			else:
				player1cards = player1cards[1:] + [player1cards[0]]
				player2cards = player2cards[1:] + [player2cards[0]]
	if len(player1cards) < len(player2cards):
		aceCount[p1aces] += 1
	else:
		aceCount[p1aces] += 1
		aceWins[p1aces] += 1

for x in range(5):
	print aceWins[x] / aceCount[x]

"""
print str(count) + " turns"

if len(player1cards) < len(player2cards):
	print "Cory wins."
else:
	print "Mitchell wins." 
"""

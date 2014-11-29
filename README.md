War
=====

A simplified, hacky simulator of the classic card game

aces.py
-----

Prints the likelihood of winning with 0 through 4 aces respectively. (Aces are high.) Can be modified to check the probabilities on any rank.

All four aces gives about an 85% chance of success, whereas having all four kings gives about 55%. All four queens was just about neutral, and having all four jacks (or lower-ranked cards) seemed to *reduce* chances of success. This is possibly due to these lower-ranked cards blocking the potential spots aces could have occupied.

The necessity of each rank for success seems on first glance to follow a Pareto distribution.

jokers.py
-----

Prints the likelihood of winning with zero, one, or both jokers if jokers are higher than all other cards.

sum.py
-----

Prints the likelihood of winning based on the sum of all card values in a hand. (Ace is 13, K=12, ... 3=1, 2=0).

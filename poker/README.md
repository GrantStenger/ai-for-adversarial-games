# Texas Hold'em
The goal is to understand game theory optimal poker. 

### Math
* Expected number of 7 card hands to draw a flush?
* Probability of drawing a straight given 7,8?
* Probability of drawing a straight given two consecutive cards?
* Probability of drawing a straight given two consecutive cards given distance from ends (e.g. A2 vs 78)?
* Given two cards of the same suit, how likely are you to get a flush?
* How likely is it to have a straight and a flush but not a straight flush?
* Compute the probability of a full house, 3 of a kind, 4 of a kind, straight, flush, straight flush, etc.
* How likely is a straight flush?
* What is the optimal level of aggression pre-flop? How does this change as the number of players changes? What is the correct threshold above which a hand should be playable pre-flop given a certain number of players in the game?
* Given m players, what's the distribution of the number of players who will not fold pre-flop?

### To Do's
* Make it possible to input any hands to decide who wins these hands. Will be useful to test edge cases of winner deciding logic.
* Implement kelly criterion––bankroll management
* Fix straight flush logic
* Fix fucking bugs
* Rewrite in Cython

### Game Theory
* Understand extremely simple game: 3 cards (AKQ), two players, can bet 1, call, check, fold, pot p.
* Chapter 13 The Mathematics of Poker
* Originally considered by Mike Caro

### Resources
* https://chrisbeaumont.org/holdem_odds/#8H+QS  

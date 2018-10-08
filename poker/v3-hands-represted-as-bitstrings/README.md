# Poker Simulator

## Docs

### Cards
* Represent cards simply as strings (possibly later as bits)
* 4 Suits
  * C: 00
  * D: 01
  * H: 10
  * S: 11
* Numbers 1-13
  * 1: 0001
  * 2: 0010
  * 3: 0011
  * 4: 0100
  * 5: 0101
  * 6: 0110
  * 7: 0111
  * 8: 1000
  * 9: 1001
  * 10: 1010
  * 11: 1011
  * 12: 1100
  * 13: 1101
* A card is the binary string: bin_num * 4 + bin_suit (i.e. QH = 110010)
* One card is higher than another if bin_card_1 / 4 > bin_card_2 / 4
* Cards are the same value if bin_card_1 / 4 == bin_card_2 / 4
* Cards are the same suit if bin_card_1 % 4 == bin_card_2 % 4

### Deck
* The deck is an array of binaries.
* Can this be optimized?

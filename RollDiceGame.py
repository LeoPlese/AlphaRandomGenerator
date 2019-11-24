# -*- coding: utf-8 -*-

"""

Program: Roll Dice Game
Version: 1.0
Author: Leo Plese
e-mail: plese.leo@gmail.com
Web: alpharandom.info

Abstract:
This game uses Alpha Particles Random Number Generator for generating random number from one to six to simulate rolling six-sided dice.

Note:
For use this program its location need to be in same directory where AlphaRandom.py is located.

"""

import AlphaRandom

diceValue = AlphaRandom.fnRandNumGen("numint", 1, 6)

print("\nDice value is " + str(diceValue) + " " + " *" * diceValue + "\n")



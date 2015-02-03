#Overview

This script checks the price of USD/BTC from Bitstamp by API every three seconds.
The user can input selected amounts of BTC and USD, and a chosen multiplier.
The program then multiplies the selected amounts according to:

Multiplied USD = BTC input * last USD/BTC * chosen multiplier
Multiplied BTC = USD input / (last USD/BTC * chosen multiplier)


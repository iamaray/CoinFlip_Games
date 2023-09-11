import coin

coin1 = coin.Coin()
coin2 = coin.Coin(0.7)

firstRun = coin1.nFlips(10000)

print(coin2.nFlips(int(1e6))[0])
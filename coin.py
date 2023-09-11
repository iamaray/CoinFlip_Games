import random

class Coin:
    def __init__(self, pHeads=0.5, initState='N'):
        # The coin bias (default value is 1/2, i.e., a fair coin).
        self.pHeads = pHeads

        # H: heads, T: tails, N: unflipped (default initial state)
        self.currentState = initState

    # Flip the coin once, and record the result
    def flip(self):
        outcome = random.choices([0, 1], weights=[self.pHeads, 1 - self.pHeads])
        self.currentState = 'H' if outcome[0] == 0 else 'T'
        return 'H' if outcome[0] == 0 else 'T'
    
    # Flip the coin n times, and record the results
    def nFlips(self, n):
        currFlips = []
        for flip in range(n):
            currFlips.append(self.flip())
        hCnt = currFlips.count('H') 
        tCnt = currFlips.count('T')
        return f"H:{hCnt}, T:{tCnt}, Current State:{self.currentState}", currFlips

    # Return a representation of the current state.
    def __repr__(self) -> str:
        return f"H:{self.flipHistory.count('H')}, T:{self.flipHistory.count('T')}, Current State:{self.currentState}"
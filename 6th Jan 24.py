from typing import List
class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        x = [i for i in range(b+1)]
        for i in range(2, int(b**0.5)+1):
            if x[i] == i:
                for j in range(i*i, b+1, i):
                    x[j] = i
        y = 0
        for n in range(a, b+1):
            while n > 1:
                y = y + 1
                n = n // x[n]
        return y
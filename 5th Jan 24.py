class Solution:
    def TotalWays(self, N):
        modulo = 10**9 + 7
        x = 1
        y = 2
		for i in range(2, N+1):
            z = y
	        z = z + x
	        z = z % modulo
            x, y = y, z
        return (y**2) % modulo
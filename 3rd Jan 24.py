class Solution:
    def smallestSubstring(self, S):
        counter = {'0':0, '1':0, '2':0}
        start = end = 0
        length = len(S)
        ans = 1e9 
        
        while end < length : 
            counter[ S[end] ] += 1 
            while counter['0'] and counter['1'] and counter['2'] : 
                counter[ S[start] ] -= 1
                ans = min(ans, end-start+1)
                start += 1
            end += 1
        
        return -1 if ans == 1e9 else ans
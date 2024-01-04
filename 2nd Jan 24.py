class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        s,m=0,float('-inf')
        l,r=0,0
        st=0
        while r < n :
            s += a[r]
            if r-l +1 == k :
                m=max(m,s)
            if r-l +1 > k :
                m=max(m,s)
                st += a[l]
                l +=1
                if st < 0 :
                    s -=st
                    st =0
                m=max(m,s)
            r +=1
        return m
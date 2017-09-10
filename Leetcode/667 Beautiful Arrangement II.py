class Solution(object):
    def constructArray(self, n, k):
        i, j = 1, n
        res = []
        while i <= j:
            res.append(i)
            if i != j:
                res.append(j)
            i+=1
            j-=1
        res = res[:k-1] + sorted(res[k-1:])
        if k>1 and res[k-2]<=n/2:
            res = res[:k-1] + res[k-1:][::-1]
        return res

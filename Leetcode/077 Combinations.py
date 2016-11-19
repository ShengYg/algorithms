class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        out = []
        self.comb(out, [], 1, n, k)
        return out

    def comb(self, out, list, start, n, k):
        if k == 0:
            out.append(list)
            return
        for i in range(start, n + 1):
            self.comb(out, list + [i], i + 1, n, k - 1)

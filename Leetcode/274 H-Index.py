class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        if not length:
            return 0
        array = [0 for i in range(length + 1)]
        for i in range(length):
            if citations[i] > length:
                array[length] += 1
            else:
                array[citations[i]] += 1
        t, result = 0, 0
        for i in range(length, -1, -1):
            t += array[i]
            if t >= i:
                return i
        return 0

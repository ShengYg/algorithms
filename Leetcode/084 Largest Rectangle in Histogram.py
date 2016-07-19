class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        length = len(heights)
        if length == 0:
            return 0
        return self.getmax(heights, 0, length)
    
    def getmax(self, heights, s, e):
        if s + 1 == e:
            return heights[s]
        mini = s
        issort = True
        for i in range(s, e):
            if i > s and heights[i] < heights[i - 1]:
                issort = False
            if heights[mini] > heights[i]:
                mini = i
        if issort:
            maxi = 0
            for i in range(s, e):
                maxi = max(maxi, heights[i] * (e - i))
            return maxi
        left = self.getmax(heights, s, mini) if mini > s else 0
        right = self.getmax(heights, mini + 1, e) if mini < e - 1 else 0
        return max(max(left, right), (e - s) * heights[mini])

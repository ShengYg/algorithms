class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a, b, water, leftmax, rightmax = 0, len(height) - 1, 0, 0, 0
        while a <= b:
            leftmax = max(leftmax, height[a])
            rightmax = max(rightmax, height[b])
            if leftmax < rightmax:
                water += (leftmax - height[a])
                a += 1
            else:
                water += (rightmax - height[b])
                b -= 1
        return water

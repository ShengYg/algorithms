class Solution:
    def isHappy(self, n):
		"""
        :type n: int
        :rtype: bool
        """
        l = []
        while True:
            num = 0
            for i in str(n):
                num += int(i) ** 2
            if num in l:
                return False
            elif num == 1:
                return True
            l.append(num)
            n = num



class Solution:
    def isHappy(self, n):
		"""
        :type n: int
        :rtype: bool
        """
        while True:
            num = 0
            for i in str(n):
                num += int(i) ** 2
            if num == 4:
                return False
            elif num == 1:
                return True
            n = num

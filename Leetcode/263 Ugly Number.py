class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        while not num % 2:
            num /= 2
        while not num % 3:
            num /= 3
        while not num % 5:
            num /= 5
        return  num == 1



class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        while not num % 2:
            num = num >> 1		##faster
        while not num % 3:
            num /= 3
        while not num % 5:
            num /= 5
        return  num == 1

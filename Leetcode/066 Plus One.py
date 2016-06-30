class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits[0] += 1
        carry = 0
        for i in range(len(digits)):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
                break
        if carry:
            digits.append(1)
        digits.reverse()
        return digits

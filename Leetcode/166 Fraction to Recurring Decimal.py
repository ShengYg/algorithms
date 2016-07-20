class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator > 0 else ''
        result = [sign, str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))
        idx = stack.index(remainder)
        result.insert(idx + 3, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        if remainder == 0:
            return ''.join([sign, str(n)])
        result = [sign, str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))
        idx = stack.index(remainder)
        result.insert(idx + 3, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '')

from itertools import permutations, product,chain
from itertools import izip_longest as zip_longest
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = ''.join([str(i) for i in nums])
        digiperm = sorted(set(permutations(nums)))
        opcomb = list(product('+-*/', repeat=3))
        brackets = ([()] + [(x, y) for x in range(0, 7, 2) for y in range(x + 4, 7 + 2, 2) if (x, y) != (0, 7 + 1)]
                    + [(0, 3 + 1, 4 + 2, 7 + 3)])
        for d in digiperm:
            for ops in opcomb:
                if '/' in ops:
                    d2 = [('%s.' % i) for i in d]
                else:
                    d2 = d
                ex = list(chain.from_iterable(zip_longest(d2, ops, fillvalue='')))
                for b in brackets:
                    exp = ex[::]
                    for insertpoint, bracket in zip(b, '()' * (len(b) // 2)):
                        exp.insert(insertpoint, bracket)
                    txt = ''.join(exp)
                    try:
                        num = eval(txt)
                    except ZeroDivisionError:
                        continue
                    if abs(num - 24) < 1e-9::
                        return True
        return False

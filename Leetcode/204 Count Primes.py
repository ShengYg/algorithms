class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True] * n
        i = 2
        while i * i < n:
            if isPrime[i] == False:
                i += 1
                continue
            for j in range(i*i, n, i):
                isPrime[j] = False
            i += 1
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count



class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        isPrime = [True] * n
        i = 2
        while i * i < n:
            if isPrime[i]:
                isPrime[i**2: n: i] = [False] * len(isPrime[i * i: n: i])
            i += 1
        return sum(isPrime) - 2



class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        if n < 4:
            return 1
        if n < 10:
            return n/2
        isPrime = [True] * n
        i = 3
        while i * i < n:
            if isPrime[i]:
                length = len(isPrime[i * i: n: 2*i])
                isPrime[i**2: n: 2*i] = [False] * length
            i += 2
        return sum(isPrime) - int(round(float(n) / 2))

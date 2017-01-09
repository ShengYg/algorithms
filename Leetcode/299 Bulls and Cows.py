class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow = 0, 0
        num = [0 for i in range(10)]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if num[int(secret[i])] < 0:
                    cow += 1
                if num[int(guess[i])] > 0:
                    cow += 1
                num[int(secret[i])] += 1
                num[int(guess[i])] -= 1
        return '{}A{}B'.format(bull, cow)


from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)

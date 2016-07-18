class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        result = {}
        for s in strs:
            if s == "":
                key = 0
            else:
                key = reduce((lambda x,y:x*y), [prime[ord(i)-97] for i in s])
            result[key] = result.get(key, []) + [s]
        return [i for i in result.values()]


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for i in strs:
            key = ''.join(sorted(i))
            hashmap[key] = hashmap.get(key, []) + [i]
        return [v for v in hashmap.values()]

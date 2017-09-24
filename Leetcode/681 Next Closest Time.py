from itertools import product
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        time_old = int(''.join(time[:2])) * 60 + int(''.join(time[3:]))
        time_ = time
        time = [item for item in time if item.isdigit()]
        time = set(product(time, repeat=4))
        time = filter(lambda item: int(''.join(item[:2])) <= 24 and int(''.join(item[2:])) <= 59, time)
        min = float('inf')
        ret = None
        for item in time:
            time_new = int(''.join(item[:2])) * 60 + int(''.join(item[2:]))
            if time_new > time_old and time_new - time_old < min:
                min = time_new - time_old
                ret = item
            elif time_new < time_old and time_new + 2400 - time_old < min:
                min = time_new + 2400 - time_old
                ret = item
        return ''.join(ret[:2]) + ':' + ''.join(ret[2:]) if ret else time_

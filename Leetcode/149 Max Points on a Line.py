# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        L = len(points)
        if L < 2:
            return 1
        result = 0
		points = sorted(points, key = lambda i:i.x)	#better
        for i in range(L):
            myMap, verticle, duplicate = {}, 0 ,0
            for j in range(i+1,L):
                a = points[i]
                b = points[j]
                if a.x == b.x:
                    if a.y != b.y:
                        verticle += 1
                    else:
                        duplicate += 1
                else:
                    slope = float(b.y - a.y) / float(b.x - a.x)
                    myMap[slope] = myMap.setdefault(slope,0) + 1
            
            try:
                slopeMax = max(myMap.values())
            except:
                slopeMax = 0
            maxPointOnLine = max(slopeMax, verticle) + duplicate
            if maxPointOnLine > result:
                result = maxPointOnLine
        
        return result+1

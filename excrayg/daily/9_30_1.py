#Let P be a set of n points in the plane. Each point hasd integer coordinates. Design an effecient algo for comouting a line that contains the max number of points in P.

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        from collections import defaultdict
        slope_map = defaultdict(int)
        for i in range(n):
            point1 = points[i]
            for j in range(i+1, n):
                point2 = points[i]
                numerator = point2.y - point1.y
                denom = point2.x - point1.x
                if denom == 0:
                    slope_map["inf"] += 1
                else:
                    slope_map[numerator/denom] += 1
                    
        max_p = float("-inf")
        for k,v in slope_map.items():
            max_p = max(max_p, v)
            
        return max_p
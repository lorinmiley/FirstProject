import intersection
from math import *

# content of test_class.py
class TestClass:
    #test for intersection at a point
    def test_One(self):
        line1 = [[2,8],[2,-2]]
        line2 = [[9,10],[-2,2]]
        result = intersection.intersects(line1, line2)
        assert isclose(result[0], 2, abs_tol=1e-1) and isclose(result[1], 4.9, abs_tol=1e-1)

    #test for infinite intersection parrallel lines
    def test_Two(self):
        line1 = [[-1,-1],[1,1]]
        line2 = [[0,0],[2,2]]
        result = intersection.intersects(line1, line2)
        assert result == inf

    #test for no intersection
    def test_Three(self):
        line1 = [[1,1],[1,2]]
        line2 = [[0,0],[1,3]]
        result = intersection.intersects(line1, line2)
        assert result == None
    
    #test for intersection at one end
    def test_Four(self):
        line1 = [[1,1],[1,2]]
        line2 = [[1,2],[1,5]]
        result = intersection.intersects(line1, line2)
        assert result == [1,2]
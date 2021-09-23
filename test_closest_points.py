import closest_pair
from math import *

# content of test_class.py
class TestClass:

    def test_one(self):
        #creates a 2d array with numerical points
        test_points = [[1,2],[3,6],[3,3],[1,9],[9,0],[8,10],[99,34]]
        tester = closest_pair.calculate_closest_pair(test_points)
        assert isclose(tester[2], 2.2, abs_tol=1e-1)

    def test_Two(self):
        #creates a 2d array with numerical points
        test_points = [[1,2],[3,6],[3,3],[1,3],[9,0],[8,10],[99,34]]
        tester = closest_pair.calculate_closest_pair(test_points)
        assert isclose(tester[2], 1, abs_tol=1e-1)

    def test_Three(self):
        #creates a 2d array with numerical points
        test_points = [[1,2],[3,6],[3,3],[4,4],[9,0],[8,10],[99,34]]
        tester = closest_pair.calculate_closest_pair(test_points)
        assert isclose(tester[2], 1.4, abs_tol=1e-1)

    def test_Four(self):
        #creates a 2d array with numerical points
        test_points = [[1,2],[3,6],[2,6.5],[4,4],[9,0],[8,10],[99,34]]
        tester = closest_pair.calculate_closest_pair(test_points)
        assert isclose(tester[2], 1.1, abs_tol=1e-1)

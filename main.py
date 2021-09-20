#Computational Geometry Project
#The purpose of this project is to create a python application where the user can input a text file
#   that contains a header with a type of problem to solve, line segment intersection, closest pair points,
#   convex hull, or largest empty circle followed by a given set of points seperated by line with a space seperating x and y

#Programmers:
#   Humberto Ortega
#   Lorin llene Miley
#   Jacob A Hendricks
#   Hope Elizabeth Fetrow

#imports
from readwrite import *
from intersection import *
from convex import *
from closest_pair import *
from largest_empty_circle import *
import sys

#main class
class Main:
    @staticmethod
    def __init__(*args: str) -> None:
        #main running code goes here
        # filename = 'test_txt_files/test_intersection.txt'
        filename = 'test_txt_files/test_pair_of_points.txt'
        # filename = 'test_txt_files/test_convex.txt'
        # filename = 'test_txt_files/test_largest_empty_circle.txt'

        #parse the text file to an array
        data_array = read_txt(filename)

        #holds string that will be returned to print to a file
        results = ''
        
        #if the first line of the file asks for intersection run this code
        if(data_array[0] == 'Line Segment Intersection'):
            results = find_intersections(data_array)

        #else if the first line of the file asks for closest pair of points run this
        elif(data_array[0] == 'Closest Pair Of Points'):
            results = find_closest_pair(data_array)

        #else if the first line of the file asks for the Convex Hull
        elif(data_array[0] == 'Convex Hull'):
            results = find_convex_hull(data_array)
        
        #else if the first line of the file asks for the Largest empty circle
        elif(data_array[0] == 'Largest Empty Circle'):
            results = find_closest_pair(data_array)

        write_txt(results)
        return

if __name__ == '__main__':
    Main()
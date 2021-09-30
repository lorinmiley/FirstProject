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

#function list_to_arrays converts a list of points in a 2d array of numerical values (can be used for 3 out of the 4 problem types)
def array_to_points(data_array):
    #Removes the first element of the array since we dont need it anymore (problem type)
    data_array.pop(0)

    #creates a 2d array with numerical points
    rows, cols = (len(data_array), 2)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    count = 0
    for i in data_array:
        points = i.split()
        arr[count][0] = int(points[0])
        arr[count][1] = int(points[1])
        count = count + 1
    return arr
    
#function array_to_lines converts a list of points in a 3d array into a a set of line segments
def array_to_lines(data_array):
    #Removes the first element of the array since we dont need it anymore (problem type)
    data_array.pop(0)

    #finds the number of lines in the txt file
    numb_lines = 0
    for i in data_array:
        if(i == "_Line_"):
            numb_lines += 1

    #create a 3d array each line contains a 2d array with all its points
    rows, cols, dim = (2, 2, numb_lines)
    arr = [[[0 for i in range(cols)] for j in range(rows)] for k in range(dim)]

    firstpoint = 1
    count = 0
    for i in data_array:
        if(i != "_Line_"):
            points = i.split()
            if(firstpoint == 1):
                arr[count][0][0] = int(points[0])
                arr[count][0][1] = int(points[1])
                firstpoint = 0
            elif(firstpoint == 0):
                arr[count][1][0] = int(points[0])
                arr[count][1][1] = int(points[1])
                count = count + 1
                firstpoint = 1   

    return arr
    
#main class
class Main:
    @staticmethod
    def __init__(*args: str) -> None:
        #main running code goes here
        #filename = 'test_intersection.txt'
<<<<<<< HEAD
        filename = 'test_pair_of_points.txt'
        # filename = 'test_convex.txt'
        # filename = 'test_largest_empty_circle.txt'
=======
        # filename = 'test_pair_of_points.txt'
        # filename = 'test_convex.txt'
        filename = 'test_largest_empty_circle.txt'
>>>>>>> 5bf7bfbf96920ea9f6fb063eef20f6f35045ecad

        #parse the text file to an array
        data_array = read_txt(filename)

        #holds string that will be returned to print to a file
        results = ''
        
        #if the first line of the file asks for intersection run this code
        if(data_array[0] == 'Line Segment Intersection'):
            results = find_intersections(array_to_lines(data_array))

        #else if the first line of the file asks for closest pair of points run this
        elif(data_array[0] == 'Closest Pair Of Points'):
            results = find_closest_pair(array_to_points(data_array))

        #else if the first line of the file asks for the Convex Hull
        elif(data_array[0] == 'Convex Hull'):
            results = find_convex_hull(array_to_points(data_array))
        
        #else if the first line of the file asks for the Largest empty circle
        elif(data_array[0] == 'Largest Empty Circle'):
            results = find_largest_empty_circle(array_to_points(data_array))

        #write_txt(results)
        print(results)
        return

if __name__ == '__main__':
    Main()
#Function to find Line Segment Intersections
#   Find the intersections between a given set of line segments.
import math

#function find_intersection takes in two line segments containing two 2d points each and returns whether or
#not the two intersect, do not, or intersect at infinite points
def intersects(line1, line2):
    #place line point values into their appropriate x and y 
    x1, x2, x3, x4 = line1[0][0], line1[1][0], line2[0][0], line2[1][0]
    y1, y2, y3, y4 = line1[0][1], line1[1][1], line2[0][1], line2[1][1]

    #create vectors for determining points of intersection
    dx1 = x2 - x1
    dx2 = x4 - x3
    dy1 = y2 - y1
    dy2 = y4 - y3
    dx3 = x1 - x3
    dy3 = y1 - y3

    #find determinants
    det = dx1 * dy2 - dx2 * dy1
    det1 = dx1 * dy3 - dx3 * dy1
    det2 = dx2 * dy3 - dx3 * dy2

    #if one line is the same as another but in the opposite direction then we know the number of intersection points is infinite
    if(x1 == x4 and y1 == y4 and x2 == x3 and y2 == y3):
        return math.inf

    #will check if the determinent is 0 in which case, the lines are parallel
    if det == 0.0:  
        if dx1:
            if x1 < x3 < x2 or x1 > x3 > x2:
                return math.inf  
        else:
            if y1 < y3 < y2 or y1 > y3 > y2:
                return math.inf 

        #if the the line intersects at one of the given line segment end points return that point of intersection
        if line1[0] == line2[0] or line1[1] == line2[0]:
            return line2[0]
        elif line1[0] == line2[1] or line1[1] == line2[1]:
            return line2[1]

        #if nothing else has run then they are parallel but do not intersect so return none since there is no intersection
        return None  

    #if the lines are found to intersect but not at any end point, perform the calculations to find the point
    s = det1 / det
    t = det2 / det

    if 0.0 < s < 1.0 and 0.0 < t < 1.0:
        return x1 + t * dx1, y1 + t * dy1


#function find_intersections runs to find the intersection points and formats them into a string to be saved to a file later
def find_intersections(data_array):
    #Write result to this string that will print int txt file
    result = "Intersections From a Given Set of Line Segments:"

    for i in data_array:
        result = result + "\nLine: " + str(data_array[0])

    result = result + "\n\n"

    for k,i in enumerate(data_array):
        for j in data_array[k:]:
            if(i != j):
                intersection_point = intersects(((i[0][0],i[0][1]), (j[0][0],j[0][1])),((i[1][0],i[1][1]), (j[1][0],j[1][1])))
                if(intersection_point != None):
                    result = result + "Line Segment " + "(" + str(i[0][0]) + "," + str(i[0][1]) + ")(" + str(j[0][0]) + "," + str(j[0][1]) + ") INTERSECTS (" + str(i[1][0]) + "," + str(i[1][1]) + ")(" + str(j[1][0]) + "," + str(j[1][1]) + ") AT POINT " + str(intersection_point) + "\n"


    return result
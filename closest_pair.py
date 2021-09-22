#Function to find the Closest Pair of Points
#   Given a set of points, find the two with the smallest distance from each other.

#imports
import math

def find_closest_pair(data_array):
    #Write result to this string that will print int txt file
    result = ''

    #starting points with a starting distance for comparison
    closest_pair_point1 = data_array[0]
    closest_pair_point2 = data_array[1]
    closest_distance = math.sqrt((closest_pair_point2[0] - closest_pair_point1[0]) ** 2 + (closest_pair_point2[1] - closest_pair_point1[1]) ** 2)

    #finds smallest distance between two unique points using distance formula
    for i in data_array:
        for j in data_array:
            if(i[0] != j[0] and i[1] != j[1]):
                tempdistance = math.sqrt((j[0]-i[0]) ** 2 + (j[1]-i[1]) ** 2)
                if(tempdistance < closest_distance):
                    closest_distance = tempdistance
                    closest_pair_point1 = i
                    closest_pair_point2 = j

    #formatting the results which will later be written to a file
    for i in data_array:
        result = result + "(" + str(i[0]) + "," + str(i[1]) + ")\n"
    result = "Closest Pair of Points Results:\n\nData Points:\n" + result + "\nClosest Pair of Points: \n(" + str(closest_pair_point1[0]) + "," + str(closest_pair_point1[1]) + ")\n(" + str(closest_pair_point2[0]) + "," + str(closest_pair_point2[0]) + ")\n\nDistance: " + str(closest_distance)
    
    return result
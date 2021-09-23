#Function to find the Closest Pair of Points
#   Given a set of points, find the two with the smallest distance from each other.

#imports
import math

#function format_result formats the result information so that it can be desplayed on terminal/file
def calculate_closest_pair(data_array):
    #starting points with a starting distance for comparison
    closest_pair_point1 = data_array[0]
    closest_pair_point2 = data_array[1]
    closest_distance = math.sqrt((closest_pair_point2[0] - closest_pair_point1[0]) ** 2 + (closest_pair_point2[1] - closest_pair_point1[1]) ** 2)

    #finds smallest distance between two unique points using distance formula
    for i in data_array:
        for j in data_array:
            tempdistance = math.sqrt((j[0]-i[0]) ** 2 + (j[1]-i[1]) ** 2)

            if(tempdistance != 0.0):
                if(tempdistance < closest_distance):
                    closest_distance = tempdistance
                    closest_pair_point1 = i
                    closest_pair_point2 = j

    answer = [closest_pair_point1, closest_pair_point2, closest_distance]
    return answer

def find_closest_pair(data_array):
    #Write result to this string that will print int txt file
    result = ''
    answer = calculate_closest_pair(data_array)
    #starting points with a starting distance for comparison
    closest_pair_point1 = answer[0]
    closest_pair_point2 = answer[1]
    closest_distance = answer[2]

    #formatting the results which will later be written to a file
    for i in data_array:
        result = result + "(" + str(i[0]) + "," + str(i[1]) + ")\n"
    result = "Closest Pair of Points Results:\n\nData Points:\n" + result + "\nClosest Pair of Points: \n(" + str(closest_pair_point1[0]) + "," + str(closest_pair_point1[1]) + ")\n(" + str(closest_pair_point2[0]) + "," + str(closest_pair_point2[1]) + ")\n\nDistance: " + str(closest_distance)
    
    return result
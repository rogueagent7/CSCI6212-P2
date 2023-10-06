import math
import random
import time


def mergeSort(array):
    if len(array) > 1:
        #  r is the point where the array is divided into two subarrays
        r = len(array) // 2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i].y < M[j].y:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

    # Print the Points
def printList(array):
    for i in range(len(array)):
        print(f"Point({array[i].x},{array[i].y})")
    return print()


class Point:
    def __init__(self, x, y):
        self.x = x

        self.y = y

#Find the minimum of two distances
def min(x, y):
    if x < y:
        return x
    else:
        return y
    # return x if x < y else y


#Calculate the distance between points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

#Find the smallest distance between the Points in the array

def smallest_distance(values):
    # idx = 0
    initial_distance_calculated = dist(values[0], values[1])
    smallest = initial_distance_calculated
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            subsequent_distance_calculated = dist(values[i], values[j])
            if subsequent_distance_calculated < smallest:
                smallest = subsequent_distance_calculated
    return smallest

#Find the minimum of the smallest value obtained from the left side and right of the array
def upperBound_of_min(smallest_upper_bound: int, values: Point):
    midpoint = len(values) // 2
    closer_coordinates = []
    for i in range(len(values)):
        if values[i].x - midpoint < smallest_upper_bound:
            closer_coordinates.append(values[i])
    return closer_coordinates

#Sorting the strip array which represents points with y coordinates smaller than the upperbound minimum
def sorting_strip_to_find_smallest_distance(smallest: int, closer_coordinates: list):
    minimum_distance = smallest

    for i in range(len(closer_coordinates)):
        for j in range(i + 1, len(closer_coordinates)):
            if closer_coordinates[j].y - closer_coordinates[i].y >= minimum_distance:
                break
            if dist(closer_coordinates[i], closer_coordinates[j]) < minimum_distance:
                minimum_distance = dist(closer_coordinates[i], closer_coordinates[j])
    return minimum_distance


if __name__ == "__main__":
    P = [] # point collection array
    n = 0 # is the number of points
    while n < 300:
        x = random.randint(0, 50) # random values from 0 to 50
        y = random.randint(0, 50) # random values from 0 to 50

        newPoint = Point(x, y) # create new instance of the Point class
        P.append(newPoint) # add to the point collection array, P

        FileOpen = open("Points.txt", "a") #Open a Point.txt file if it doesn't exist
        # FileOpen.write(f"Points({x},{y})\n")
        FileOpen.write(f"Points({x},{y})\n") # write to the file
        n += 1 # increase counter by one
        FileOpen.close() # close file

    start_time = time.time_ns() # start time of execution
    mergeSort(P) # merge-sort of points on the y coordinates
    FileOpen2 = open("Sorting_on_Y.txt", "a") #Open a Sorting_on_Y.txt file if it doesn't exist
    for i in range(len(P)): # write to file
        FileOpen2.write(f"Point({P[i].x},{P[i].y})\n")

    FileOpen2.close()#close file

    mid_point = len(P) // 2 #split array into two
    arrayLeft_Side = P[:mid_point] # left is from index 0 to the midpoint index
    # print(f"arrayLeft_side:{arrayLeft_Side}")
    arrayRight_Side = P[mid_point + 1 :] # right from index just after the midpoint to the end

#We find the smallest distance possible in the left array
    arrayLeft_Side_minimum_smallest_distance = smallest_distance(arrayLeft_Side)
    print(
        f"Array Left Side Minimum Smallest Distance: {arrayLeft_Side_minimum_smallest_distance}"
    )
    # We find the smallest distance possible in the right array
    arrayRight_Side_minimum_smallest_distance = smallest_distance(arrayRight_Side)
    print(
        f"Array Right Side Minimum Smallest Distance: {arrayRight_Side_minimum_smallest_distance}"
    )

# we find the smallest of the smallest values from the left and right. This becomes our bound(delta)
    smallest_distance_upperBound = min(
        arrayLeft_Side_minimum_smallest_distance,
        arrayRight_Side_minimum_smallest_distance,
    )
    print(f"Smallest Distance Upper Bound: {smallest_distance_upperBound}")

# we find all point on the left side of our delta that have Y coordinates less than our delta
    Left_closer_coordinates = upperBound_of_min(
        smallest_distance_upperBound, arrayLeft_Side
    )
    # print(f"Left closer Coordinates : {Left_closer_coordinates}")

    # we find all point on the right side of our delta that have Y coordinates less than our delta
    Right_closer_coordinates = upperBound_of_min(
        smallest_distance_upperBound, arrayRight_Side
    )
    # print(f"Right closer Coordinates : {Right_closer_coordinates}")

#we put these coordinates with Y
    # coordinates less than our delta into an array. by joining those seperate arrays
    Left_Right_closer_coordinates = Left_closer_coordinates + Right_closer_coordinates
    # print(f"Left and Right closer Coordinates : {Left_Right_closer_coordinates }")

#Merge sort those points
    # write to file
    mergeSort(Left_Right_closer_coordinates)
    FileOpen3 = open("LeftRight_closerPoints.txt", "a")
    for a in range(len(P)):
        FileOpen3.write(f"Point({P[a].x},{P[a].y})\n")
    FileOpen3.close()

#We find the point that have the smallest distance in that collection
    #Write to file
    minimum_distance = sorting_strip_to_find_smallest_distance(
        smallest_distance_upperBound, Left_Right_closer_coordinates
    )
    print(f"The smallest distance is {minimum_distance}")

    stop_time = time.time_ns()
    execution_time = stop_time - start_time
    FileOpen4 = open("Execution Time", "a")
    FileOpen4.write(f"The execution Time for {n} Points: {execution_time}\n")
    FileOpen4.close()

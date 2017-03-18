###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    
    return {'Maggie':3,'Herman':7,'Betsy':9,'Oreo':6,'Moo Moo':3,'Milkshake':2,'Millie':5,'Lola':2,'Florence':2,'Henrietta':9}

# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowList = cows.copy()
    output = []
    
    def tripWeight(tripList):
        sum = 0
        for i in tripList:
            sum += cows[i]
        return sum
        
    def getCow(maxLimit, cows):
        currentCow = ()
        for c in cows:
            if cows[c] <= maxLimit and cows[c] >= 0:
                if len(currentCow) == 0:
                    currentCow = (c, cows[c])
                else:
                    if cows[c] > currentCow[1]:
                        currentCow = (c, cows[c])
        return currentCow
    
    while len(cowList) > 0:
        trip = []
        while True:
            cow = getCow(limit - tripWeight(trip), cowList)
            if len(cow) > 0:
                trip.append(cow[0])
                del(cowList[cow[0]])
            else:
                output.append(trip)
                break
    return output


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
def brute_force_cow_transport(cowDict, limit=10):
    output = []
    cowList = []
    transportedCows = []
    
    def getPartitionWeight(cList):
        totalWeight = 0
        for p in cList:
            totalWeight += cowDict[p]
        return totalWeight
    
    for i in cowDict:
        cowList.append(i)
    
    while len([x for subList in output for x in subList]) < len(cowDict):
        currentSet = []
        currentSetWeight = 0
        for partition in get_partitions(cowList):
            for cowSet in partition:
                if len(set(cowSet).intersection(set(transportedCows))) > 0:
                    continue
                cowSetWeight = getPartitionWeight(cowSet)
                if not cowSet in output and cowSetWeight <= limit and len(cowSet) >= len(currentSet) and cowSetWeight > currentSetWeight:
                    currentSet = cowSet
                    currentSetWeight = cowSetWeight
        
        output.append(currentSet)
        transportedCows += currentSet
    return output

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    start = time.time()
    print(greedy_cow_transport(cows))
    end = time.time()
    print('greedy_cow_transport time = ' + str(end - start))

    start = time.time()
    print(brute_force_cow_transport(cows))
    end = time.time()
    print('brute_force_cow_transport time = ' + str(end - start))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
#limit=100
#print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()


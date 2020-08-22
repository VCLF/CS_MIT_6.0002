###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Vicente Carvalho
# Collaborators: -
# Time: -

from ps1_partition import get_partitions
import time
import pandas as pd

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    file = open(filename,"r")
    cows_names = {}
    line = ''
    for line in file:
        [name, age] = list(line.split(','))
        cows_names[name] = int(age)
    file.close()
    return cows_names

# Problem 2
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
    # TODO: Your code here
    travel_weights = []
    travel_names = []
    cows_df = pd.DataFrame()
    cows_df['name'] = cows.keys()
    cows_df['weight'] = cows.values()
    cows_df.sort_values(['weight'], ascending=False, inplace=True)
    cows_df['trip'] = 0
    cases = cows_df.shape[0]
    trip = 0
    while cases > 0:
        budget = limit
        trip += 1 
        for ind, row in cows_df.iterrows():
            weight = row['weight']
            if row['trip'] == 0:
                if weight <= budget:
                    cows_df.at[ind, 'trip'] = trip
                    budget -= weight
                    cases -= 1
            if budget == 0:
                break
    trips = cows_df.trip.unique()
    for trip in trips:
        travel_weights.append(list(cows_df.loc[(cows_df.trip == trip),'weight']))
        travel_names.append(list(cows_df.loc[(cows_df.trip == trip),'name']))
    return travel_names

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
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
    budget = limit
    best = 1000000
    #import pdb; pdb.set_trace()
    for  partition in get_partitions(cows):
        trips = is_trips_valid(cows, partition, budget)
        if (trips != 0) and (trips < best):
            best = trips
            names = partition
    return (best, names)

def is_trips_valid(cows, travel, limit):
    """ Calcule if travel is valid
    """
    for trip in travel:
        budget = 0
        for cow in trip:
            budget += cows[cow]
            if budget > limit:
                return 0
    return len(travel)

# Problem 4
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
    cows_names = load_cows("ps1_cow_data_2.txt")
    start = time.time()
    travel = greedy_cow_transport(cows_names, 12)
    end = time.time()
    print(" ## Greedy took " + str(round(end-start,3)) + " to finish.")
    print(" ## Greedy solution was " + str(travel)+ ".")
    start = time.time()
    (travel, names) = brute_force_cow_transport(cows_names,12)
    end = time.time()
    print(" ** Brute force took " + str(round(end-start, 3)) + " to finish.")
    print(" ** Brute solution was " + str(names)+ ".")


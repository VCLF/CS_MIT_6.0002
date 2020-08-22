###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Vicente Carvalho
# Collaborators: - 
# Time: -
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

import time

# Problem 1
def dp_make_weight2(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    weights = list(egg_weights)
    if len(weights) == 1:
        return target_weight//weights[0]
    return target_weight//weights[-1] + dp_make_weight2(weights[0:-1], target_weight%weights[-1])

def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    weights = list(egg_weights)
    memo['last'] = memo.get('last',0) + target_weight//weights[-1]
    if len(weights) == 1:
        return memo['last']

    return  dp_make_weight(weights[0:-1], target_weight%weights[-1], memo)

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1,2,3,5,7,11,13,17,19)
    n = 1000
    #import pdb; pdb.set_trace()
    print("Egg weights = " + str(egg_weights))
    print("n = " + str(n))
    start = time.time()
    print("Actual output:", dp_make_weight2(egg_weights, n))
    end = time.time()
    print("Recursive took " + str(round(end-start, 3)) + " seconds.")
    print()
    print("Egg weights = " + str(egg_weights))
    print("n = " + str(n))
    start = time.time()
    print("Actual output:", dp_make_weight(egg_weights, n))
    end = time.time()
    print("DP took " + str(round(end-start, 3)) + " seconds.")
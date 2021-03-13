# Given an array of integers. Check whether it contains a triplet that sums up to zero. 

# Example 1:

# Input: N = 5, arr[] = {0, -1, 2, -3, 1}
# Output: true
# Explanation: 0, -1 and 1 forms a triplet
# with sum equal to 0.

# Example 2:

# Input: N = 3, arr[] = {1, 2, 3}
# Output: false
# Explanation: No triplet with zero sum exists. 

from itertools import combinations

#Function to find triplets with zero sum.    
def findTriplets(arr,n):
    #code here
    comb = combinations(arr,3)
    for item in comb:
        if(item[0]+item[1]+item[2]) == 0:
            print(item)
            break

#demo run
arr = [-1,-2,0,3,4,5]
n = 6
findTriplets(arr, n)
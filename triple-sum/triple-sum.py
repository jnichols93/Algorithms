# Given an Array of sorted Integers find a Triplet 
# where the sum of the triplet is equal to the target sum provided
def trip(arr, target):
    d = dict()
    n = len(arr)
    for i in arr:
        d[i] = 1
    
    i = 0
    j = n - 1
    while i<j:
        s = arr[i] + arr[j]     # Calculate the sum of the elements at i and j position
        diff = target - s       # Calculate the difference needed to complete the table
        if arr[i] != diff and arr[j] != diff and diff in d: # Check if the difference exists in the hashtable and as we cannot reuse elements
            return [arr[i], arr[j], diff]# diff should not be equal to elements at i or j and  then return the triplet if exists
        else:
            if s > target:                                  # If difference does not exist, adjust pointers
                j -= 1
            elif s == target:
                if arr[i+1] + arr[j] < target:
                    i+=1
                else:
                    j-=1
            else:
                i += 1
                
    return [None]

"""Steps and explanation
---
1.   First we hash the array to a dictionary.
2.   Then we take two pointers i and j.
3.   Then we run a loop for i < j:
2.   Then we check all the conditions.
"""
"""Test cases
"""
# arr = [1, 2, 4, 6, 8, 10, 12]
# target = 14
# print(trip(arr, target))

# arr = [-2, -1, 4, 8, 10, 12]
# target = 14
# print(trip(arr, target))

# arr = [1, 2, 4, 6, 8, 10, 12]
# target = 13
# print(trip(arr, target))

# arr = [-2, -1, 4, 8, 11, 12]
# target = 13
# print(trip(arr, target))

# arr = [-2, -1, 4, 8, 15, 17]
# target = 11
# print(trip(arr, target))

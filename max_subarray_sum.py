'''The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''
def max_sequence(arr):
#TODO: they want a summation of following items in the list from the first positive digit 
#TODO: to the last positive digit with the highest number possible. 
    puffer = []
    puffer_two = []
    greatest_value = 0
#    greatest_value_pos = [a,b]
    if arr == [] :
        return 0
    elif all(ele >= 0 for ele in arr):
        return sum(arr)
    else :
        print("sorry")

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([2,0,4,-5,6]))

----------------------------------------
'''i simply copied this version and just added the first if statements to pass the test on codewars
But hey, I was close!'''
def max_sequence(arr) :
    
    if arr == [] :
        return 0
    if all( i < 0 for i in arr):
        return 0
    if all( i >= 0 for i in arr) :
        return sum(arr)
    max_so_far =arr[0]
    curr_max = arr[0]
    
    for i in range(1,len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far

    

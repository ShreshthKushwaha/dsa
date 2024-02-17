#kadane's algorithm
class Solution:
    def maxSubArray(self, nums) -> int:

        ans = -2**31

        currSum = -2**31

        for e in nums:
            currSum = max(e,e+currSum)
            ans = max(currSum,ans)
        return ans    

## possible via divide and conquer as well---> LHS,RHS,CSS->Max return
##     
    

##chatgpt solution

def max_crossing_sum(arr, low, mid, high):
    # Find the maximum subarray sum that crosses the midpoint
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        left_sum = max(left_sum, sum)

    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, high + 1):
        sum += arr[i]
        right_sum = max(right_sum, sum)

    return left_sum + right_sum

def max_subarray_sum(arr, low, high):
    if low == high:
        # Base case: only one element
        return arr[low]

    mid = (low + high) // 2

    # Find the maximum subarray sum in the left and right halves
    left_sum = max_subarray_sum(arr, low, mid)
    right_sum = max_subarray_sum(arr, mid + 1, high)

    # Find the maximum subarray sum that crosses the midpoint
    cross_sum = max_crossing_sum(arr, low, mid, high)

    # Return the maximum of the three values
    return max(left_sum, right_sum, cross_sum)

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr, 0, len(arr) - 1)
print("Maximum subarray sum:", result)    


         

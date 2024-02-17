class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def __init__(self):
        self.count_inversions = 0
    def inversionCount(self, arr, n):
        
        
        
        
        def merge(arr1,arr2):
            sorted_arr = []
            i = 0
            j = 0
            while i<len(arr1) and j<(len(arr2)):
                if arr1[i]<=arr2[j]:
                    
                    sorted_arr.append(arr1[i])
                    i+=1
                else:
                    sorted_arr.append(arr2[j])
                    ##copy pen [8,9,19] [1,2,3]--> inversion har time jab j move karega i se len(arr1) ke sare inversions hain
                    self.count_inversions+=(len(arr1)-1-i+1)
                    j+=1
            if i<len(arr1):
                sorted_arr+=arr1[i:]
            if j<len(arr2):
                sorted_arr+=arr2[j:]
            return sorted_arr
        
        def sort(arr):
            if len(arr)==1:
                return arr
            a = sort(arr[0:len(arr)//2])
            b = sort(arr[len(arr)//2:])
            temp = merge(a,b)
        
            return temp
        sort(arr)    
        return self.count_inversions    
            
            
        # Your Code Here





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends
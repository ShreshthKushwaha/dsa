#Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.
#Examples : 
#Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
#Output :  { 1 2 3 4 } 
#          { 5 , 5 }
#Input : Arr[] = { 4, 1, 2, 3 }
#Output : {4 1}
#         {2 3}
#Input : Arr[] = { 4, 3, 2, 1}
#Output : Not Possible

def find(arr):
    if len(arr)<=1:
        return -1
    all_sum = sum(arr)
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum+=arr[i]
        if curr_sum==(all_sum//2):
            return (arr[0:i+1],arr[i+1:])
    return -1
print (find([4,3,2,1]))    


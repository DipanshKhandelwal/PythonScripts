def findMaximum(arr, low, high): 
    max = arr[low] 
    i = low 
    for i in range(high+1): 
        if arr[i] > max: 
            max = arr[i] 
    return max
  
# Driver program to check above functions */ 
arr = [1, 30, 40, 50, 60, 70, 23, 20] 
n = len(arr) 
print ("The maximum element is %d"% 
        findMaximum(arr, 0, n-1)) 
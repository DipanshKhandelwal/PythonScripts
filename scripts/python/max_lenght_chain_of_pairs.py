class Pair(object): 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
# This function assumes that arr[] is sorted in increasing 
# order according the first (or smaller) values in pairs. 
def maxChainLength(arr, n): 
      
    max = 0
  
    # Initialize MCL(max chain length) values for all indices 
    mcl = [1 for i in range(n)] 
  
    # Compute optimized chain length values in bottom up manner 
    for i in range(1, n): 
        for j in range(0, i): 
            if (arr[i].a > arr[j].b and mcl[i] < mcl[j] + 1): 
                mcl[i] = mcl[j] + 1
  
    # mcl[i] now stores the maximum 
    # chain length ending with pair i 
  
    # Pick maximum of all MCL values 
    for i in range(n): 
        if (max < mcl[i]): 
            max = mcl[i] 
  
    return max
  
# Driver program to test above function 
arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)] 
  
print('Length of maximum size chain is', 
      maxChainLength(arr, len(arr))) 
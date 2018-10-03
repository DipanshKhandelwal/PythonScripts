  
# Class to represent an area 
class area: 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
# Utility method to get maximum survival time 
def maxSurvival(A, B, X, Y, Z, last, memo): 
    # if any of A or B is less than 0, return 0 
    if (A <= 0 or B <= 0): 
        return 0
    cur = area(A, B) 
  
    # if already calculated, return calculated value 
    for ele in memo.keys(): 
        if (cur.a == ele.a and cur.b == ele.b): 
            return memo[ele] 
  
    # step to areas on basis of last chosen area 
    if (last == 1): 
        temp = 1 + max(maxSurvival(A + Y.a, B + Y.b, 
                                   X, Y, Z, 2, memo), 
                       maxSurvival(A + Z.a, B + Z.b, 
                                   X, Y, Z, 3, memo)) 
    elif (last == 2): 
        temp = 1 + max(maxSurvival(A + X.a, B + X.b, 
                                   X, Y, Z, 1, memo), 
               maxSurvival(A + Z.a, B + Z.b, 
                   X, Y, Z, 3, memo)) 
    elif (last == 3): 
        temp = 1 + max(maxSurvival(A + X.a, B + X.b, 
                   X, Y, Z, 1, memo), 
               maxSurvival(A + Y.a, B + Y.b, 
                   X, Y, Z, 2, memo)) 
  
    # store the result into map 
    memo[cur] = temp 
  
    return temp 
  
# method returns maximum survival time 
def getMaxSurvivalTime(A, B, X, Y, Z): 
    if (A <= 0 or B <= 0): 
        return 0
    memo = dict() 
  
    # At first, we can step into any of the area 
    return max(maxSurvival(A + X.a, B + X.b, X, Y, Z, 1, memo), 
           maxSurvival(A + Y.a, B + Y.b, X, Y, Z, 2, memo), 
           maxSurvival(A + Z.a, B + Z.b, X, Y, Z, 3, memo)) 
  
# Driver code to test above method 
X = area(3, 2) 
Y = area(-5, -10) 
Z = area(-20, 5) 
  
A = 20
B = 8
print(getMaxSurvivalTime(A, B, X, Y, Z))
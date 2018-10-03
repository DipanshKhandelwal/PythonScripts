# Python3 code to print trinomial triangle. 
  
# Function to find the trinomial triangle value. 
def TrinomialValue(n, k): 
    # base case 
    if n == 0 and k == 0: 
        return 1
      
    # base cas 
    if k < -n or k > n: 
        return 0
          
    # recursive step. 
    return (TrinomialValue (n - 1, k - 1)+ 
                TrinomialValue (n - 1, k)+
                        TrinomialValue (n - 1, k + 1)) 
  
# Function to print Trinomial Triangle of height n. 
def printTrinomial( n ): 
  
    # printing n rows. 
    for i in range(n): 
  
        # printing first half of triangle 
        for j in range(-i, 1): 
            print(TrinomialValue(i, j),end=" ") 
          
        # printing second half of triangle. 
        for j in range(1, i+1): 
            print( TrinomialValue(i, j),end=" ") 
          
        print("\n",end='') 
          
# Driven Code 
n = 4
printTrinomial(n) 
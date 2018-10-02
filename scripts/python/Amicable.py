
# Python program to check  
# if two numbers are 
# Amicable or not. 
import math 
  
# def to calculate sum  
# of all proper divisors 
# of a given number 
def divSum(n) : 
      
    # Sum of divisors 
    result = 0
  
    # find all divisors  
    # which divides 'num' 
    for i in range(2, int(math.sqrt(n)) + 1) : 
          
        # if 'i' is  
        # divisor of 'n' 
        if (n % i == 0) : 
              
            # if both divisors are same 
            # then add it once else add 
            # both 
            if (i == int(n / i)) : 
                result = result + i 
            else : 
                result = result + 
                         (i + int(n / i)) 
  
    # Add 1 and n to result  
    # as above loop considers 
    # proper divisors greater  
    # than 1. 
    return (result + 1) 
  
# Returns true if x and y  
# are Amicable else false. 
def areAmicable(x, y) : 
  
    if (divSum(x) != y) : 
        return False
          
    return (divSum(y) == x)  
  
# Driver Code 
x = 220
y = 284
if (areAmicable(x, y)) : 
    print ("Yes") 
else : 
    print ("No") 
      
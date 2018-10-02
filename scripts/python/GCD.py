
def gcd(a,b): 
  
    # base case if a and b are equal  
    if (a == b): 
        return a 
    # if a is greater 
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a) 

a = 15 
b = 20
print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
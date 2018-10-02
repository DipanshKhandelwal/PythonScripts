
def gcd(a,b): 
  
   
    if (a == b): 
        return a 
     
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a) 
  

def lcm(a,b): 
    return (a*b) / gcd(a,b) 
  
 
a = 15 
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b)) 
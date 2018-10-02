
# Function calculates the decimal equivalent  
# to given binary number 
  
def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)

# One More Way
def bin2dec(binary):
    print(int(str(binary),2))

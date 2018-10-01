# Function to find the 
# maximum perimeter
def maxPerimeter(arr):
    maxi = 0
    n = len(arr)
    arr.sort(reverse = True)
 
    for i in range(0, n - 2):
        if arr[i] < (arr[i + 1] + arr[i + 2]):
            maxi = max(maxi, arr[i] +
                       arr[i + 1] + arr[i + 2])
            break
 
    if(maxi == 0):
        return "Triangle formation is not possible"
    else:
        return "Maximum Perimeter is: "+ str(maxi)
 
# Driver Code
def main():
    arr1 = [6, 1, 6, 5, 8, 4]
    a = maxPerimeter(arr1)
    print(a)
 
    arr2 = [2, 20, 7, 55, 
            1, 33, 12, 4]
    a = maxPerimeter(arr2)
    print(a)
 
    arr3 = [33, 6, 20, 1, 8,
            12, 5, 55, 4, 9]
    a = maxPerimeter(arr3)
    print(a)
 
if __name__=='__main__':
    main()
 

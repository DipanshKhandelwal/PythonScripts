def ssum(list, sum):
  current = ""
  ssum_h(list, len(list), current, sum)

def ssum_h(list, n, subset, sum):
  if sum == 0:
    print subset
    return
    
  if n == 0:
    return
    
  if list[n-1] <= sum:
    ssum_h(list, n-1, subset, sum)
    ssum_h(list, n-1, subset+`list[n-1]`+" ", sum-list[n-1])
  else:
    ssum_h(list, n-1, subset, sum)

if __name__ == "__main__":
    lst = [int(x) for x in raw_input().split()]
    sum = int(input())
    ssum(lst, sum)
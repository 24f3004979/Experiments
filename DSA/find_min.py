def findMinimum(L):
  low, high = 0, len(L) -1 

  while low < high:
    mid = (low + high)//2

    if L[mid] > L[mid+1]:
      low = mid + 1
    else:
      high = mid
  return L[low]

l = []
for i in range(10):
    import random
    e = random.randint(0,10)
    l.append(e)

print(l)
print(findMinimum(l))

def findMnimum(L):
    '''
    Binary search for smallest element

    Problem : finding smallest element from the given rotated list

    [3,4,5,1,2] <-- Find smallest element

    procedure
    1. take pivot
    2. compare with the other pivot element
    3. if first pivot is smaller then keep comparing to the left
    4. if first pivot is bigger then keep comparing with right
    '''

    l = len(L)
    
    left = 0
    right = l
    mid = l // 2

    pivot = L[mid]

    while left != right:
        first_pivot = (left + mid) // 2
        if pivot > first_pivot:
            left = mid
            mid = (left + right) // 2 

        second_pivot = (mid + right) // 2 
        if pivot < second_pivot:
            right = mid
            mid = (left + right) // 2 
        if pivot > first_pivot:
            return frist_pivot
        elif pivot > second_pivot:
            return second_pivot

l = [3,4,5,1,2]
print(def findMnimum(L):
    '''
    Binary search for smallest element

    Problem : finding smallest element from the given rotated list

    [3,4,5,1,2] <-- Find smallest element

    procedure
    1. take pivot
    2. compare with the other pivot element
    3. if first pivot is smaller then keep comparing to the left
    4. if first pivot is bigger then keep comparing with right
    '''

    l = len(L)
    
    left = 0
    right = l
    mid = l // 2

    pivot = L[mid]

    while left != right:
        first_pivot = (left + mid) // 2
        if pivot > first_pivot:
            left = mid
            mid = (left + right) // 2 

        second_pivot = (mid + right) // 2 
        if pivot < second_pivot:
            right = mid
            mid = (left + right) // 2 
        if pivot > first_pivot:
            return frist_pivot
        elif pivot > second_pivot:
            reutrn second_pivot
l = [3,4,5,1,2]
print(findMnimum(l))

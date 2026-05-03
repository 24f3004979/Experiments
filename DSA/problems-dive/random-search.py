import heapq

def KminGreaterThan(arr, k, num):
    max_heap = []

    for x in arr:
        heapq.heappush(max_heap, -x)
        print(f'Max heap condition : {max_heap}')
        if len(max_heap) > k:
            heapq.heappop(max_heap)
            print(f'After removing a element : {max_heap}')

    kth_smallest = -max_heap[0]
    print(f'Kth smallest element is : {kth_smallest}')
    if kth_smallest < num:
        return True
    return False

l = [29, 18, 10, 3, 1, 90, 20]
print(KminGreaterThan(l, 2, 11))

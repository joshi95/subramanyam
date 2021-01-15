import heapq

if __name__ == "__main__":
    l = [5, 6, 2, 12, 3, 9]
    k = 4

    heap = []
    for item in l:
        heapq.heappush(heap, item)

    cnt = 0
    ans = None
    while cnt < k:
        ans = heapq.heappop(heap)
        cnt += 1


    # time complexity: klogn

    # space complexity: n

    # for a small k and huge n we will be still using n space which is very big
    
    



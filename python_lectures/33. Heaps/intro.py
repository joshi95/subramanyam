heap = [111, 22, 33, 4, 15, 64, 7, 8, 9]


def heapsort():
    global heap

    while len(heap) != 0:
        print(heap[0])
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()
        heapify(0)


def heapify(i):
    global heap

    left_idx = 2 * i + 1
    right_idx = 2 * i + 2

    # leaf node since they are already max heap
    if left_idx > len(heap) - 1 and right_idx > len(heap) - 1:
        return

    max_idx = i
    if left_idx < len(heap) and heap[max_idx] < heap[left_idx]:
        max_idx = left_idx

    if right_idx < len(heap) and heap[max_idx] < heap[right_idx]:
        max_idx = right_idx

    if max_idx != i:
        heap[max_idx], heap[i] = heap[i], heap[max_idx]
        heapify(max_idx)


if __name__ == "__main__":
    n = len(heap)

    #creating a max heap
    for i in range(n - 1, -1, -1):
        heapify(i)

    heapsort()

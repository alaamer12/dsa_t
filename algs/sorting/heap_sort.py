def max_heapify(arr, node, heap_size, order: str):
    largest = node
    left = 2 * node + 1
    right = 2 * node + 2
    if order == "asc":
        compare = lambda x, y: x > y
    elif order == "desc":
        compare = lambda x, y: x < y
    else:
        raise ValueError("order must be 'asc' or 'desc'")
    if left < heap_size and compare(arr[left], arr[largest]):
        largest = left
    if right < heap_size and compare(arr[right], arr[largest]):
        largest = right
    if largest != node:
        arr[node], arr[largest] = arr[largest], arr[node]
        max_heapify(arr, largest, heap_size, order)


def build_heap(arr, heap_size, order: str):
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(arr, i, heap_size, order)
    return arr


def heap_sort(arr, order: str = "asc"):
    heap_size = len(arr)
    arr = build_heap(arr, heap_size, order)
    for i in range(heap_size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0, heap_size, order)
    return arr


if __name__ == '__main__':
    arr = [5, 3, 8, 4, 2, 7, 1, 9]
    print(heap_sort(arr))
    print(heap_sort(arr, "desc"))

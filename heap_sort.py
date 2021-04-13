import heap


def heapify(arr: list):
    heap_item = heap.Heap()
    for item in arr:
        heap_item.insert(item)
    return heap_item


def get_sorted_arr(heap_item) -> list:
    arr = []
    while heap_item.size:
        arr.append(heap_item.extract_min())
    return arr


list_arr = [49, 2, 78, 0, 15, 4]
heap_from_arr = heapify(list_arr)
sorted_arr = get_sorted_arr(heap_from_arr)
print(sorted_arr)

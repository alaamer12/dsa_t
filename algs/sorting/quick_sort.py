from typing import List
import timeit


def quick_sort(arr: List[int], order: str = "asc") -> List[int]:
    if len(arr) <= 1:
        return arr
    else:
        if order == "asc":
            less_compare = lambda x, y: x >= y
            greater_compare = lambda x, y: x < y
        elif order == "desc":
            less_compare = lambda x, y: x <= y
            greater_compare = lambda x, y: x > y
        else:
            raise ValueError("order must be 'asc' or 'desc'")
        pivot = arr[0]
        less = [i for i in arr[1:] if less_compare(i, pivot)]
        greater = [i for i in arr[1:] if greater_compare(i, pivot)]
        return quick_sort(greater, order) + [pivot] + quick_sort(less, order)


def standard_quick_sort(arr: List[int], start, end) -> List[int]:
    if start < end:
        pivot = (start + end) // 2
        arr[end], arr[pivot] = arr[pivot], arr[end]
        p = start
        for i in range(start, end):
            if arr[i] <= arr[end]:
                arr[i], arr[p] = arr[p], arr[i]
                p += 1
        arr[p], arr[end] = arr[end], arr[p]
        standard_quick_sort(arr, start, p - 1)
        standard_quick_sort(arr, p + 1, end)
    return arr

def another_standard_quick_sort(arr: List[int], start, end) -> List[int]:
    if start < end:
        pivot = partition(arr, start, end)
        standard_quick_sort(arr, start, pivot - 1)
        standard_quick_sort(arr, pivot + 1, end)
    return arr

def partition(arr: List[int], start, end) -> int:
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


if __name__ == '__main__':
    arr = [5, 3, 8, 4, 2, 7, 1, 9] * 500
    # print(quick_sort(arr))
    # print(quick_sort(arr, "desc"))
    # print(timeit.timeit("quick_sort(arr, 'desc')", setup="from __main__ import quick_sort, arr", number=50))
    # print(standard_quick_sort(arr, 0, len(arr) - 1))
    print(timeit.timeit("standard_quick_sort(arr, 0, len(arr) - 1)", setup="from __main__ import standard_quick_sort, arr", number=50))
    print(timeit.timeit("another_standard_quick_sort(arr, 0, len(arr) - 1)", setup="from __main__ import another_standard_quick_sort, arr", number=50))
    

"""
12.55657649999921
5.761624899998424
"""
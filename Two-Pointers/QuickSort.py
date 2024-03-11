from typing import List

def QuickSort(arr: List[int], lo: int, hi: int):
    if (lo < hi):
        pivot_index = partition(arr, lo, hi)
        QuickSort(arr, lo, pivot_index-1)
        QuickSort(arr, pivot_index, hi)

    return

def partition(arr: List[int], lo: int, hi: int) -> int:
    pivot: int = arr[hi]
    leftwall: int = lo

    for i in range(lo, hi):
        elem = arr[i]
        if (elem < pivot):
            arr[i], arr[leftwall] = arr[leftwall], arr[i]
            leftwall += 1
        

    arr[leftwall], arr[hi] = arr[hi], arr[leftwall] 
    
    return leftwall
           
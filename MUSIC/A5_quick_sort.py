import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]           # last element as pivot
    smaller = [x for x in arr[:-1] if x <= pivot]
    bigger = [x for x in arr[:-1] if x > pivot]
    return quicksort(smaller) + [pivot] + quicksort(bigger)

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)   # random pivot
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    bigger = [x for x in arr if x > pivot]
    return quicksort_random(smaller) + equal + quicksort_random(bigger)

nums = list(map(int, input("Enter numbers: ").split()))
print("Normal QuickSort:", quicksort(nums))
print("Random QuickSort:", quicksort_random(nums))

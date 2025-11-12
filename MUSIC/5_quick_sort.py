import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    smaller = [x for x in arr[:-1] if x <= pivot]
    bigger = [x for x in arr[:-1] if x > pivot]
    return quicksort(smaller) + [pivot] + quicksort(bigger)

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    bigger = [x for x in arr if x > pivot]
    return quicksort_random(smaller) + equal + quicksort_random(bigger)

# ---- Change size here ----
n = int(input("Enter number of elements to generate: "))
nums = [random.randint(1, 100000) for _ in range(n)]

print(f"\nGenerated {n} random numbers!")

# ---- Deterministic QuickSort ----
start = time.time()
quicksort(nums)
end = time.time()
print("Deterministic QuickSort Time:", round((end - start)*1000, 4), "ms")

# ---- Randomized QuickSort ----
start = time.time()
quicksort_random(nums)
end = time.time()
print("Randomized QuickSort Time:", round((end - start)*1000, 4), "ms")

import random
import time

sizes = [5000,10000,25000]

def generated_array(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0,500000))

    return arr

#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                flag = True
        if not flag :
         break


#selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
         arr[i], arr[min_index] = arr[min_index], arr[i]


#insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

##### Assignment two
## PART ONE:
#heap sort
def Max_heap (arr,n,i):
    largest = i
    left = 2 * i +1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Max_heap(arr,n,largest)
def heap_sort(arr,n):
    ##build max heap // O(n)
    for i in range(n//2 -1 ,-1,-1):
        Max_heap(arr,n,i)
    ##deletion // O(n log n)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        Max_heap(arr,i,0)

#quick sort (random pivot)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]
    return partition(arr, low, high)

def quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

#merge sort
def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]

    i = 0
    j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while j < len(right):
         arr[k] = right[j]
         j += 1
         k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        merge(arr, l, m, r)

##PART TWO:
##FIRST: HYBRID MERGE SELECTION SORT ALGORITHM

def hybrid_merge_selection(arr, left , right , threshold):
    if right - left +1 <= threshold:
        sub_array = arr[left:right+1]
        selection_sort(sub_array)
        arr[left:right+1] = sub_array
        return

    if left < right:
        median = (left + right) // 2
        hybrid_merge_selection(arr, left , median , threshold)
        hybrid_merge_selection(arr, median+1 , right , threshold)
        merge(arr, left, median, right)

array = [23, 25, 4, 7, 11, 48, 3, 10, 43]
threshold = 5
print("Hybrid Merge and Selection Sort")
arr_hybrid = array.copy()
print(f"Before:", arr_hybrid)
hybrid_merge_selection(arr_hybrid, 0, len(arr_hybrid) - 1, threshold)
print(f"After:", arr_hybrid)
print()

##SECOND: KTH SMALLEST ELEMENT IN UNSORTED ARRAY
def kth_smallest(arr, low, high, k):
    if low <= high:
        pi = randomized_partition(arr, low, high)

        if pi == k:
            return arr[pi]

        elif pi > k:
            return kth_smallest(arr, low, pi - 1, k)

        else:
            return kth_smallest(arr, pi + 1, high, k)

test_arr = [7, 10, 4, 3, 20, 15]
k = 1
result = kth_smallest(test_arr.copy(), 0, len(test_arr) - 1, k-1)
print("array:", test_arr)
print(f"{k}th smallest element =", result)
print()

for size in sizes:
    arr = generated_array(size)
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()
    arr6 = arr.copy()

    start = time.time()
    bubble_sort(arr1)
    end = time.time()
    bubble_sort_time = (end - start)*1000


    start = time.time()
    selection_sort(arr2)
    end = time.time()
    selection_sort_time = (end - start) * 1000

    start = time.time()
    insertion_sort(arr3)
    end = time.time()
    insertion_sort_time = (end - start) * 1000

    start = time.time()
    heap_sort(arr4,size)
    end = time.time()
    heap_sort_time = (end - start) * 1000

    # quick sort
    start = time.time()
    quick_sort(arr5, 0, size - 1)
    end = time.time()
    quick_sort_time = (end - start) * 1000

    # merge sort
    start = time.time()
    merge_sort(arr6, 0, size - 1)
    end = time.time()
    merge_sort_time = (end - start) * 1000

##PART ONE
    print("Array size :", size)
    print("O(n^2)")
    print("bubble sort time:",bubble_sort_time,"ms")
    print("selection sort time:", selection_sort_time, "ms")
    print("insertion sort time:", insertion_sort_time, "ms")
##PART ONE ASSIGNMENT  TWO
    print("O(n log n)")
    print("Heap sort time:", heap_sort_time, "ms")
    print("Quick sort time:", quick_sort_time, "ms")
    print("Merge sort time:", merge_sort_time, "ms")
    print()




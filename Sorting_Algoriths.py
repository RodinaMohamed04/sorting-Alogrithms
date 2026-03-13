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
    for i in range(n//2,-1,-1):
        Max_heap(arr,n,i)
    ##deletion // O(n log n)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        Max_heap(arr,n,0)



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


for size in sizes:
    arr = generated_array(size)
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()

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

### assignment two
    start = time.time()
    heap_sort(arr4,size)
    end = time.time()
    heap_sort_time = (end - start) * 1000

    # quick sort
    start = time.time()
    quick_sort(arr5, 0, size - 1)
    end = time.time()
    quick_sort_time = (end - start) * 1000


    print("Array size :",size)
    print("bubble sort time:",bubble_sort_time,"ms")
    print("selection sort time:", selection_sort_time, "ms")
    print("insertion sort time:", insertion_sort_time, "ms")
    print("Heap sort time:", heap_sort_time, "ms")
    print("Quick sort time:", quick_sort_time, "ms")
    print()




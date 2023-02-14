import time

numbers = [6, 5, 3, 1, 8, 7, 2, 4]

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = int(len(list)/2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0
    # case1: left/right 아직 남아 있는 경우
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1
    # case2: left만 남아 있는 경우
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
    # case3: right만 남아 있는 경우
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1
    return merged

time_to_complete = time.time()
result = merge_sort(numbers)
print("Merge sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    tail = list[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

time_to_complete = time.time()
result = quick_sort(numbers)
print("Quick sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

time_to_complete = time.time()
result = bubble_sort(numbers)
print("Bubble sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

time_to_complete = time.time()
result = selection_sort(numbers)
print("Selection sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def insertion_sort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
            else:
                break
    return list

time_to_complete = time.time()
result = insertion_sort(numbers)
print("Insertion sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def counting_sort(list):
    count = [0] * (max(list) + 1)
    for i in range(len(list)):
        count[list[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')

time_to_complete = time.time()
result = counting_sort(numbers)
print("Counting sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)


def radix_sort(list):
    max_num = max(list)
    max_digit = len(str(max_num))
    for i in range(max_digit):
        bucket = [[] for _ in range(10)]
        for j in range(len(list)):
            bucket[list[j] // (10 ** i) % 10].append(list[j])
        list = [num for bucket in bucket for num in bucket]
    return list

time_to_complete = time.time()
result = radix_sort(numbers)
print("Radix sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def heap_sort(list):
    def heapify(list, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and list[i] < list[left]:
            largest = left
        if right < n and list[largest] < list[right]:
            largest = right
        if largest != i:
            list[i], list[largest] = list[largest], list[i]
            heapify(list, n, largest)
    n = len(list)
    for i in range(n, -1, -1):
        heapify(list, n, i)
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)
    return list

time_to_complete = time.time()
result = heap_sort(numbers)
print("Heap sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def shell_sort(list):
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap, len(list)):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap //= 2
    return list

time_to_complete = time.time()
result = shell_sort(numbers)
print("Shell sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def cocktail_sort(list):
    left = 0
    right = len(list) - 1
    while left < right:
        for i in range(left, right):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        right -= 1
        for i in range(right, left, -1):
            if list[i - 1] > list[i]:
                list[i], list[i - 1] = list[i - 1], list[i]
        left += 1
    return list

time_to_complete = time.time()
result = cocktail_sort(numbers)
print("Cocktail sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def comb_sort(list):
    gap = len(list)
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = int(float(gap) / shrink)
        swapped = False
        for i in range(len(list) - gap):
            if list[i] > list[i + gap]:
                list[i], list[i + gap] = list[i + gap], list[i]
                swapped = True
    return list

time_to_complete = time.time()
result = comb_sort(numbers)
print("Comb sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def gnome_sort(list):
    i = 1
    while i < len(list):
        if not i or list[i - 1] <= list[i]:
            i += 1
        else:
            list[i], list[i - 1] = list[i - 1], list[i]
            i -= 1
    return list

time_to_complete = time.time()
result = gnome_sort(numbers)
print("Gnome sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def bitonic_sort(list):
    def comp_and_swap(list, i, j, dire):
        if (list[i] > list[j]) == dire:
            list[i], list[j] = list[j], list[i]
    def bitonic_merge(list, low, cnt, dire):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                comp_and_swap(list, i, i + k, dire)
            bitonic_merge(list, low, k, dire)
            bitonic_merge(list, low + k, k, dire)
    def bitonic_sort(list, low, cnt, dire):
        if cnt > 1:
            k = cnt // 2
            bitonic_sort(list, low, k, True)
            bitonic_sort(list, low + k, k, False)
            bitonic_merge(list, low, cnt, dire)
    n = len(list)
    bitonic_sort(list, 0, n, True)
    return list

time_to_complete = time.time()
result = bitonic_sort(numbers)
print("Bitonic sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def pancake_sort(list):
    for i in range(len(list)):
        max_index = i
        for j in range(i + 1, len(list)):
            if list[j] > list[max_index]:
                max_index = j
        list[i], list[max_index] = list[max_index], list[i]
    return list

time_to_complete = time.time()
result = pancake_sort(numbers)
print("Pancake sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def cycle_sort(list):
    writes = 0
    for cycle_start in range(0, len(list) - 1):
        item = list[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, len(list)):
            if list[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == list[pos]:
            pos += 1
        list[pos], item = item, list[pos]
        writes += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(list)):
                if list[i] < item:
                    pos += 1
            while item == list[pos]:
                pos += 1
            list[pos], item = item, list[pos]
            writes += 1
    return list

time_to_complete = time.time()
result = cycle_sort(numbers)
print("Cycle sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def stooge_sort(list):
    def stooge_sort2(list, i, j):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
        if i + 1 >= j:
            return
        t = (j - i + 1) // 3
        stooge_sort2(list, i, j - t)
        stooge_sort2(list, i + t, j)
        stooge_sort2(list, i, j - t)
    stooge_sort2(list, 0, len(list) - 1)
    return list

time_to_complete = time.time()
result = stooge_sort(numbers)
print("Stooge sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def bogosort(list):
    import random
    while (sorted(list) != list):
        random.shuffle(list)
    return list

time_to_complete = time.time()
result = bogosort(numbers)
print("Bogosort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def odd_even_sort(list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(list) - 1, 2):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_sorted = False
        for i in range(0, len(list) - 1, 2):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                is_sorted = False
    return list

time_to_complete = time.time()
result = odd_even_sort(numbers)
print("Odd-even sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def cocktail_sort(list):
    swapped = True
    start = 0
    end = len(list)
    while (swapped == True):
        swapped = False
        for i in range(start, end - 1):
            if (list[i] > list[i + 1]):
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (list[i] > list[i + 1]):
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
        start = start + 1
    return list

time_to_complete = time.time()
result = cocktail_sort(numbers)
print("Cocktail sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def comb_sort(list):
    gap = len(list)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(list):
            if list[i] > list[i + gap]:
                list[i], list[i + gap] = list[i + gap], list[i]
                sorted = False
            i += 1
    return list

time_to_complete = time.time()
result = comb_sort(numbers)
print("Comb sort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)

def heapsort(list):
    def heapify(list, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and list[i] < list[l]:
            largest = l
        if r < n and list[largest] < list[r]:
            largest = r
        if largest != i:
            list[i], list[largest] = list[largest], list[i]
            heapify(list, n, largest)
    n = len(list)
    for i in range(n, -1, -1):
        heapify(list, n, i)
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)
    return list

time_to_complete = time.time()
result = heapsort(numbers)
print("Heapsort:",(time.time() - time_to_complete) * 1000, "ms")
print(result)
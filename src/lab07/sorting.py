def bubble_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется."""
    a = list(nums)
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n -1 - i):
            if a[j] > a[j + 1]:
                a[j],a[j+1] = a[j+1],a[j] 
                swapped = True
        if  not swapped:
            break
    return a

def selection_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется."""
    a = list(nums)
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[m]>a[j]:
                m = j
        a[i],a[m] = a[m],a[i]
    return a

def insertion_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется."""
    a = list(nums)
    for i in range(1, len(a)):
        key = a[i] # карта, которую берём
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j] # сдвиг вправо, не обмен
            j -= 1
        a[j+1] = key
    return a
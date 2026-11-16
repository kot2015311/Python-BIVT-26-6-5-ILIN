def linear_search(nums, x):
    """Индекс первого вхождения x или -1."""
    for i, v in enumerate(nums):
        if v == x:
            return i
    return -1

def binary_search(sorted_nums, x):
    """Индекс x или -1. Список ДОЛЖЕН быть отсортирован по возрастанию;
    на неотсортированном результат не определён."""
    lo, hi = 0, len(sorted_nums)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid -1
    return -1

def two_sum_brute(nums, target):
    """Пара (i, j), i < j, nums[i]+nums[j]==target, или None."""
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):   
            if nums[i] + nums[j] == target:
                return (i,j)
    return None

def two_sum_fast(nums, target):
    """То же, что two_sum_brute, но за один проход со словарём."""
    seen = {}                        # значение -> индекс
    for i, x in enumerate(nums):
        complement = target - x      # чего не хватает до target
        if complement in seen:       # O(1), хеш-таблица
            return (seen[complement], i)
        seen[x] = i                  # запомнить ПОСЛЕ проверки
    return None
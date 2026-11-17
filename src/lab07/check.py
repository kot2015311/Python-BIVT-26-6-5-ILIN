import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
 
def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
    
def check_search(trials=100):
    count = 0
    cases = []
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-110, 110) # шире диапазона -> иногда x точно нет
        cases.append((nums, x))
    # явные краевые случаи из Л9 — случайность может их не выдать
    cases += [([], 5), ([5], 5), ([5], 2), ([1,3], 2), ([1,3], 1),
              ([1,3], 3), ([1,3], 0), ([1,3], 9), ([2,2,2], 2)]

    for nums, x in cases:
        try:
            expected = nums.index(x)       # эталон
        except ValueError:
            expected = -1                 # TODO: index бросает, а мы возвращаем... что?

        got = linear_search(nums, x)
        assert got == expected, f"linear_search({nums}, {x}) = {got}, ждали {expected}"
        count += 1

        a = sorted(nums)                   # бинарному нужен отсортированный!
        i = binary_search(a, x)
        if expected != -1:                 # x есть -> любое вхождение, не первое!
            assert i != -1 and a[i] == x, f"binary_search({a}, {x}) = {i}, а x есть"
        else:
            assert i == -1, f"binary_search({a}, {x}) = {i}, а x нет"
        count += 1
    return count

def check_two_sum(trials=100):
    count = 0
    cases = [([3,3], 6), ([3], 6), ([], 0), ([1,2], 10)]   # явные случаи
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        if n >= 2 and random.random() < 0.5:
            i, j = random.sample(range(n), 2)
            target = nums[i] + nums[j]        # ответ гарантированно есть
        else:
            target = random.randint(-200, 200)
        cases.append((nums, target))
    for nums, target in cases:
        brute, fast = two_sum_brute(nums, target), two_sum_fast(nums, target)
        assert (brute is None) == (fast is None), f"разошлись на {nums}, target={target}"
        for name, p in (("brute", brute), ("fast", fast)):
            if p is not None:
                i, j = p
                assert i < j and nums[i] + nums[j] == target, f"{name}: неверная пара {p} на {nums}, target={target}"
        count += 1
    return count

if __name__ == "__main__":
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
        total += 100
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок")
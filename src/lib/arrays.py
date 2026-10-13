# 1 МИН МАКС

def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: 
        raise ValueError("Список не должен быть пустым") # Вывод ошибки при пустом списке
    max_num = nums[0] # Создание сравнимых чисел
    min_num = nums[0]
    for num in nums:
        if num > max_num: max_num = num # Проверка по числам
        if num < min_num: min_num = num
    return min_num, max_num

print('[3, -1, 5, 5, 0] -> ',min_max([3, -1, 5, 5, 0]))
print('[42] -> ',min_max([42]))
print('[-5, -2, -9] -> ',min_max([-5, -2, -9]))
print('[1.5, 2, 2.0, -3.1] -> ',min_max([1.5, 2, 2.0, -3.1]))
print('[] -> ',min_max([]))

# # 2 СОРТИРОВКА

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    result = []
    for num in nums:
        if num not in result:
            result.append(num) # Создание списка без повторяющихся чисел
    
    n = len(result)
    for i in range(n):
        min_idx = i # Берем минимальный индекс, предполагая, что это минимальное число
        for num in range(i + 1, n): # Берем число от i + 1, + 2...
            if result[num] < result[min_idx]: # Если число с индексом i + 1, + 2... < числа с минимальным индексом
                min_idx = num # Запоминаем индекс нового найденного минимума
        result[i], result[min_idx] = result[min_idx], result[i] # Меняем местами
        
    return result


print('[3, 1, 2, 1, 3] -> ',unique_sorted([3, 1, 2, 1, 3]))
print('[-1, -1, 0, 2, 2]] -> ',unique_sorted([-1, -1, 0, 2, 2]))
print('[1.0, 1, 2.5, 2.5, 0] -> ',unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print('[] -> ',unique_sorted([]))

# 3 Расплющить матрицу

def flatten(mat: list[list | tuple]) -> list:
    new_mat = [] # Список новой матрицы
    for i in mat:
        if type(i) == list or type(i) == tuple: # Проверка на тип
            for x in i:
                new_mat.append(x) # Добавление цифры в матрицу
        else:
            raise TypeError('строка не строка строк матрицы') 
    return new_mat

print('[[1,2],[3,4]] -> ',flatten([[1,2],[3,4]]))
print('[[1, 2], (3, 4, 5)] -> ',flatten([[1, 2], (3, 4, 5)]))
print('[[1], [], [2, 3]] -> ',flatten([[1], [], [2, 3]]))
print('[[1, 2], ''ab''] -> ',flatten([[1, 2], 'ab']))

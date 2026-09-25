# 1 МИН МАКС

def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0: 
        raise ValueError("Список не должен быть пустым") # Вывод ошибки при пустом списке
    max_num = nums[0] # Создание сравнимых чисел
    min_num = nums[0]
    for num in nums:
        if num > max_num: max_num = num # Проверка по числам
        if num < min_num: min_num = num
    return (min_num, max_num)

print('[3, -1, 5, 5, 0] -> ',min_max([3, -1, 5, 5, 0]))
print('[42] -> ',min_max([42]))
print('[-5, -2, -9] -> ',min_max([-5, -2, -9]))
print('[1.5, 2, 2.0, -3.1] -> ',min_max([1.5, 2, 2.0, -3.1]))
print('[] -> ',min_max([]))

# # 2 СОРТИРОВКА

# def unique_sorted(nums: list[float | int]) -> list[float | int]:
#     snums = [] # Пустой список для сортировки чисел
#     for i in range(len(nums)):
#         if nums[i]<=nums[i]: # Проверка чисел и добавление их в список
#             if nums[i] not in snums:
#                 snums.append(nums[i])
#             else:
#                 continue # Если число есть в списке
#     return sorted(snums)

# print('[3, 1, 2, 1, 3] -> ',unique_sorted([3, 1, 2, 1, 3]))
# print('[-1, -1, 0, 2, 2]] -> ',unique_sorted([-1, -1, 0, 2, 2]))
# print('[1.0, 1, 2.5, 2.5, 0] -> ',unique_sorted([1.0, 1, 2.5, 2.5, 0]))
# print('[] -> ',[])

# # 3 Расплющить матрицу

# def flatten(mat: list[list | tuple]) -> list:
#     new_mat = [] # Список новой матрицы
#     for i in mat:
#         if type(i) == list or type(i) == tuple: # Проверка на тип
#             for x in i:
#                 new_mat.append(x) # Добавление цифры в матрицу
#         else:
#             raise TypeError('строка не строка строк матрицы') 
#     return new_mat

# print('[[1,2],[3,4]] -> ',flatten([[1,2],[3,4]]))
# print('[[1, 2], (3, 4, 5)] -> ',flatten([[1, 2], (3, 4, 5)]))
# print('[[1], [], [2, 3]] -> ',flatten([[1], [], [2, 3]]))
# print('[[1, 2], ''ab''] -> ',flatten([[1, 2], 'ab']))

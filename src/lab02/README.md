# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

## Задание 1 - min_max
```py
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
```
![alt text](../../images/lab02/01.png)

## Задание 2 - unique_sorted
```py

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
```
![alt text](../../images/lab02/02.png)

## Задание 3 - flatten
```py

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
```
![alt text](../../images/lab02/03.png)

## Заданиие 4 - transpose
```py
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat: # Обрабатываем пустую матрицу
        return []   
    
    cols_count = len(mat[0])  # Берем длину первого столбца за основу
    for row in mat:
        if len(row) != cols_count:
            raise ValueError("рваная матрица") # Проверяем матрицу на "рваность"
    
    t_mat = [] # Создаем новую пустую матрицу  
    for col in range(cols_count): # Проходимся по столбцам исходной матрицы
        new_row = []
        for row in range(len(mat)): # Проходимся по строкам исходной матрицы
            new_row.append(mat[row][col])
        t_mat.append(new_row)

    return t_mat

print('[[1, 2, 3]] -> ',transpose([[1, 2, 3]]))
print('[[1], [2], [3]] -> ',transpose([[1], [2], [3]]))
print('[[1, 2], [3, 4]] -> ',transpose([[1, 2], [3, 4]]))
print('[] -> ',transpose([]))
print('[[1, 2], [3]] -> ',transpose([[1, 2], [3]]))
```
![alt text](../../images/lab02/04.png)

# Задание 5 - row_sums
```py
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    cols_count = len(mat[0])  
    for row in mat:
        if len(row) != cols_count:
            raise ValueError("рваная матрица") # Проверка на рванасть
    sum_mat = []
    for row in mat:
        sum_mat.append(sum(row)) # Сумма строк
    return sum_mat

print('[[1,2,3],[4,5,6]] -> ',row_sums([[1,2,3],[4,5,6]]))
print('[[-1, 1], [10, -10]] -> ',row_sums([[-1, 1], [10, -10]]))
print('[[0, 0], [0, 0]] -> ',row_sums([[0, 0], [0, 0]]))
print('[[1,2],[3]] -> ',row_sums([[1,2],[3]]))
```
![alt text](../../images/lab02/05.png)

# Задание 6 - col_sums
```py
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    cols_count = len(mat[0])  
    for row in mat:
        if len(row) != cols_count:
            raise ValueError("рваная матрица") # Проверка на рванасть
    col = zip(*mat) # Распаковка столбцов по 2 числа в один кортеж
    new_sum = [] # Список сумм
    for i in col:
        new_sum.append(sum(i)) # Преобразование кортежа в список и его суммирование
    return new_sum

print('[[1,2,3],[4,5,6]] -> ',col_sums([[1, 2, 3], [4, 5, 6]]))
print('[[-1, 1], [10, -10]] -> ',col_sums([[-1, 1], [10, -10]]))
print('[[0, 0], [0, 0]] -> ',col_sums([[0, 0], [0, 0]]))
print('[[1,2],[3]] -> ',col_sums([[1, 2], [3]]))
```
![alt text](../../images/lab02/06.png)

# Задание 7 Форма
```py
def format_record(rec: tuple[str, str, float]) -> str:
    
    if type(rec) is not tuple:
        raise TypeError("Входные данные должны быть кортежем")# Проверка, что входные данные кортеж
    
    
    if len(rec) != 3:
        raise ValueError("Неточный формат входных данных")# Проверка длины кортежа
    
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    
    # Проверки типов
    if type(fio) != str:
        raise TypeError("ФИО должно быть строкой")
    
    if type(group) != str:
        raise TypeError("Группа должна быть строкой")
    
    if type(gpa) not in (int, float):
        raise TypeError("GPA должен быть числом")
    
    gpa = round(gpa, 2)
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("GPA должен быть в диапазоне от 0.0 до 5.0")# Проверка диапазона GPA
    
    fio = fio.split()
    if len(fio) not in (2, 3):
        raise ValueError("Неверный ввод ФИО")
    
    
    if not group.strip():
        raise ValueError("Группа должна быть написана")# Проверка группы
    
    # Формирование ФИО с инициалами
    
    f_name = fio[0].capitalize() # Фамилия с большой буквы
    initials = ''
    for i in fio[1:]:
        initials+=i[0].upper()+'.'
    fio = f_name + ' ' + initials
    return f"{fio}, гр. {group.strip()}, GPA {gpa:.2f}"

print('("Иванов Иван Иванович", "BIVT-25", 4.6) -> ', format_record(("   Иванов Иван Иванович", "    BIVT-25", 4.6)))
print('("Петров Пётр", "IKBO-12", 5.0) -> ', format_record(("   Петров Пётр", "IKBO-12", 5.0)))
print('("Петров Пётр Петрович", "IKBO-12", 5.0) -> ', format_record(("Петров Пётр Петрович", "IKBO-12   ", 5.0)))
print('("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> ', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print('("Иванов Иван", "BIVT-25", 5) -> ', format_record(("Иванов Иван", "BIVT-25", 5))) 
```
![alt text](../../images/lab02/07.png)
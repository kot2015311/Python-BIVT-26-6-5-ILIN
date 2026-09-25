# 1 Транспортировка матрицы

def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat: # Обрабатываем пустую матрицу
        return []   
    
    cols_count = len(mat[0])  # Берем длину первой строки за основу
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

# 2 Сумма по каждой строке

def row_sums(mat: list[list[float | int]]) -> list[float]:
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

# 3 Сумма по каждому столбцу

def col_sums(mat: list[list[float | int]]) -> list[float]:
    cols_count = len(mat[0])  
    for row in mat:
        if len(row) != cols_count:
            raise ValueError("рваная матрица") # Проверка на рванасть
    col = zip(*mat) # Распаковка столбцов по 2 числа вв один кортеж
    new_sum = [] # Список сумм
    for i in col:
        new_sum.append(sum(list(i))) # Преобразование кортежа в список и его суммирование
    return new_sum

print('[[1,2],[3]] -> ',col_sums([[1, 2, 3], [4, 5, 6]]))
print('[[-1, 1], [10, -10]] -> ',col_sums([[-1, 1], [10, -10]]))
print('[[0, 0], [0, 0]] -> ',col_sums([[0, 0], [0, 0]]))
print('[[1,2],[3]] -> ',col_sums([[1, 2], [3]]))

def transpose(mat: list[list[float | int]]) -> list[list]:
    
    if len(mat) == 0:
        return []
    count = len(mat[0])
    for n in mat:
        if len(n) != count:
            raise ValueError('рваная матрица')
    
    return [list(row) for row in zip(*mat)]

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

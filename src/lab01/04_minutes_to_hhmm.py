min = int(input('Введите минуты: '))
hours = f'{min//60}:{min%60:02d}'

print(f'Минуты: {min}')
print(hours)
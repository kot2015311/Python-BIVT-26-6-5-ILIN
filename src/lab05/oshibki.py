"""ЛР5: демонстрация ошибок — какие файлы функции не принимают и что они говорят."""
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

ERR = "data/samples/errors"   # файлы с ошибками
OUT = "data/out/oshibki"      # сюда ничего не запишется: все вызовы падают раньше

# (функция, входной файл, выходной файл)
cases = [
    (json_to_csv, "data/samples/nope.json", f"{OUT}/x.csv"),        # файла нет
    (csv_to_json, f"{ERR}/people.txt", f"{OUT}/x.json"),            # вход не .csv
    (json_to_csv, "data/samples/people.json", f"{OUT}/x.txt"),      # выход не .csv
    (json_to_csv, f"{ERR}/empty.json", f"{OUT}/x.csv"),             # []
    (json_to_csv, f"{ERR}/not_dicts.json", f"{OUT}/x.csv"),         # в списке не только словари
    (json_to_csv, f"{ERR}/broken.json", f"{OUT}/x.csv"),            # битый JSON
    (csv_to_json, f"{ERR}/empty.csv", f"{OUT}/x.json"),             # пустой файл
    (csv_to_json, f"{ERR}/header_only.csv", f"{OUT}/x.json"),       # только заголовок
    (csv_to_json, f"{ERR}/ragged.csv", f"{OUT}/x.json"),            # лишнее значение в строке
    (csv_to_xlsx, f"{ERR}/ragged.csv", f"{OUT}/x.xlsx"),            # то же для XLSX
]

for func, src, dst in cases:
    try:
        func(src, dst)
        print(f"{func.__name__}({src}) — ошибки нет?!")
    except (FileNotFoundError, ValueError) as e:
        # type(e).__name__ — имя класса ошибки, например "ValueError"
        print(f"{func.__name__}({src.split('/')[-1]}, {dst.split('/')[-1]}) -> {type(e).__name__}: {e}")

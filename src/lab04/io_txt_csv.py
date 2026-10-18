# 1
from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает его содержимое одной строкой.

    Для другой кодировки можно передать, например, encoding="cp1251".
    """
    p = Path(path) # превращаем путь в объект Path, чтобы строка и path работали одинаково.
    return p.read_text(encoding=encoding)


# 2


def write_csv(rows: list[tuple | list], path: str | Path,header: tuple[str, ...] | None = None) -> None:
    """
    Записывает строки в CSV-файл с разделителем запятая.
    """
    
    rows = list(rows)
    p = Path(path) # превращаем путь в объект Path, чтобы строка и path работали одинаково.
    
    if rows: # если есть непустая строка
        len_r = len(rows[0]) # длина первой строки за основу
        for i, row in enumerate(rows): # enumerate даёт пару: номер строки i (с нуля) и саму строку row. Номер нужен, чтобы в сообщении об ошибке было понятно, где проблема.
            if len(row) != len_r:
                raise ValueError(
                    f"Строка {i} имеет длину {len(row)}, ожидалась {len_r}"
                )
    
    ensure_parent_dir(path)
    
    with p.open("w", newline="", encoding="utf-8") as f: # открываем файл на запись и стираем содержимое.
        w = csv.writer(f) # превращение строки в строку csv + ' , 
        if header is not None: # именно с None, потому что пустая строка тоже значение
            w.writerow(header)
        for r in rows:
            w.writerow(r)
            
def ensure_parent_dir(path: str | Path) -> None:
    """
    Создаёт родительские папки для файла, если их ещё нет.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
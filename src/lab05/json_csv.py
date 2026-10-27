"""ЛР5, задание A: конвертация JSON <-> CSV."""
import csv                                  # стандартный модуль для работы с CSV
import json                                 # стандартный модуль для работы с JSON
from pathlib import Path                    # удобная работа с путями к файлам

from src.lib.io_helpers import check_path           # проверка расширения и наличия файла
from src.lab04.io_txt_csv import ensure_parent_dir  # создание папок из ЛР4


def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    """
    Преобразует JSON-файл (список словарей) в CSV.
    Колонки идут в порядке ключей первого объекта; если в следующих объектах
    есть новые ключи, они добавляются в конец. Отсутствующие поля — пустые строки.
    Кодировка UTF-8.
    """
    # Проверяем оба пути: вход должен быть .json и существовать, выход — .csv
    src = check_path(json_path, ".json", must_exist=True)
    dst = check_path(csv_path, ".csv", must_exist=False)

    # json.load читает файл и превращает JSON в объекты Python: [...] -> list, {...} -> dict
    # Если JSON битый, будет json.JSONDecodeError — это подкласс ValueError
    with src.open(encoding="utf-8") as f:
        data = json.load(f)

    # Нужен непустой список
    if type(data) != list or len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    # Каждый элемент списка — одна строка таблицы, поэтому он должен быть словарём
    for item in data:
        if type(item) != dict:
            raise ValueError("В JSON-списке должны быть только словари")

    # Собираем заголовок: все ключи по порядку появления, без повторов
    fieldnames = []
    for item in data:
        for key in item:
            if key not in fieldnames:
                fieldnames.append(key)

    # Если все словари пустые ({}), колонок нет — таблицу не построить
    if len(fieldnames) == 0:
        raise ValueError("В объектах JSON нет ни одного поля")

    # Вложенные списки и словари записываем JSON-строкой, чтобы не потерять данные
    rows = []
    for item in data:
        row = {}
        for key, value in item.items():
            if type(value) in (list, dict):
                value = json.dumps(value, ensure_ascii=False)
            row[key] = value
        rows.append(row)

    # Создаём папку для файла, если её ещё нет
    ensure_parent_dir(dst)
    with dst.open("w", newline="", encoding="utf-8") as f:
        # DictWriter пишет словари; restval="" — чем заполнить поле, которого нет в словаре
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()        # первая строка — заголовок
        writer.writerows(rows)      # остальные строки — данные


def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Первая строка CSV — заголовок (обязателен), значения сохраняются как строки.
    Пишется через json.dump(..., ensure_ascii=False, indent=2).
    """
    # Проверяем оба пути: вход должен быть .csv и существовать, выход — .json
    src = check_path(csv_path, ".csv", must_exist=True)
    dst = check_path(json_path, ".json", must_exist=False)

    # utf-8-sig — та же UTF-8, но отрезает метку BOM, которую ставит Excel
    with src.open(encoding="utf-8-sig", newline="") as f:
        # DictReader берёт первую строку как заголовок и отдаёт остальные строки словарями
        reader = csv.DictReader(f)

        # fieldnames — это заголовок: у пустого файла там None, а если первая строка пустая — []
        header = reader.fieldnames
        # not header ловит оба случая: и None, и пустой список считаются ложью
        if not header:
            raise ValueError("Пустой CSV: нет заголовка")

        # Пустое имя колонки (например, "name,,city") — заголовок испорчен
        for name in header:
            if name.strip() == "":
                raise ValueError("В заголовке CSV есть пустое имя колонки")

        # Повторяющиеся имена: в словаре второе значение затёрло бы первое
        if len(set(header)) != len(header):
            raise ValueError("В заголовке CSV повторяются имена колонок")

        rows = []
        for row in reader:
            # Лишние значения DictReader складывает под ключ None
            if None in row:
                raise ValueError(f"Строка {reader.line_num}: значений больше, чем колонок")
            # Недостающие значения DictReader заполняет None — меняем на пустую строку
            for key in row:
                if row[key] is None:
                    row[key] = ""
            rows.append(row)

    # Заголовок есть, а данных нет — конвертировать нечего
    if len(rows) == 0:
        raise ValueError("Пустой CSV: есть только заголовок")

    ensure_parent_dir(dst)
    with dst.open("w", encoding="utf-8") as f:
        # ensure_ascii=False — русские буквы как есть
        # indent=2 — каждый ключ с новой строки с отступом в 2 пробела
        json.dump(rows, f, ensure_ascii=False, indent=2)

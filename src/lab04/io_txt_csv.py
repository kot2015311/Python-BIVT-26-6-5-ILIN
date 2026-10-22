"""ЛР4, задание A: чтение текста и запись CSV."""
import csv                                  # стандартный модуль для работы с CSV
from pathlib import Path                    # удобная работа с путями к файлам
from typing import Iterable, Sequence       # типы: Iterable — любой итерируемый объект, Sequence — список/кортеж


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские папки для файла, если их нет."""
    # Path(path).parent — папка, в которой лежит файл
    # mkdir(parents=True) — создать всю цепочку папок, если её нет
    # exist_ok=True — не падать, если папка уже существует
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает его содержимое одной строкой.
    FileNotFoundError и UnicodeDecodeError не перехватываются, пусть всплывают.
    Другую кодировку можно указать явно, например: encoding="cp1251".
    """
    # Path(path) — превращает строку или Path в объект Path
    # read_text(encoding=...) — открывает файл, читает всё содержимое и закрывает его
    return Path(path).read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Создаёт или перезаписывает CSV-файл (разделитель — запятая).
    rows   — строки данных; все строки должны иметь одинаковую длину.
    header — необязательный заголовок, пишется первой строкой.
    Если rows пуст и header=None, создаётся пустой файл.
    """
    # Превращаем rows в список списков: нужно проверить длины и пройти по данным дважды
    rows = [list(row) for row in rows]

    if rows:
        # Запоминаем длину первой строки как эталон
        width = len(rows[0])
        for row in rows:
            # Если длина строки не совпадает с эталоном — останавливаемся с понятной ошибкой
            if len(row) != width:
                raise ValueError("Все строки CSV должны иметь одинаковую длину.")
        # Заголовок тоже должен совпадать по длине со строками данных
        if header is not None and len(header) != width:
            raise ValueError("Длина заголовка не совпадает с длиной строк.")

    # Создаём папку для файла, если её ещё нет
    ensure_parent_dir(path)
    # newline="" — отключает автоматическую замену перевода строки;
    with Path(path).open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Если заголовок задан — пишем его первой строкой
        if header is not None:
            writer.writerow(header)
        # writerows записывает все строки данных по очереди
        writer.writerows(rows)


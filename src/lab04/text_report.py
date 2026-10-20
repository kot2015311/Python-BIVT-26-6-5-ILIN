# Импортируем normalize и tokenize из ЛР3 — там уже реализованы правила casefold/ё→е/пробелы и regex-токенизация.
from src.lib.text import normalize, tokenize, top_n, count_freq
# read_text и write_csv — наши утилиты из задания A (файловый слой отдельно от логики).
from src.lab04.io_txt_csv import read_text, write_csv
# Path — чтобы путь можно было принимать и строкой, и объектом Path.
from pathlib import Path
# argparse — разбор аргументов командной строки.
import argparse
# sys — для sys.exit(1) и sys.stderr при ошибках.
import sys


# --- Логика (без I/O) -------------------------------------------------------

def read_and_tokenize(path: str | Path, encoding: str = "utf-8") -> list[str]:
    """
    Читает файл и возвращает список токенов (уже нормализованных).

    Это объединение трёх шагов: read_text → normalize → tokenize.
    Именно это и должна была делать твоя text_norm, но с чтением файла.
    """
    # 1. Читаем текст файла в нужной кодировке (UTF-8 по умолчанию).
    text = read_text(path, encoding=encoding)
    # 2. Приводим к нижнему регистру, ё→е, заменяем \t\r\n, схлопываем пробелы.
    normalized = normalize(text)
    # 3. Режем на токены по шаблону \w+(?:-\w+)*.
    tokens = tokenize(normalized)
    # 4. Возвращаем список строк.
    return tokens


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """
    Возвращает ВСЕ пары (слово, частота), отсортированные:
    сначала по count, при равенстве — по word

    Важно: возвращаем все пары, а не только топ-5,
    потому что CSV-отчёт должен содержать полный список.
    """
    # Превращаем dict в список пар, чтобы можно было сортировать.
    items = list(freq.items())
    # Ключ сортировки: (-count, word).
    #   -count → по убыванию счёта (минус вместо reverse=True, чтобы
    #            при равных счётах слово всё равно шло по возрастанию);
    #   word   → по возрастанию слова.
    items.sort(key=lambda pair: (-pair[1], pair[0]))
    # Возвращаем готовый список.
    return items



def text_report(input_path: str | Path,
                output_path: str | Path,
                encoding: str = "utf-8") -> None:
    """Читает один файл, пишет report.csv и печатает статистику."""
    # 1. Получаем токены (чтение + нормализация + токенизация).
    tokens = read_and_tokenize(input_path, encoding=encoding)
    # 2. Считаем частоты: dict[str, int].
    freq = count_freq(tokens)
    # 3. Сортируем все пары по правилу count , word
    rows = sorted_word_counts(freq)

    # 4. Пишем CSV. Даже если rows == [] — заголовок всё равно будет
    #    Политика «пустой вход - только заголовок» зафиксирована в README
    write_csv(rows, output_path, header=("word", "count"))

    # 5. Печатаем краткое резюме.
    print(f"Всего слов: {len(tokens)}")          # сумма всех частот == len(tokens)
    print(f"Уникальных слов: {len(freq)}")       # сколько разных слов
    print("Топ-5:")
    # top_n уже сортирует count ↓, word ↑ и обрезает до n (по умолчанию 5).
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")
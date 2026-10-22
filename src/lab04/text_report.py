import argparse                                     # Для приёма аргументов из консоли (--in, --out, --encoding)
import sys                                          # Для sys.exit() и вывода ошибок в sys.stderr
from pathlib import Path                            

from src.lib.text import normalize, tokenize, count_freq, top_n   
from src.lab04.io_txt_csv import read_text, write_csv             


def read_and_tokenize(file_path: str | Path, encoding: str) -> list[str]:
    """Читает файл и возвращает список нормализованных слов (токенов)."""
    text = read_text(file_path, encoding=encoding)  
    norm_text = normalize(text)                     
    tokens = tokenize(norm_text)                   
    return tokens                                   

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует словарь частот: count , при равенстве word ."""
    items = freq.items() # Получаем пары (слово, частота) из словаря
    # Сортируем по ключу: сначала -частота (минус для убывания), потом само слово (по алфавиту)
    return sorted(items, key=lambda pair: (-pair[1], pair[0]))


def main() -> None:
    """Главная функция: разбирает аргументы, запускает логику, пишет отчёт."""
    # 1. Настраиваем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description="Частотный отчёт по словам (ЛР4)") #ArgumentParser создаёт «описание» программы, какие аргументы она принимает.
    
    # Аргумент --in: путь к входному файлу. Если не указан, берется data/lab04/input.txt
    parser.add_argument("--in", dest="input_file", default="data/lab04/input.txt", help="Путь к входному файлу")
    
    # Аргумент --out: путь к выходному CSV. По умолчанию data/report.csv
    parser.add_argument("--out", dest="output_file", default="data/report.csv", help="Путь к выходному CSV")
    
    # Аргумент --encoding: кодировка файла. По умолчанию utf-8
    parser.add_argument("--encoding", default="utf-8", help="Кодировка файла (например, cp1251)")
    
    # Читаем аргументы, которые ввел пользователь в консоли
    args = parser.parse_args()

    # 2. Блок try-except для обработки ошибок чтения файла
    try:
        # Получаем список слов из файла (вызываем нашу функцию)
        tokens = read_and_tokenize(args.input_file, encoding=args.encoding)
    except FileNotFoundError as e:
        # Если файл не найден, печатаем ошибку в поток ошибок (stderr) и выходим
        print(f"Ошибка: файл не найден: {e.filename}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        # Если файл не читается в указанной кодировке, подсказываем пользователю
        print(f"Ошибка кодировки. Попробуйте добавить --encoding cp1251", file=sys.stderr)
        sys.exit(1)

    # 3. Считаем частоты слов
    freq = count_freq(tokens)  # Получаем словарь вида {"привет": 2, "мир": 1}

    # 4. Сортируем словарь по правилу: count , word 
    sorted_rows = sorted_word_counts(freq)

    # 5. Сохраняем результат в CSV-файл
    # Передаем заголовок ("word", "count"). Если слов нет, файл будет содержать только заголовок.
    write_csv(sorted_rows, args.output_file, header=("word", "count"))

    # 6. Печатаем краткое резюме в консоль
    print(f"Всего слов: {len(tokens)}")            # Общее количество токенов (сумма всех частот)
    print(f"Уникальных слов: {len(freq)}")         # Количество ключей в словаре freq
    print("Топ-5:")                                # Заголовок для списка
    
    # Получаем топ-5 слов (функция из ЛР3) и выводим их в формате слово:кол-во
    for word, cnt in top_n(freq, n=5):
        print(f"{word}:{cnt}")


# Эта конструкция гарантирует, что main() запустится только при прямом запуске скрипта
if __name__ == "__main__":
    main()  # Вызываем главную функцию
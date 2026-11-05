import argparse
from pathlib import Path

# ВАЖНО: Проверь путь к файлу, где лежат эти функции! 
# Если файл называется иначе (например, src.lab03.text_processing), измени импорт.
from src.lib.text import normalize, tokenize, count_freq, top_n 

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6 (работа с текстом)")
    subparsers = parser.add_subparsers(dest="command", title="Доступные команды")

    # --- Подкоманда cat ---
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", dest="number", action="store_true", help="Нумеровать строки") # -n для нумерации строк, action="store_true" означает, что если флаг указан, то number будет True, иначе False

    # --- Подкоманда stats ---
    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов (по умолчанию 5)")

    args = parser.parse_args()

    # Если подкоманда не указана
    if args.command is None:
        parser.error("не указана подкоманда: cat | stats")

    try:
        if args.command == "cat":
            with open(args.input, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, start=1):
                    if args.number:
                        print(f"{i:4}: {line}", end="") # i:4 - ширина поля 4 символа, выравнивание по правому краю
                    else:
                        print(line, end="") # end="" - чтобы не добавлять лишний перенос строки, т.к. line уже содержит \n
                        
        elif args.command == "stats":
            # Читаем файл
            text = Path(args.input).read_text(encoding="utf-8")
            
            # 1. Нормализация (приводим к нижнему регистру, чистим пробелы)
            clean_text = normalize(text)
            
            # 2. Токенизация (разбиваем на слова)
            words = tokenize(clean_text)
            
            # 3. Подсчет частот (возвращает словарь)
            freqs = count_freq(words)
            
            # 4. Топ-N слов (возвращает список кортежей)
            top_words = top_n(freqs, args.top)
            
            print(f"Топ {args.top} слов:")
            for word, count in top_words:
                print(f"{word}: {count}")

    except FileNotFoundError:
        parser.error(f"файл не найден: {args.input}")
    except Exception as e:
        # Ловим остальные ошибки (например, если вместо текста передали бинарный файл)
        parser.error(str(e))

if __name__ == "__main__":
    main()
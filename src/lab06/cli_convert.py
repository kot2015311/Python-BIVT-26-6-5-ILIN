# Функция конвертации
import argparse
from src.lab05.csv_xlsx import csv_to_xlsx
from src.lab05.json_csv import json_to_csv
from src.lab05.json_csv import csv_to_json

def main():
    # Лицо парсера
    parser = argparse.ArgumentParser(description="Конвертер данных (JSON, CSV, XLSX)")
    # Команды 
    subparse = parser.add_subparsers(dest='command', title="Доступные команды")

    # Расписываем что должен делать
    json2csv = subparse.add_parser('json2csv', help="Конвертировать JSON в CSV")
    json2csv.add_argument('--in', dest='input', required=True, help="Путь к исходному JSON файлу")
    json2csv.add_argument('--out', dest='output', required=True, help="Путь для сохранения CSV файла")

    csv2json = subparse.add_parser('csv2json', help="Конвертировать CSV в JSON")
    csv2json.add_argument('--in', dest='input', required=True, help="Путь к исходному CSV файлу")
    csv2json.add_argument('--out', dest='output', required=True, help="Путь для сохранения JSON файла")

    csv2xlsx = subparse.add_parser('csv2xlsx', help="Конвертировать CSV в XLSX (Excel)")
    csv2xlsx.add_argument('--in', dest='input', required=True, help="Путь к исходному CSV файлу")
    csv2xlsx.add_argument('--out', dest='output', required=True, help="Путь для сохранения XLSX файла")

    args = parser.parse_args()

    # Если подкоманда не указана — подсказываем пользователю и выходим
    if args.command is None:
        parser.error("не указана подкоманда: json2csv | csv2json | csv2xlsx")

    # Вызываем нужную функцию из ЛР5, передавая пути (args.input, args.output)
    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError as e:
        parser.error(f"файл не найден: {e}")
    except (OSError, ValueError) as e:
        parser.error(str(e))
    else:
        print(f"OK: {args.command}: {args.input} -> {args.output}")

if __name__=='__main__':
    main()
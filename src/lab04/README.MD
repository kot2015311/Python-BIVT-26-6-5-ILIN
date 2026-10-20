# ЛР4 — Текстовые отчёты и CSV (I/O + статистика)

ЦЕЛЬ РАБОТЫ:
Освоить чтение/запись файлов и CSV на Python, научиться разделять
файловый слой и логику, применять функции из ЛР3 (normalize,
tokenize, count_freq, top_n) к реальным файлам.

## Задание А — модуль `src/lab04/io_txt_csv.py`

Три «кирпича»: чтение текста, запись CSV, создание папок.
Всё с докстрингами и аннотациями типов.

### Read_text

Открывает файл в заданной кодировке и возвращает содержимое одной
строкой. Ошибки `FileNotFoundError` и `UnicodeDecodeError` не
перехватываются — пусть вызывающий решает. Для нестандартной
кодировки её передают явно: `read_text("f.txt", encoding="cp1251")`.

```python
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)
```

Вывод

![alt text](../../images/lab04/read_text.png)

### Ensure_parent_dir

Создаёт родительские папки для файла (если их нет). Вызывается
изнутри `write_csv`, чтобы не падало `open()`.

```python
def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
```

Вывод

![alt text](../../images/lab04/ensure_parent_dir.png)

### Write_csv

Пишет список строк в CSV через `csv.writer` с разделителем «,»,
кодировка UTF-8, файл перезаписывается. Если передан `header` —
пишется первой строкой. Проверяет **одинаковую ширину** всех
строк (эталон — длина `header`, если он есть, иначе — первой
строки). При нарушении — `ValueError`.

```python
def write_csv(rows, path, header=None) -> None:
    rows = list(rows)
    p = Path(path)
    if header is not None:
        length = len(header)
    elif rows:
        length = len(rows[0])
    else:
        length = None
    if length is not None:
        for i, row in enumerate(rows):
            if len(row) != length:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, "
                                 f"ожидалась {length}")
    ensure_parent_dir(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```

Вывод

![alt text](../../images/lab04/write_csv.png)

### Проверка через assert

```python
from src.lab04.io_txt_csv import read_text, write_csv

# чтение пустого файла → ""
Path("data/lab04/empty.txt").write_text("", encoding="utf-8")
assert read_text("data/lab04/empty.txt") == ""

# обычная запись с заголовком
write_csv([("test", 3)], "data/lab04/check.csv", header=("word", "count"))
assert Path("data/lab04/check.csv").read_text(encoding="utf-8") == \
    "word,count\ntest,3\n"

# пустой rows + header → только заголовок
write_csv([], "data/lab04/check.csv", header=("word", "count"))
assert Path("data/lab04/check.csv").read_text(encoding="utf-8") == \
    "word,count\n"

# пустой rows + header=None → пустой файл
write_csv([], "data/lab04/check.csv")
assert Path("data/lab04/check.csv").read_text(encoding="utf-8") == ""

# разная длина строк → ValueError
try:
    write_csv([("a", 1), ("b", 2, 3)], "data/lab04/check.csv")
    raise AssertionError("ожидали ValueError")
except ValueError:
    pass

# несовпадение ширины с header → ValueError
try:
    write_csv([("a", "b")], "data/lab04/check.csv", header=("x", "y", "z"))
    raise AssertionError("ожидали ValueError")
except ValueError:
    pass

print("Все проверки пройдены!")
```

Вывод

![alt text](../../images/lab04/proverka_io.png)

## Задание В — скрипт `src/lab04/text_report.py`

Скрипт:
1. читает `data/lab04/input.txt` (путь можно задать флагом `--in`);
2. нормализует и токенизирует (функции из ЛР3);
3. считает частоты и пишет `report.csv` с колонками `word,count`,
   отсортированный по `count ↓, word ↑`;
4. печатает в консоль: всего слов, уникальных слов, топ-5.

Код функции одного файла:

```python
def text_report(input_path, output_path, encoding="utf-8") -> None:
    tokens = read_and_tokenize(input_path, encoding=encoding)
    freq = count_freq(tokens)
    rows = sorted_word_counts(freq)
    write_csv(rows, output_path, header=("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")
```

Пример запуска:

```bash
python -m src.lab04.text_report
python -m src.lab04.text_report --in data/lab04/input.txt \
                                --out data/lab04/report.csv
```

Пример `report.csv`:

```
word,count
привет,2
мир,1
```

Вывод

![alt text](../../images/lab04/report_one.png)

## Тест-кейсы A / B / C

### A. Обычный вход

`data/lab04/input.txt`:

```
Привет, мир! Привет!!!
```

Запуск:

```bash
python -m src.lab04.text_report
```

Ожидание в консоли:

```
Всего слов: 3
Уникальных слов: 2
Топ-5:
привет:2
мир:1
```

`report.csv`:

```
word,count
привет,2
мир,1
```

### B. Пустой вход

`data/lab04/input.txt` пустой → `report.csv` содержит **только
заголовок** `word,count` (такая политика выбрана осознанно — так
файл удобнее парсить; альтернатива «пустой файл» отвергнута).

### C. Кодировка cp1251

Создаём файл в cp1251:

```python
open("data/lab04/input.txt", "w", encoding="cp1251").write("Привет")
```

Запуск:

```bash
python -m src.lab04.text_report --encoding cp1251
```

Ожидание: чтение успешно, `report.csv` = `word,count / привет,1`.
Если забыть `--encoding`, скрипт печатает в stderr подсказку
«Попробуйте --encoding cp1251» и завершается с кодом 1.

Вывод

![alt text](../../images/lab04/report_cp1251.png)

## Задание ★ — несколько файлов

Флаг `--in` принимает несколько путей. Флаги `--per-file` и
`--total` включают многфайловый режим и указываются **вместе**:

* `--per-file` — CSV со столбцами `file,word,count`, сортировка
  `file ↑, count ↓, word ↑`;
* `--total` — сводный CSV `word,count`, сортировка `count ↓, word ↑`.

Запуск:

```bash
python -m src.lab04.text_report \
    --in data/lab04/a.txt data/lab04/b.txt \
    --per-file data/lab04/report_per_file.csv \
    --total    data/lab04/report_total.csv
```

Вход:

* `a.txt`: `Привет мир`
* `b.txt`: `Привет, привет!`

`report_per_file.csv`:

```
file,word,count
a.txt,мир,1
a.txt,привет,1
b.txt,привет,2
```

`report_total.csv`:

```
word,count
привет,3
мир,1
```

Вывод

![alt text](../../images/lab04/report_multi.png)

## Политика по кодировкам и ошибкам

* **По умолчанию UTF-8.** Для другой кодировки — флаг
  `--encoding cp1251` (или `read_text(path, encoding="cp1251")`).
* **Файл не найден:** печатаем `Ошибка: файл не найден: <path>`
  в `stderr`, код возврата 1.
* **Ошибка декодирования:** печатаем подсказку про `--encoding`,
  код возврата 1.
* **Пустой вход:** `report.csv` содержит только заголовок.
* **Большие файлы:** по ТЗ читаем целиком; в реальном проекте
  стоит читать построчно — это отмечено в коде `read_text`.

## Структура проекта

```
src/
  lab04/
    __init__.py
    io_txt_csv.py       # Задание A (I/O слой)
    text_report.py      # Задание B + ★ (логика + CLI)
  lib/
    text.py             # функции из ЛР3
data/
  lab04/
    input.txt
    a.txt
    b.txt
    report.csv
    report_per_file.csv
    report_total.csv
images/
  lab04/
    read_text.png
    write_csv.png
    ...
```
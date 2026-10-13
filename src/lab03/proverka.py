from src.lib.text import count_freq, normalize, tokenize, top_n

assert normalize("ПрИвЕт\nМИр\t") == "привет мир", "Ошибка в normalize (регистр/пробелы)"
assert normalize("ёжик, Ёлка") == "ежик, елка", "Ошибка в normalize (замена ё/е)"
assert normalize("Hello\r\nWorld") == "hello world", "Ошибка в normalize (управляющие символы)"
assert normalize("  двойные   пробелы  ") == "двойные пробелы", "Ошибка в normalize (схлопывание пробелов)"

assert tokenize("привет мир") == ["привет", "мир"], "Ошибка в tokenize (обычные слова)"
assert tokenize("hello,world!!!") == ["hello", "world"], "Ошибка в tokenize (знаки препинания)"
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"], "Ошибка в tokenize (дефисы)"
assert tokenize("2025 год") == ["2025", "год"], "Ошибка в tokenize (числа)"
assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"], "Ошибка в tokenize (эмодзи)"

assert count_freq(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}, "Ошибка в count_freq (базовый подсчет)"
assert count_freq(["bb", "aa", "bb", "aa", "cc"]) == {"bb": 2, "aa": 2, "cc": 1}, "Ошибка в count_freq (порядок ключей)"

assert top_n({"a": 3, "b": 2, "c": 1}, 2) == [("a", 3), ("b", 2)], "Ошибка в top_n (сортировка по убыванию)"
assert top_n({"aa": 2, "bb": 2, "cc": 1}, 2) == [("aa", 2), ("bb", 2)], "Ошибка в top_n (сортировка по алфавиту при равенстве)"

print("Все проверки успешно пройдены! Функции работают правильно.")
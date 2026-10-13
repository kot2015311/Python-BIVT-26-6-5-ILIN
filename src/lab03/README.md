# ЛР3 — Тексты и частоты слов (словарь/множество)

## Задание А(функции)

### Normalize
```py
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if type(text)!= str:
        raise TypeError("Текст должен быть строкой") # Проверка 
    
    if len(text.strip()) == 0:
        raise ValueError('Пустое значение') # Проверка 
    
    result = text # Переменная под результат
    if casefold:
        result = result.casefold() # Убираем знаки, которых нет в питоне, доводим до маленького регистра
    else:
        result = result.lower() 
    
    if yo2e:
        result = result.replace('ё','е') # Замена регистра и букв е/ё
        result = result.replace('Ё','Е')
    
    result = result.replace('\t',' ') # Заменяем все ненужные знаки и буквы на пробелы
    result = result.replace('\r',' ')
    result = result.replace('\n',' ')

    result = re.sub(r' +', ' ', result) # Двойный пробелы сводим к одному

    result = result.strip() # Убираем пробелы слева и справа
    
    return result

print('ПрИвЕт\\nМИр\\t -> ', normalize("ПрИвЕт\nМИр\t"))
print('ёжик, Ёлка -> ', normalize("ёжик, Ёлка"))
print('Hello\\r\\nWorld -> ', normalize("Hello\r\nWorld"))
print('  двойные   пробелы   -> ', normalize("  двойные   пробелы  "))
```
![alt text](../../images/lab03/normalize.png)

### tokenize
```py
def tokenize(text: str) -> list[str]:
    if type(text)!= str:
        raise TypeError("Текст должен быть строкой") # Проверка 
    
    result = text

    result = re.findall(r"\w+(?:-\w+)*", text) #  Разбитие слово - слово

    return result

print('привет мир -> ', tokenize("привет мир"))
print('hello,world!!! -> ', tokenize("hello,world!!!"))
print('по-настоящему круто -> ', tokenize("по-настоящему круто"))
print('2025 год -> ', tokenize("2025 год"))
print('emoji 😀 не слово -> ', tokenize("emoji 😀 не слово"))
```
![alt text](../../images/lab03/tokenize.png)

### Count_freq
```py
def count_freq(tokens: list[str]) -> dict[str, int]:
    if type(tokens) != list:
        raise TypeError('Нужен список слов') # Проверка 
    
    if len(tokens) == 0:
        raise ValueError('Список пустой') # Проверка 

    result = {} 
    for word in tokens:
        result[word] = tokens.count(word) # Записываем в словарь сколько раз встречается конкретное слово

    return result

print('["a","b","a","c","b","a"] -> ', count_freq(["a", "b", "a", "c", "b", "a"]))
print('["bb","aa","bb","aa","cc"] -> ', count_freq(["bb", "aa", "bb", "aa", "cc"]))
```
![alt text](Count_freq.png)

### Top_n
```py
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    
    if type(freq) != dict:
        raise ValueError('Неправильный ввод данных') # Проверка 
    
    if len(freq) == 0:
        raise ValueError('Словарь пуст') # Проверка 

    if n == 0:
        raise ValueError('Нет слов') # Проверка 

    result = list(freq.items()) # Создаем список из ключей и их слов

    return sorted(result, key=lambda p: (-p[1],p[0]))[:n] 
    # key возвращает кортеж (-счёт, слово).
    # Кортежи сравниваются по первому элементу, при равенстве — по второму: сначала по убыванию счёта, при равных — по алфавиту.
    # Минус перед счётом — вместо reverse=True, чтобы слова при этом шли по возрастанию[:n] — срез списка пар, первые n

print('{"a":3,"b":2,"c":1}, n=2 -> ', top_n({"a": 3, "b": 2, "c": 1}, 2))
print('{"aa":2,"bb":2,"cc":1}, n=2 -> ', top_n({"aa": 2, "bb": 2, "cc": 1}, 2))
```
![alt text](Top_n.png)
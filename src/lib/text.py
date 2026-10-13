# 1
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if type(text)!= str:
        raise TypeError("Текст должен быть строкой") # Проверка 
    
    if len(text.strip()) == 0:
        return ''
        # raise ValueError('Пустое значение') # Проверка 
    
    result = text # Переменная под результат
    if yo2e:
        result = result.replace('ё','е') # Замена регистра и букв е/ё
        result = result.replace('Ё','Е')
    
    if casefold:
        result = result.casefold() # Убираем знаки, которых нет в питоне, доводим до маленького регистра
    else:
        result = result.lower() 
    
    
    
    result = result.replace('\t',' ') # Заменяем все ненужные знаки и буквы на пробелы
    result = result.replace('\r',' ')
    result = result.replace('\n',' ')

    result = re.sub(r' +', ' ', result) # Двойный пробелы сводим к одному

    result = result.strip() # Убираем пробелы слева и справа
    
    return result


# 2

def tokenize(text: str) -> list[str]:
    
    if type(text)!= str:
        raise TypeError("Текст должен быть строкой") # Проверка 
    
    result = text

    result = re.findall(r"\w+(?:-\w+)*", text) #  Разбитие слово - слово

    return result



# 3 

def count_freq(tokens: list[str]) -> dict[str, int]:
    if type(tokens) != list:
        raise TypeError('Нужен список слов') # Проверка 
    
    if len(tokens) == 0:
        return {}
        # raise ValueError('Список пустой') # Проверка 

    result = {} 
    for word in tokens:
        result[word] = result.count(word) # Записываем в словарь сколько раз встречается конкретное слово

    return result


# 4

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    
    if type(freq) != dict:
        raise TypeError('Неправильный ввод данных') # Проверка 
    
    if len(freq) == 0:
        return []
        # raise ValueError('Словарь пуст') # Проверка 

    if n < 0:
        raise ValueError('Нет слов') # Проверка 

    result = list(freq.items()) # Создаем список из ключей и их слов

    return sorted(result, key=lambda p: (-p[1],p[0]))[:n] 
    # key возвращает кортеж (-счёт, слово).
    # Кортежи сравниваются по первому элементу, при равенстве — по второму: сначала по убыванию счёта, при равных — по алфавиту.
    # Минус перед счётом — вместо reverse=True, чтобы слова при этом шли по возрастанию[:n] — срез списка пар, первые n


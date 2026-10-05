def format_record(rec: tuple[str, str, float]) -> str:
    
    if type(rec) is not tuple:
        raise TypeError("Входные данные должны быть кортежем")# Проверка, что входные данные кортеж
    
    
    if len(rec) != 3:
        raise ValueError("Неточный формат входных данных")# Проверка длины кортежа
    
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    
    # Проверки типов
    if type(fio) != str:
        raise TypeError("ФИО должно быть строкой")
    
    if type(group) != str:
        raise TypeError("Группа должна быть строкой")
    
    if type(gpa) not in (int, float):
        raise TypeError("GPA должен быть числом")
    
    gpa = round(gpa, 2)
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("GPA должен быть в диапазоне от 0.0 до 5.0")# Проверка диапазона GPA
    
    fio = fio.split()
    if len(fio) not in (2, 3):
        raise ValueError("Неверный ввод ФИО")
    
    
    if not group.strip():
        raise ValueError("Группа должна быть написана")# Проверка группы
    
    # Формирование ФИО с инициалами
    
    f_name = fio[0].capitalize() # Фамилия с большой буквы
    initials = ''
    for i in fio[1:]:
        initials+=i[0].upper()+'.'
    fio = f_name + ' ' + initials
    return f"{fio}, гр. {group.strip()}, GPA {gpa:.2f}"


# Тесты
print('("Иванов Иван Иванович", "BIVT-25", 4.6) -> ', format_record(("   Иванов Иван Иванович", "    BIVT-25", 4.6)))
print('("Петров Пётр", "IKBO-12", 5.0) -> ', format_record(("   Петров Пётр", "IKBO-12", 5.0)))
print('("Петров Пётр Петрович", "IKBO-12", 5.0) -> ', format_record(("Петров Пётр Петрович", "IKBO-12   ", 5.0)))
print('("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> ', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print('("Иванов Иван", "BIVT-25", 5) -> ', format_record(("Иванов Иван", "BIVT-25", 5))) 
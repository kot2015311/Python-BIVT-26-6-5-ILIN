def format_record(rec: tuple[str, str, float]) -> str:
    
    if type(rec) != tuple: #Проверка на кортеж 
        raise TypeError("Входные данные должны быть кортежем")
    
    gpa = round(rec[2],2) # Проверка на гпа
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("GPA должен быть в диапазоне от 0.0 до 5.0")
    
    fio = rec[0].split() # Проверка на имя
    if len(fio) == 0:
        raise ValueError('Напиши имя')
    
    if len(gr) == 0: # Поверка на группу
        raise ValueError('Напиши группу')
    
    if len(rec) < 3: # Недополнение
        raise ValueError("Неполный формат входных данных")
    
    if len(rec) > 3: # Переполнение
        raise IndexError("Слишком много входных данных")
    
    name = fio[0].lower() # Имя с строчных букв
    gr = rec[1]

    
    if len(fio)== 3: 
        fio1 = f'{name[0].upper()+name[1:]} {fio[1][0].upper()}. {fio[2][0].upper()}.' # Сбор ФИО+группы+гпа
    else: 
        fio1 = f'{name[0].upper()+name[1:]} {fio[1][0].upper()}.' # Если неполное фио
    fio1 = f'{fio1.strip()}, гр. {gr.strip()}, GPA {gpa:.2f}'
    return fio1

print('("Иванов Иван Иванович", "BIVT-25", 4.6) -> ',format_record(("   Иванов Иван Иванович", "    BIVT-25",           4.6)))
print('("Петров Пётр", "IKBO-12", 5.0) -> ',format_record(("   Петров Пётр", "IKBO-12", 5.0)))
print('("Петров Пётр Петрович", "IKBO-12", 5.0) -> ',format_record(("Петров Пётр Петрович", "IKBO-12   ", 5.0)))
print('("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> ',format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
# print(format_record(("  ", "ABB-01", 3.999)))
# print(format_record(("фыв  фыв фыв", "", 3.999)))




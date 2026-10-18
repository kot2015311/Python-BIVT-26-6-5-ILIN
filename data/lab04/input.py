from src.lab04.io_txt_csv import read_text, write_csv

txt = read_text("data/lab04/input.txt")  # читаем файл один раз
write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создаст CSV
print(repr(txt)) # repr покажет текст вместе с кавычками и служебными символами
# repr покажет лишние пробелы и переносы строк, которые иначе не видны.
"""Общие помощники для работы с файлами (ЛР5 и дальше)."""
from pathlib import Path                    # удобная работа с путями к файлам


def check_path(path: str | Path, suffix: str, must_exist: bool) -> Path:
    """
    Проверяет путь к файлу и возвращает его как Path.
    suffix     — нужное расширение вместе с точкой, например ".json".
    must_exist — True для входного файла: он обязан существовать.
    Неверное расширение -> ValueError, нет входного файла -> FileNotFoundError.
    """
    p = Path(path)  # превращаем строку в Path, чтобы были .suffix и .is_file()

    # Сравниваем расширение в нижнем регистре: ".JSON" и ".json" — одно и то же
    if p.suffix.lower() != suffix:
        raise ValueError(f"Неверный тип файла: {p.name} (нужен {suffix})")

    # Входной файл должен лежать на диске, иначе конвертировать нечего
    if must_exist and not p.is_file():
        raise FileNotFoundError(f"Файл не найден: {p}")

    return p

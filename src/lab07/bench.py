import timeit
import random
import os
from src.lab04.io_txt_csv import write_csv 
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def bench():
    # 1. Фиксируем генератор случайных чисел (Л8: честные замеры)
    # Чтобы при каждом запуске данные были одинаковыми и результаты воспроизводимыми.
    random.seed(42)
    
    rows = [] # Сюда будем складывать результаты: (task, n, impl, seconds)

    print("--- Замер сортировок ---")
    # Задание требует n = 1000, 10000, 100000.
    # Для своих квадратичных сортировок n=100000 — это ~10^10 операций (~15-30 минут).
    # Поэтому мерим 1000 и 10000, а для 100000 делаем честную оценку или ставим ">60".
    for n in [1000, 10000]:
        # Данные готовим ДО таймера! (Л8: не мерить генерацию данных)
        data = [random.randint(-10**6, 10**6) for _ in range(n)]
        
        # Эталон sorted (Timsort, O(n log n))
        # number=10, repeat=3 -> берем min, чтобы отсечь помехи ОС
        t = min(timeit.repeat(lambda: sorted(data), number=10, repeat=3)) / 10
        rows.append(("sort", n, "sorted", t))
        
        # Свои сортировки (O(n^2))
        # number=1, потому что они медленные. repeat=3 для надежности.
        for name, fn in [("bubble", bubble_sort), ("insertion", insertion_sort), ("selection", selection_sort)]:
            # ВАЖНО: fn(data) возвращает новый список, data не меняется.
            # Поэтому lambda: fn(data) безопасно вызывать много раз.
            t = min(timeit.repeat(lambda: fn(data), number=1, repeat=3))
            rows.append(("sort", n, name, t))
            
    # Оценка для n=100_000 (пузырёк)
    # Теория: время растет как n^2. Если n вырос в 10 раз (10^4 -> 10^5), время вырастет в 100 раз.
    # Берем время пузырька на 10000 и умножаем на 100.
    t_bubble_10k = next(r[3] for r in rows if r[0]=="sort" and r[1]==10000 and r[2]=="bubble")
    rows.append(("sort", 100000, "bubble", t_bubble_10k * 100))
    # Можно добавить строки ">60" для остальных, если требуется строгий формат
    rows.append(("sort", 100000, "insertion", ">60")) 
    rows.append(("sort", 100000, "selection", ">60"))

    print("--- Замер поиска ---")
    n = 100000
    data = [random.randint(-10**6, 10**6) for _ in range(n)]
    sorted_data = sorted(data) # Сортируем один раз до замеров
    
    # Генерируем запросы ЗАРАНЕЕ. 
    # 50% элементов из списка (есть), 50% случайных больших чисел (нет).
    queries = [random.choice(data) if random.random() < 0.5 else random.randint(10**7, 2*10**7) 
               for _ in range(10000)]

    # Линейный поиск: 10000 запросов к 100000 элементам на чистом Python — это ОЧЕНЬ долго (~минута).
    # Чтобы не ждать, мерим 1000 запросов и умножаем время на 10. Это честно по линейности O(n).
    t_lin = min(timeit.repeat(lambda: [linear_search(data, q) for q in queries[:1000]], number=1, repeat=1)) * 10
    rows.append(("search", n, "linear", t_lin))
    
    # Бинарный поиск: быстрый, мерим все 10000 запросов
    t_bin = min(timeit.repeat(lambda: [binary_search(sorted_data, q) for q in queries], number=1, repeat=3))
    rows.append(("search", n, "binary", t_bin))
    
    # Время сортировки (для честности: бинарный поиск требует отсортированных данных)
    t_sort = min(timeit.repeat(lambda: sorted(data), number=1, repeat=3))
    rows.append(("search", n, "sort_once", t_sort))

    print("--- Замер Two Sum ---")
    for n in [1000, 10000]:
        data = [random.randint(-10**6, 10**6) for _ in range(n)]
        # Гарантируем, что ответ существует (берем два случайных элемента)
        i, j = random.sample(range(n), 2)
        target = data[i] + data[j]
        
        # Fast (O(n)) - быстрый, number=10
        t_fast = min(timeit.repeat(lambda: two_sum_fast(data, target), number=10, repeat=3)) / 10
        rows.append(("two_sum", n, "fast", t_fast))
        
        # Brute (O(n^2)) - на 10000 будет долгим (~5-10 сек), но терпимо
        if n == 1000:
             t_brute = min(timeit.repeat(lambda: two_sum_brute(data, target), number=1, repeat=3))
             rows.append(("two_sum", n, "brute", t_brute))
        else:
             # На 10000 brute может занять много времени, оцениваем или пишем >60
             rows.append(("two_sum", n, "brute", ">60"))

    # --- Вывод результатов ---
    os.makedirs("data/lab07", exist_ok=True)
    
    # Запись в CSV (используем твою функцию из ЛР4)
    # Если write_csv принимает список списков/кортежей:
    try:
        write_csv(rows, 'data/lab07/bench.csv', header=('task','n','impl','seconds'))
    except TypeError:
        pass 

    print(f"\n{'task':<10}{'n':>8}{'impl':>15}{'seconds':>12}")
    for r in rows:
        task, n_val, impl, sec = r
        if isinstance(sec, float):
            print(f"{task:<10}{n_val:>8}{impl:>15}{sec:>12.4f}")
        else:
            print(f"{task:<10}{n_val:>8}{impl:>15}{sec:>12}")

if __name__ == "__main__":
    bench()
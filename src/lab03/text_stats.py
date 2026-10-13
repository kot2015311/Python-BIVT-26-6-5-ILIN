from src.lib.text import normalize, tokenize, top_n, count_freq

def text_stat(text: str):
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    top = top_n(freq)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    for word, count in top:
        print(f"{word}:{count}")


text = input()
text_stat(text)
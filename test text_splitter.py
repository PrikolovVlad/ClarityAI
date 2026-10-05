from ai.text_splitter import split_text


text = "А" * 10000

chunks = split_text(text)

print("Количество частей:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"Часть {i + 1}: {len(chunk)} символов")
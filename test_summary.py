from ai.summary import summarize_large_text


with open("lecture.txt", "r", encoding="utf-8") as file:
    material = file.read()


print("Начинаю обработку лекции...")

summary = summarize_large_text(material)

print("\n===== КОНСПЕКТ =====\n")
print(summary)
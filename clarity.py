import os
import fitz  # PyMuPDF
import ollama


def extract_text_from_pdf(pdf_path):
    """Извлекает весь печатный текст из PDF-файла."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


if __name__ == "__main__":
    # Название вашего PDF-файла (положите его в ту же папку, где лежит этот скрипт)
    pdf_file_path = "document.pdf"

    if not os.path.exists(pdf_file_path):
        print(f"Ошибка! Пожалуйста, положите ваш PDF-файл в папку с проектом под именем: {pdf_file_path}")
    else:
        print("1. Считывание текста из PDF-документа...")
        full_text = extract_text_from_pdf(pdf_file_path)

        if not full_text.strip():
            print("Текст в файле не обнаружен. Возможно, это отсканированные картинки.")
        else:
            # Ограничиваем объем текста для стабильной работы на слабом железе (около 7000 символов)
            text_to_process = full_text[:7000]

            print("2. Передача текста вашей личной ИИ (my-pdf-assistant)...")
            response = ollama.chat(
                model='my-pdf-assistant',  # Вызываем именно вашу созданную модель
                messages=[
                    {
                        'role': 'user',
                        'content': f'Сделай конспект следующего текста:\n\n{text_to_process}'
                    }
                ]
            )

            print("\n=== ВАШ БЕСПЛАТНЫЙ ЛОКАЛЬНЫЙ КОНСПЕКТ ===")
            print(response['message']['content'])

from ai.ollama import generate_response
from ai.text_splitter import split_text


def summarize_text(material):
    instruction = """
    Сделай краткий и понятный конспект учебного материала.

    Правила:
    - убери лишнюю информацию и воду;
    - сохрани основные понятия и определения;
    - выдели важные факты;
    - используй понятную структуру;
    - не придумывай информацию, которой нет в материале.
    """

    return generate_response(instruction, material)


def summarize_large_text(material):
    chunks = split_text(material)

    summaries = []

    for chunk in chunks:
        summary = summarize_text(chunk)
        summaries.append(summary)

    return "\n\n".join(summaries)
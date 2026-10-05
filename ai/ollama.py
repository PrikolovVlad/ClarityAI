import ollama


def generate_response(instruction, material):
    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "system",
                "content": instruction
            },
            {
                "role": "user",
                "content": material
            }
        ]
    )

    return response["message"]["content"]

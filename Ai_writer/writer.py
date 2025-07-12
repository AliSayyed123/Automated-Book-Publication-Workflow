# ai_writer/writer.py
from transformers import pipeline

def spin_text(text: str) -> str:
    paraphraser = pipeline("text2text-generation", model="google/flan-t5-base")
    chunks = text.split('\n\n')[:3]  # Limit to first 3 paragraphs
    spun = ""

    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()
        if not chunk or len(chunk.split()) < 5:
            continue

        prompt = f"Paraphrase the following: {chunk}"
        try:
            result = paraphraser(prompt, max_new_tokens=256, do_sample=True)
            generated = result[0]['generated_text']
            spun += f"[Chunk {i+1}]\n{generated}\n\n"
        except Exception as e:
            spun += f"[Chunk {i+1}] - Error: {e}\n\n"
            continue

    return spun.strip() if spun.strip() else "No usable content was generated."

from transformers import pipeline


def review_text(text: str):
    grammar_corrector = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")
    corrected = grammar_corrector(text[:500], max_length=512)[0]["generated_text"]
    return corrected

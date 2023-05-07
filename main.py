from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer, pipeline

app = FastAPI()
def translate_zh_to_en(text: str):
    translation = pipeline(task="translation_zh_to_en", model="Helsinki-NLP/opus-mt-zh-en", device=-1)

    translated_text = translation(text)
    return translated_text[0]["translation_text"]


class TranslationInput(BaseModel):
    text: str


class TranslationOutput(BaseModel):
    translated_text: str


@app.post("/translate/zh-en", response_model=TranslationOutput)
async def translate(input_data: TranslationInput) -> Dict[str, str]:
    translated_text = translate_zh_to_en(input_data.text)
    return {"translated_text": translated_text}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

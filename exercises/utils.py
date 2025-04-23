# utils.py
def generate_caption(image_path):
    from transformers import BlipProcessor, BlipForConditionalGeneration
    import torch

    # остальной код...

from PIL import Image
import torch
import pyttsx3

# Загружаем модель
def generate_caption(image_path):
    from transformers import BlipProcessor, BlipForConditionalGeneration
    import torch
    from PIL import Image

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    raw_image = Image.open(image_path).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt")

    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption


# Генерация подписи к изображению
def generate_caption(image_path):
    raw_image = Image.open(image_path).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Озвучка подписи
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
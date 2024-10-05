import os
import requests
from dotenv import load_dotenv
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TranslatorCredential, TextTranslationClient
from azure.ai.translation.text.models import InputTextItem
from openai import AsyncAzureOpenAI
from io import BytesIO
import asyncio

# Load environment files
ocr_env_file = '05-ocr/Python/read-text/.env'
translate_env_file = '06b-translator-sdk/Python/translate-text/.env'
chat_env_file = '03-prompt-engineering/Python/.env'
gen_env_file = '05-image-generation/Python/.env'
system_file = '03-prompt-engineering/Python/system.txt'
summarizer_system_file = '03-prompt-engineering/Python/system2.txt'

# OCR Function
def ocr():
    load_dotenv(ocr_env_file)
    ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
    ai_key = os.getenv('AI_SERVICE_KEY')

    cv_client = ImageAnalysisClient(
        endpoint=ai_endpoint,
        credential=AzureKeyCredential(ai_key)
    )

    print('\nUse our sample image or provide your own image to read text from it?\n 1. Use sample image\n 2. Provide your own image\n 3. Exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        image_file = 'ffe8cfd4174a3eed39cbb8e3db5dc9d7.jpg'
    elif choice == '2':
        image_file = input('Enter your image file path: ')
    else:
        return

    print('Reading text from the image...')
    
    return GetTextRead(cv_client, image_file)

def GetTextRead(cv_client, image_file):
    with open(image_file, "rb") as f:
        image_data = f.read()

    result = cv_client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.READ]
    )

    paragraph_text = []
    if result.read is not None:
        image = Image.open(image_file)
        fig = plt.figure(figsize=(image.width/100, image.height/100))
        plt.axis('off')
        draw = ImageDraw.Draw(image)
        color = 'cyan'

        for line in result.read.blocks[0].lines:
            paragraph_text.append(line.text)
            bounding_polygon = [(point.x, point.y) for point in line.bounding_polygon]
            draw.polygon(bounding_polygon, outline=color, width=3)

        plt.imshow(image)
        plt.tight_layout(pad=0)
        outputfile = 'text.jpg'
        fig.savefig(outputfile)
        print('\nResults saved in', outputfile)

        return " ".join(paragraph_text)

# Translation Function
def translate(input_text):
    load_dotenv(translate_env_file)
    translatorRegion = os.getenv('TRANSLATOR_REGION')
    translatorKey = os.getenv('TRANSLATOR_KEY')

    credential = TranslatorCredential(translatorKey, translatorRegion)
    client = TextTranslationClient(credential)

    languagesResponse = client.get_languages(scope="translation")
    print("Enter a target language code (e.g., 'en'):")
    targetLanguage = input()

    while targetLanguage not in languagesResponse.translation.keys():
        print(f"{targetLanguage} is not a supported language.")
        targetLanguage = input()

    input_text_elements = [InputTextItem(text=input_text)]
    print("Translating text...")
    translationResponse = client.translate(content=input_text_elements, to=[targetLanguage])

    return translationResponse[0].translations[0].text if translationResponse else None

# Azure OpenAI Function (Chat)
async def prompt_openai(prompt_text, system_file_path):
    load_dotenv(chat_env_file)
    azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
    azure_oai_key = os.getenv("AZURE_OAI_KEY")
    azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

    client = AsyncAzureOpenAI(
        azure_endpoint=azure_oai_endpoint,
        api_key=azure_oai_key,
        api_version="2024-02-15-preview"
    )

    system_text = open(file=system_file_path, encoding="utf8").read().strip()

    response = await call_openai_model(system_text, prompt_text, azure_oai_deployment, client)
    return response

async def call_openai_model(system_message, user_message, model, client):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=800
    )
    return response.choices[0].message.content

# Image Generation Function
def generate_image(prompt):
    load_dotenv(gen_env_file)
    api_base = os.getenv("AZURE_OAI_ENDPOINT_GEN")
    api_key = os.getenv("AZURE_OAI_KEY_GEN")
    api_version = '2024-02-15-preview'

    url = f"{api_base}openai/deployments/dall-e-3/images/generations?api-version={api_version}"
    headers = {"api-key": api_key, "Content-Type": "application/json"}
    body = {"prompt": prompt, "n": 1, "size": "1792x1024"}
    

    response = requests.post(url, headers=headers, json=body)
    return response.json()['data'][0]['url']

# Main Orchestration
async def main():
    text = ocr()
    translation = translate(text)
    print("\nText translated successfully.")
    print("\nGenerating Article...")
    article = await prompt_openai(translation, system_file)
    print("\nArticle generated successfully.")
    print("\nGenerating image...")
    summary = await prompt_openai(article, summarizer_system_file)
    image_url = generate_image(summary)
    print("\nImage generated successfully.")

    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        # save the image
        image.save('generated_image.jpg')
    else:
        print("Failed to retrieve the image.")
        
    print(article)
    
    print("\nProcess completed successfully.")
# Execute the main function
if __name__ == "__main__":
    asyncio.run(main())

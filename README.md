# Multilingual-News-Aggregator
This project is an AI-powered pipeline that integrates OCR (Optical Character Recognition), translation, text generation, and image creation. The project leverages several Azure AI services and OpenAI's language models to process news content in multiple languages.
## Features

1. **OCR**: Extract text from images using Azure Computer Vision.
2. **Translation**: Translate the extracted text into a desired language using Azure Translator.
3. **Text Generation**: Use OpenAI's models to generate detailed articles based on the translated text.
4. **Image Generation**: Generate custom images from the content using Azure's DALL-E 3 image generation.

---

## Setup

### Prerequisites

- Python 3.8+
- Azure subscription for Cognitive Services (Computer Vision, Translator, OpenAI)
- `.env` file with the following keys:
  - `AI_SERVICE_ENDPOINT`
  - `AI_SERVICE_KEY`
  - `OPENAI_API_KEY`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/News-Multilingual-Aggregator.git
    cd News-Multilingual-Aggregator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate # On Windows use `env\\Scripts\\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Azure service credentials as shown above.

---

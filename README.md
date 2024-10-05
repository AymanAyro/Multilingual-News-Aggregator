# Multilingual-News-Aggregator
This project is an AI-powered pipeline that integrates OCR (Optical Character Recognition), translation, text generation, and image creation. The project leverages several Azure AI services and OpenAI's language models to process news content in multiple languages.
## Features

1. **OCR**: Extract text from images using Azure Computer Vision.
2. **Translation**: Translate the extracted text into a desired language using Azure Translator.
3. **Text Generation**: Use OpenAI's models to generate detailed articles based on the translated text.
4. **Image Generation**: Generate custom images from the content using Azure's DALL-E 3 image generation.

![Slide1](https://github.com/user-attachments/assets/869d5a4a-ac88-44cd-a526-1d7095916bdd)

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

## Optical Character Recognition (OCR) with Azure AI Vision

Implements Optical Character Recognition (OCR) using the Azure AI Vision service to extract text from images. The application provides a simple command-line interface for users to analyze images and visualize the extracted text.


### Features
- **Image Analysis**: Extract text from images using Azure AI Vision.
- **Sample Image**: Use a predefined sample image for quick testing.
- **Custom Image Upload**: Provide your own image file path for analysis.
- **Visual Feedback**: Generate an output image with bounding boxes around recognized text.

  ![image](https://github.com/user-attachments/assets/96610c6f-431b-435a-abe8-f270219b0504)

---

## Text Translation and OCR with Azure AI

Implements Optical Character Recognition (OCR) and text translation using Azure AI services. It provides a command-line interface for users to extract text from images and translate text into different languages.

### Features
- **Image Analysis**: Extract text from images using Azure AI Vision.
- **Text Translation**: Translate input text into various languages using Azure Translator.
- **Sample Image**: Use a predefined sample image for quick testing.
- **Custom Image Upload**: Provide your own image file path for analysis.
- **Visual Feedback**: Generate an output image with bounding boxes around recognized text.

  ```"Alle Nachrichten Wetter: Regen, warm heute; clear That's Fit to Print" heute Abend. Sonniger, angenehmer Morgen. Temperaturbereich: heute 80-66; Sonntag 71-66. Temp .- Hum. Index gestern 69. Vollständiger US-Bericht auf S. 50. BD. CXVIII.Nr. 40,721 1969 Die New York Times Company. NEW YORK, MONTAG, 21. JULI 1969 x 10 CENTS MÄNNER GEHEN AUF DEM MOND ASTRONAUTEN LANDEN AUF DER EBENE; STEINE SAMMELN, FLAGGE PFLANZEN Stimme vom Mond: Eine pudrige Oberfläche "Eagle Has Landed" wird aus der Nähe erforscht EAGLE (die Mondlandefähre): Houston,..etc```

---

## Azure OpenAI Chat Function

### Overview
This Python module integrates with the Azure OpenAI API to facilitate chat interactions. It loads configuration settings from an environment file, retrieves the system prompt from a text file, and calls the Azure OpenAI model to get a response based on user input.

### Features
- **Asynchronous Processing**: Utilizes Python's `async` features to allow for non-blocking calls to the Azure OpenAI API, improving responsiveness in applications.
- **Configuration Management**: Loads configuration settings from an environment file, making it easy to manage sensitive information like API keys.
- **System Prompt Management**: Reads a system prompt from a text file, allowing for easy updates to the behavior of the AI model without modifying the code.
- **Dynamic User Interaction**: Accepts user input as a prompt and returns a generated response based on the provided system and user messages.
- **Error Handling**: Includes robust error handling to manage exceptions and ensure that issues during API calls do not crash the application.
- **Customizable Output**: Allows users to toggle the printing of the full response, which can be useful for debugging or logging purposes.
- **Temperature and Token Control**: Supports adjustable parameters such as `temperature` and `max_tokens`, enabling fine-tuning of the response generation.

```
Kategorie: Weltraum und Astronomie

Titel: Menschlicher Fußabdruck auf dem Mond: Eine historische Leistung der Apollo 11 Astronauten

Artikel:

Am 21. Juli 1969 wurde Geschichte geschrieben, als zwei amerikanische Astronauten der Apollo 11 Mission zum ersten Mal auf dem Mond landeten. Neil A. Armstrong und Col. Edwin E. Aldrin Jr. steuerten ihre Mondlandefähre sicher auf einer felsigen Ebene nahe der südwestlichen Küste des trockenen Meeres der Ruhe.

Armstrong, der zivile Kommandeur der Mission, war der erste Mensch, der seinen Fuß auf die Mondkruste setzte. "Houston, Tranquility Base hier. Der Adler ist gelandet", funkte er zur Erde und zum Missionskontrollraum in Houston. Dieser historische Moment wurde um 16:17:40 Uhr Eastern Daylight Time festgehalten.

Etwa sechseinhalb Stunden später verließ Armstrong das Landefahrzeug und betrat als erster Mensch den Mond. "Das ist ein kleiner Schritt für den Menschen, ein riesiger Sprung für die Menschheit", verkündete er, während eine Fernsehkamera jedes seiner Worte und Bewegungen an ein gespanntes und begeistertes Publikum von Hunderten von Millionen Menschen auf der Erde übertrug.

Sein Co-Pilot, Col. Edwin E. Aldrin Jr., trat ihm auf dem Mond bei. Gemeinsam sammelten sie Proben und pflanzten die amerikanische Flagge auf der Mondoberfläche. Ihre erfolgreiche Landung und Rückkehr zur Erde markierten einen entscheidenden Moment in der menschlichen Geschichte und Raumfahrt.
```

---

## Azure DALL-E Image Generation Function

### Overview
This Python module facilitates image generation using the DALL-E model from Azure OpenAI. It loads configuration settings from an environment file, prepares the request for image generation, and processes the response to return the generated image URL.

### Features
- **Asynchronous Image Generation**: Leverages Azure OpenAI's DALL-E model to generate images based on user-defined prompts.
- **Configuration Management**: Loads necessary configuration settings (API endpoint and keys) from an environment file for easy management and security.
- **Prompt Handling**: Accepts a user-defined prompt for generating images, allowing for a wide range of creative possibilities.
- **API Interaction**: Sends requests to the Azure DALL-E endpoint and handles responses, ensuring a smooth communication process.
- **Response Processing**: Extracts and prints the revised prompt and image URL from the response, providing feedback to the user.
- **Dynamic Size Specification**: Allows the user to specify the desired image size, in this case, set to "1792x1024".

```"Astronauts on moon, planted American flag"```

![image](https://github.com/user-attachments/assets/296add84-49a9-429e-bc2c-7f81d793c10a)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License

MIT License

Copyright (c) [2024] [AymanSaber]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

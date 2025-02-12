# EchoAI Poem Generator

A Python application that transforms text into beautiful poems using ChatGPT. The app supports multiple languages, with a default focus on Persian poetry generation.

## Features
- Transform any text into poetic form
- Support for multiple input and output languages
- Default mode: Persian to Persian poetry
- Powered by OpenAI's ChatGPT

## Requirements
- Python 3.8+
- OpenAI API key
- Required packages:
  - openai
  - python-dotenv
  - streamlit

## Setup
1. Clone the repository
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Enter your text in the input field
2. Select input language (default: Persian)
3. Select output language (default: Persian)
4. Click "Generate Poem" to transform your text into poetry
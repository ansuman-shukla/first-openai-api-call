# Sarcastic Teacher AI Chatbot

## What the Script Does

The script is a **Sarcastic Teacher AI Chatbot** that:

1. **Takes user input**: Prompts the user to enter a question or message
2. **Sends it to OpenAI**: Uses the OpenAI API with a hardcoded API key
3. **Uses a sarcastic persona**: The AI is instructed to respond as a "sarcastic Teacher AI" that answers questions in a sarcastic manner
4. **Returns the response**: Prints the AI's sarcastic response to the user's question

## How to Run It

### Prerequisites
- Python 3.x installed on your system
- Internet connection (for OpenAI API calls)

### Setup and Dependencies

1. **Virtual Environment**: The project already has a virtual environment set up in the `venv` folder.

2. **Activate the virtual environment**:
   ```powershell
   .\venv\Scripts\Activate
   ```

3. **Dependencies**: The required dependency is already installed in the virtual environment:
   - `openai` - The OpenAI Python client library

4. **Run the script**:
   ```powershell
   python first_call.py
   ```

### Usage
1. When you run the script, it will prompt: "Enter your prompt:"
2. Type your question or message
3. Press Enter
4. The AI will respond with a sarcastic answer in the style of a teacher

### Important Notes

⚠️ **Security Warning**: The script contains a hardcoded API key directly in the code, which is a security risk. In production, this should be stored in environment variables or a secure configuration file.

⚠️ **API Issues**: The script uses `client.responses.create()` and `model="gpt-4.1"`, which appear to be incorrect API calls. The correct OpenAI API usage should be `client.chat.completions.create()` with a valid model name like `"gpt-4"` or `"gpt-3.5-turbo"`.

## Project Structure

```
misogi_assignment/
├── first_call.py      # Main script file
├── requirements.txt   # Python dependencies
├── README.md         # This file
└── venv/             # Virtual environment
```#

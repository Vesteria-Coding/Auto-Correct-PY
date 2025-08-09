# Real-time Grammar and Spelling Corrector Using Google Gemini API

This Python script listens for keyboard input and automatically corrects spelling and grammar in real-time using Google's Gemini API. When you press the backtick key (`), it sends the typed text to the API and replaces it with the corrected text in your active application.

---

## Features

- Captures keyboard input live.
- Uses Google Gemini API to fix spelling and grammar.
- Automatically replaces incorrect text with corrected version.
- Simple trigger mechanism: press the backtick key (`) to submit and correct.
- Uses `pyautogui` to simulate keyboard presses for seamless text editing.

---

## Requirements

- Python 3.7+
- [Google Gemini API](https://developers.google.com/genai) access and API key.
- Python libraries:
  - `keyboard`
  - `pyautogui`
  - `python-dotenv`
  - `google-genai` (Google Gemini client)
  
Install dependencies with:

```bash
pip install keyboard pyautogui python-dotenv google-genai

## Setup

1. **Clone the repository** or download the script to your local machine.

2. The script supports inputting your Google Gemini API key via a command-line argument. To provide your API key and save it automatically to a `.env` file, run the script as follows:

```bash
python AutoCorrect.py --api_key YOUR_GOOGLE_GEMINI_API_KEY

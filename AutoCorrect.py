import os
import argparse
import keyboard
import time as t
from google import genai
import pyautogui as autogui
from google.genai import types
from dotenv import load_dotenv

# Setup
parser = argparse.ArgumentParser(description="Simple Spell Checker Using Gemini")
parser.add_argument('--api_key', help='Input your Gemini API key')
args = parser.parse_args()
print('Saving The API Key')
if args.api_key:
    with open('.env', 'w') as f:
        f.write(f'API_KEY={args.api_key}')
    print('Saved API Key')
load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))

# Main
print('Ready')
while True:
    keyboard.wait('`')
    key_log = ''
    t.sleep(0.02)
    autogui.press('backspace')
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key == '`':
                response = client.models.generate_content(
                    model="gemini-2.0-flash", contents=f"Without adding anything else and no response, fix my spelling and grammar: {key_log}"
                )
                print(response.text)
                key_log += '`'
                for i in key_log:
                    autogui.press('backspace')
                    t.sleep(0.005)
                autogui.typewrite(response.text, interval=0.04)
                t.sleep(0.02)
                break

            elif len(key) == 1:
                key_log += key
                print(key)
            elif key == 'backspace':
                key_log = key_log[:-1]
                print(key)
            elif key == 'space':
                key_log += ' '
                print(key)
            elif key == 'decimal':
                key_log += '.'
                print(key)

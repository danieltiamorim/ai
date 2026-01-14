import os
import sys
import json
import requests

#!/usr/bin/env python3
"""
gemini.py

Simple CLI to query a Google Generative AI (Gemini) model via REST.
Requires:
    - pip install requests (if don't have installed before)
    - Create and set environment variable GOOGLE_API_KEY with your API key
    - optionally set GEMINI_MODEL (default: gemini-3-flash-preview)

"""
import urllib.parse

API_KEY = "GOOGLE_API_KEY"
MODEL="gemini-3-flash-preview"
if not API_KEY:
        print("Missing GOOGLE_API_KEY environment variable", file=sys.stderr)
        sys.exit(1)

BASE = "https://generativelanguage.googleapis.com/v1beta/models"
URL = f"{BASE}/{urllib.parse.quote(MODEL)}:generateContent?key={API_KEY}"

def generate(prompt):
        payload = {
                "contents": {"parts": [{"text": prompt}]}
                   }
        headers = {"Content-Type": "application/json"}
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
                print(response.json()['candidates'][0]['content']['parts'][0]['text'])
        else:
            print("Erro:", response.text)

def main():
        print("Gemini CLI — Write some question: (Ctrl+D to  EXIT)")
        try:
                while True:
                        try:
                                prompt = input("\n> ").strip()
                        except EOFError:
                                print()
                                break
                        if not prompt:
                                continue
                        try:
                                out = generate(prompt)
                        except Exception as e:
                                print("Error:", e)
                                continue
                        f"\n{out}"
        except KeyboardInterrupt:
                print()
if __name__ == "__main__":
        main()

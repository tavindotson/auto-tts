# All .txt files in /files will be sent to OpenAI TTS and saved in /files/audio

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
voice = int(input("Enter the voice to use: "))
model = int(input("tts-1 or tts-1-hd: "))
current_dir = Path("./files")
audio_dir = current_dir / "audio"

audio_dir.mkdir(parents=True, exist_ok=True)

txt_files = sorted(current_dir.glob("*.txt"))

print("Copy the env.template to .env and edit it before running this")
print("You may want to run this inside tmux for safety")
time.sleep(5)

def process_text_file(txt_file):
    audio_file = audio_dir / (txt_file.stem + ".mp3")
    
    if audio_file.exists():
        print(f"Skipping {txt_file.name} as corresponding audio file already exists.")
        return
    
    with open(txt_file, 'r', encoding='utf-8') as f:
        text = f.read().strip()
    
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text
    )
    
    response.stream_to_file(audio_file)
    print(f"Generated audio for {txt_file.name} and saved as {audio_file.name}")

print("Processing files...")

num_threads = int(input("Enter the number of threads: "))

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(process_text_file, txt_files)

print("All conversions completed.")

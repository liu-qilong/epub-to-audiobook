import os
from dotenv import load_dotenv
from openai import OpenAI

# load environment variables from .env file
load_dotenv()

client = OpenAI(
    base_url=os.getenv("closeai_server"),
    api_key=os.getenv("closeai_key"),
)

file_path = 'temp/test.md'

with open(file_path, 'r') as file:
    rows = file.readlines()

for idx, row in enumerate(rows):
    print(f'{idx + 1}/{len(rows)} - {(idx + 1)/len(rows) * 100:.2f}%')

    if len(row) > 1:
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice="nova",
            input=row,
        )

        response.stream_to_file(f'temp/test-{str(idx).zfill(6)}.mp3')

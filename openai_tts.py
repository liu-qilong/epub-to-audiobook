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
    content = file.read()

response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=content,
)

response.stream_to_file('temp/test.mp3')
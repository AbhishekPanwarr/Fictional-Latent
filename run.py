import os
from datetime import datetime
from dotenv import load_dotenv
from google.cloud import aiplatform
import numpy as np


load_dotenv()

# prompt = f"""
# You are a character from { }. Your name is {character_name}.
# Your typical speaking style: {quirks}.
# Your past dialogues: {retrieved_dialogues}.
# You are interacting with {other_character}. Respond in character using references from your show.
# """

# response = OpenAI.chat.completions.create(
#     model="gpt-4",
#     messages=[{"role": "system", "content": prompt}]
# )
# print(response.choices[0].message['content'])

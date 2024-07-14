# import the libraries
from openai import OpenAI
import re
import os
import dotenv

# load the environment variables
dotenv.load_dotenv()

# create an instance of the OpenAI class
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# system prompts
messages = [
     {
          "role": "system",
          "content": "You are an artiest expert at impressionism.",
     }
]

# ask the user for input
paint = input("Please provide a brief description on what you want me to paint:\n")

# add the user input to the messages
messages.append(
    {
        "role": "user",
        "content": paint
    }
)

# model to use
model = "dall-e-2"

# create the completion
response = client.images.generate(
  model=model,
  prompt=messages,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
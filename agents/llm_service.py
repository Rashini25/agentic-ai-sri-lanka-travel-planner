from dotenv import load_dotenv
import os

from groq import Groq
from openai import OpenAI


load_dotenv()


# Groq client
groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# OpenRouter client
openrouter_client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)



def groq_chat(prompt):

    response = groq_client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )


    return response.choices[0].message.content



def openrouter_chat(prompt):

    response = openrouter_client.chat.completions.create(

        model="meta-llama/llama-3.1-70b-instruct",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.5
    )


    return response.choices[0].message.content
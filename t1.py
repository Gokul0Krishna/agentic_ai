from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

secret_key = os.getenv("APIKEY")

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=secret_key
)



def question(query):
    return client.chat.completions.create(model="z-ai/glm-4.5-air:free",messages=[{"role":"user","content":query}])

if __name__=="__main__":
    result = question(query="what are you")
    print(result.choices[0].message.content)
from openai import OpenAI
import os
import dotenv


dotenv.load_dotenv(".env")
key=os.getenv("gptAPIKEY")
print(key)
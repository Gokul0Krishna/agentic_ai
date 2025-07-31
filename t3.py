from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel

llmapikey=os.getenv("gptAPIKEY")

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=llmapikey
)

class bmodel(BaseModel):
    name: str
    date:str
    participants:list[str]


def call_llm():
    task=client.chat.completions.create(
        model="z-ai/glm-4.5-air:free",
        messages=[
                {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."}
        ],
        response_format={"type": "json_object"},
    )
    return task.choices[0].message.content

if __name__=="__main__":
    ret=call_llm()
    print(ret)

"""
output:

"""
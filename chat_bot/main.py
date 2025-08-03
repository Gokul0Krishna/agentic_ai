from openai import OpenAI
import os
import dotenv
import json
    
dotenv.load_dotenv(".env")
key=os.getenv("gptAPIKEY")

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=key
)



def call_llm():
    task=client.chat.completions.create(
        model="z-ai/glm-4.5-air:free",
        messages=[
                {"role":"system","content":"extract information from the user's promt and restructure it into 'goal' : str, 'location' : str, 'budget' : float,'constraints' : str and return it in a json format"},
                {"role": "user", "content": "I want to meet for coffee this Tuesday afternoon near me, vegetarian, under 20"}
        ],
    )

    return task.choices[0].message.content

def converttojson(r):
    y=json.loads(r)
    return y




if __name__=="__main__":
    # output=call_llm()
    # print(output)
    r="""{
  "goal": "meet for coffee",
  "location": "near me",
  "budget": 20.0,
  "constraints": "vegetarian, Tuesday afternoon"
    }"""
    converttojson(r)
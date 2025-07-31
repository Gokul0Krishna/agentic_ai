from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
import datetime

wapikey=os.getenv("WAPIKEY")
llmapikey=os.getenv("gptAPIKEY")

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=llmapikey
)

def get_weather_data():
    GAPIurl=" http://api.weatherapi.com/v1/forecast.json"
    gparameters={
        "q":"London",
        "days":1,
        "key":wapikey
    }
    response=requests.get(GAPIurl,params=gparameters)
    data=response.json()
    data=data['forecast']['forecastday'][0]['hour']

    format = '%Y-%m-%d %H:%M'

    for i in data: 
        dt = datetime.datetime.strptime(i["time"], format)
        if int(dt.strftime("%H"))>=(int(datetime.datetime.today().strftime("%H"))+1):
            wdata=i
            break
    return wdata

def call_llm(data):
    task=client.chat.completions.create(
        model="z-ai/glm-4.5-air:free",
        messages=[
                {"role": "system", "content": "You're a helpful assistant that provides clothing recommendations based on weather data."},
                {"role": "user", "content": f"Based on this weather data: {data}, what should I wear when I go out?"}
        ]
    )
    return task.choices[0].message.content
if __name__=="__main__":
    result=call_llm(get_weather_data())
    print(result)

"""
output-
    
Based on the weather data for July 30, 2025 at 7:00 PM, here's my clothing recommendation:

**Temperature Analysis:**
- It's a comfortable 21.5°C (70.7°F) with "feels like" temperature matching
- Cloudy skies with 63% cloud cover
- Light breeze from the north-northeast at 2.2 mph (3.6 kph)
- No precipitation expected
- Humidity at 52% (not too humid)

**Recommended Clothing:**
- **Top:** A light t-shirt or short-sleeved shirt would be perfect
- **Mid-layer:** A light sweater, cardigan, or long-sleeved shirt that you can easily layer
- **Bottoms:** Comfortable pants (chinos, casual trousers, or light jeans)
- **Footwear:** Regular sneakers, loafers, or comfortable casual shoes
- **Outerwear:** A light jacket or windbreaker might be nice but isn't essential
- **Accessories:** Consider a light scarf if you tend to get cool in the evening

This is quite pleasant weather for an evening out with friends or for a casual dinner. The mild temperature and minimal wind make for comfortable conditions without needing heavy layers.


"""
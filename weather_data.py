import requests
import os
import  dotenv


dotenv.load_dotenv()
key = os.getenv("API")
city = "Panipat"
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
response = requests.get(weather_url)
data = response.json()
#
print(data)




  






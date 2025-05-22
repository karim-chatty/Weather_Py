import requests
from datetime import datetime ,timedelta
from dotenv import load_dotenv
import os 
load_dotenv()

name=input("What is your Name :")
ur_country= input("Enter your country| city:")
 # THIS lines to get the targeted day 
dayswanted=int(input("enter the Day u want (ex:1=>tomorrow,2=>after Tomorrow,3=>thirdday ...etc) :"))
futerdate=datetime.now()+ timedelta(days=dayswanted)
print(futerdate)

API_KEY= os.getenv("API_KEY")

complete_url = f"http://api.openweathermap.org/data/2.5/forecast?q={ur_country}&appid={API_KEY}"
response = requests.get(complete_url)
whatweget = response.json()

print(response.status_code)  #THIS LINE IS TO RETURN IF OUR DATA ACCESSED OR no BY RETURNING THE status code 

for forecast in whatweget['list']:  
    
 print(f"Hello {name}, The Weather in {ur_country} on {futerdate}: \nTemperature: {forecast['main']['temp']-273.15} C \n wind speed:{forecast['wind']['speed']}\nHumidity:{forecast['main']['humidity']}")




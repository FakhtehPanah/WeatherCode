import json
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

ApiKey = "0ddfc031dcf36f601590ce662262eaf1"

City = input("Enter your favorite City : ")

# updating url
URL = BASE_URL + "q=" + City + "&appid=" + ApiKey

# sending http request 
response = requests.get(URL)

# checking the status code
if response.status_code == 200 :
    #retrieving data
    data = response.json()

    # take the main...
    main = data['main']

    # temperature, feels like, humidity, pressure, weather, wind
    temperature = main['temp']
    feels_like = main['feels_like']
    humidity = main['humidity']
    pressure = main['pressure']
    
    weather_report = data['weather']
   # weatherReport = weather_report['description']
    wind_report = data['wind']
  #  windReport = wind_report['speed']
    

    # conver Kelvin to Celsius
    Temperature =float(temperature -273.15)
    FeelsLike = float(feels_like -273.15)

    print(f"You chose {City}")
    print(f"The Temperature is : {Temperature}  Celsius")
    print(f"You Feel the temperature is : {FeelsLike}  Celsius")
    print(f"The Humidity is : {humidity} %")
    print(f"The Pressure is : {pressure}")
    print(f"Weather Report: {weather_report[0]['description']}")
    print(f"The wind speed is : {wind_report['speed']}")

else:
    print("OoOoOpsSsS ... Error")




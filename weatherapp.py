import requests

# Enter your OpenWeatherMap API key here
API_KEY = "a5bbcc34a83976f87f0fb8b1caed55f4"

# Ask user for city
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(url)
data = response.json()
print(data)

# Display weather
if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather Details")
    print("----------------------")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")

else:
    print("City not found. Please try again.")
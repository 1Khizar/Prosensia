import requests

API_KEY = "API_KEY"  # 🔑 Paste your OpenWeatherMap API key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            print("\n🌤️ Weather Info")
            print(f"📍 City: {data['name']}")
            print(f"🌡️ Temperature: {data['main']['temp']}°C")
            print(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
            print(f"💧 Humidity: {data['main']['humidity']}%")
            print(f"☁️ Weather: {data['weather'][0]['description'].title()}")
            return data
        else:
            print(" City not found. Please enter a valid city name.")
            return None
    except requests.exceptions.RequestException:
        print("⚠️ Network error. Check your connection.")
        return None

def save_to_file(data, filename="Day_21_Task/weather_data.txt"):
    with open(filename, "w") as file:
        file.write(f"str(data)\n")
    print(f"💾 Weather data saved to {filename}")

# 🔘 Simple CLI Menu
while True:
    print("\n--- Weather API App ---")
    print("1. Get weather by city")
    print("2. Exit")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        city = input("Enter city name: ")
        result = get_weather(city)
        if result:
            save = input("Do you want to save this data? (yes/no): ").lower()
            if save == "yes":
                save_to_file(result)
    elif choice == "2":
        print("👋 Goodbye!")
        break
    else:
        print(" Invalid option. Try again.")

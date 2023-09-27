import requests

BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    try:
        response = requests.get(BASE_URL)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print("Failed to fetch weather data. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def get_temperature(data):
    temperature = data['list'][0]['main']['temp']
    return temperature

def get_wind_speed(data):
    wind_speed = data['list'][0]['wind']['speed']
    return wind_speed

def get_pressure(data):
    pressure = data['list'][0]['main']['pressure']
    return pressure

def main():
    data = get_weather_data()
    if data:
        while True:
            print("\nChoose an option:")
            print("1. Get Temperature")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                temperature = get_temperature(data)
                print(f"Temperature: {temperature}°K")
            elif choice == '2':
                wind_speed = get_wind_speed(data)
                print(f"Wind Speed: {wind_speed} m/s")
            elif choice == '3':
                pressure = get_pressure(data)
                print(f"Pressure: {pressure} hPa")
            elif choice == '0':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

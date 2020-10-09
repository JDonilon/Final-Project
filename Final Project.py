# Python program to gather current weather information
# using zip code or city name

import requests


# Print the weather using city input
def print_weather_C(data, city_name):
    print("{}'s Temperature: {}°F".format(city_name, data['main']['temp']))
    print("Wind speed: {} mph".format(data['wind']['speed']))
    print("Weather: {}".format(data['weather'][0]['main']))


# Print the weather using zip input
def print_weather_Z(data, zip_code):
    print("Temperature for {}: {}°F".format(zip_code, data['main']['temp']))
    print("Wind speed: {} mph".format(data['wind']['speed']))
    print("Weather: {}" .format(data['weather'][0]['main']))


# User Menu
def menu():
    # Find weather using zip code or city name
    print('[1] Find weather using city name')
    print('[2] Find weather using zip code')
    print('[3] Quit')
    
    return int(input('\nPlease enter a number from above: '))


def more():
    print("[1] Yes")
    print("[2] No")

    return int(input('Would you like the forecast for another city or zip code? '))


# Response from Weather Service
def weather_zip(zip):
    try:
        print("Connecting")
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?' + zip + '&APPID=b48b4b3967f074d78ad4ba0dbfb3a36a&units=imperial')
        return response.json()
    except:
        print("Connection Error")


def weather_city(city):
    try:
        print("Connecting")
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?' + city + '&APPID=b48b4b3967f074d78ad4ba0dbfb3a36a&units=imperial')
        return response.json()
    except:
        print("Connection Error")

# Program Main Start
def main():
    print('Welcome to the Weather finder\n')
    while True:
        menuoption = menu()
        if (menuoption == 1):
            # www.w3resource.com
            city_name = input("Enter city: ").upper()
            print()
            try:
                city = 'q=' + city_name
                w_data = weather_city(city)
                print_weather_C(w_data, city_name)
                print()
                moreoption = more()
                if (moreoption == 1):
                    continue
                else:
                    print("Thank you for using the weather finder.")
                    break
            except:
                print("City not found")

        elif (menuoption == 2):
            # www.w3resource.com
            zip_code = input("Enter zip code: ")
            print()
            try:
                zip = 'zip=' + zip_code
                w_data = weather_zip(zip)
                print_weather_Z(w_data, zip_code)
                print()
                moreoption = more()
                if (moreoption == 1):
                    continue
                else:
                    print("Thank you for using the weather finder.")
                    break
            except:
                print("Zip code not found")

        elif (menuoption == 3):
            print('Thank you for using the weather finder.')
            break

main()

# Resources used
# https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-21.php

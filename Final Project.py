# Python program to gather current weather information
# using zip code or city name

import requests, json


# Print the weather description
def print_weather(result, city_name):
    print('The current temperature is'.format(city_name, result['main']['temp']))
    print('The current wind speed is'.format(result['wind']['speed']))
    print('The weather is currently'.format(result['weather'][0]['description']))


#User Menu
def menu():
# Find weather using zip code or city name
    print('Welcome to the Weather finder')
    print('[1] Find weather using city name')
    print('[2] Find weather using zip code')
    print('[3] Quit')
    
    return int(input('Please enter a number from above: '))


#Program Main Start
def main():
    while True:
        menuoption = menu()
        if (menuoption == 1):
            city_name = input("Enter city: ")
            print(city_name)
            data = weather_city()
            print_weather(data, city_name)

        elif (menuoption == 2):
            zip_code = input("Enter zip code: ")
            print(zip_code)
            data = weather_zip()
            print_weather(data, zip_code)

        elif (menuoption == 3):
            print('Thank you for using the weather finder.')
            break


#Response from Weather Service
def weather_zip(zip_code):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + zip_code + '&APPID+b48b4b3967f074d78ad4ba0dbfb3a36a')
    return response.json()


def weather_city(city_name):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&APPID+b48b4b3967f074d78ad4ba0dbfb3a36a')
    return response.json()


if __name__ == '__main__':
    main()

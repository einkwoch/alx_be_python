class temperror(Exception):
    def __init__(self, *args):
        super().__init__("Invalid temperature. Please enter a numeric value.")
    

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    try:
        temperature = int(input("Enter the temperature to convert: "))
    except ValueError:
        # Raise your custom exception if not numeric
        raise temperror()
    
    celcius_Fahrenheit = str(input('Is this temperature in Celsius or Fahrenheit? (C/F):')).upper()

    if celcius_Fahrenheit == 'C':
        print(f'{temperature}°C is {convert_to_fahrenheit(temperature)}°F')

    elif celcius_Fahrenheit == 'F':
        print(f'{temperature}°F is {convert_to_celsius(temperature)}°C')

    else:
        print('Enter C or F as temperature type')
except temperror as e:
    print(e)
def temperature_calculation(temperature):
    """ Conversion of Celsius, Fahrenheit and Kelvin and vise-versa """
    
    celsius, fahrenheit, kelvin = 0, 0, 0
    temperature_format = temperature[-1]
    temperature = float(temperature[:-1])
    
    if temperature_format == ('c' or 'C'):
        celsius    = temperature
        fahrenheit = ((temperature * (9 / 5)) + 32)
        kelvin     = (temperature + 273.15)
        
    elif temperature_format == ('f' or 'F'):
        celsius    = ((temperature - 32) * (5 / 9))
        fahrenheit = temperature
        kelvin     = (celsius + 273.15)
        
    elif temperature_format == ('k' or'K'):
        celsius    = (temperature - 273.15)
        fahrenheit = ((temperature * (9/5)) - 459.67)
        kelvin     = temperature
        
    else:
        print('Available unites are: C, F, K')
        
    print(f"\nCelsius: {celsius}C, Fahrenheit: {fahrenheit}F, Kelvin: {kelvin}K")


if __name__=="__main__":
    temperature = input('Input temperature endswith temperature unit (40C): ')
    temperature_calculation(temperature)

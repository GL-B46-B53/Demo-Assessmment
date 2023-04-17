def temp_converter(fahrenheit):
    ''' Fahrenheit to Celsius '''
    return 5*(fahrenheit-32)/9 


temp=float(input())
print(temp_converter(temp))

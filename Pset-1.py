def temp_converter(fahrenheit):
    ''' param : fahrenheit float
returns celsius float
'''
    return 5*(fahrenheit-32)/9 


temp=float(input())
print(temp_converter(temp))

def c_to_f(celsiuses):
    fahrenheits = []
    for celsius in celsiuses:
        if type(celsius) not in [int, float]:
            raise ValueError('Only numbers are accepted')
        
        fahrenheit = celsius * 9/5 + 32
        fahrenheits.append(fahrenheit)

    return fahrenheits

print(c_to_f([10]))


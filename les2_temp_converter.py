loop = False
while loop == False:
    start = input('Wilt u Starten..(Y/N)')
    if start.upper() == 'N':
        loop = True
    current = input('Kies een Type ...(Fh, C, K)')

    if current.upper() == 'FH':
        current = input('Waarop wilt u Omrekenen (C, K)')
        if current.upper() == 'C':
            current = float(input('Kies u Fahrenheit ...'))
            current = (current - 32)/1.8
            print('Celsius:', current)
            break
        elif current.upper() == 'K':
            current = float(input('Kies u Fahrenheit ...'))
            current = (current - 32) / 1.8 + 287.15
            print('Kelvin:', current)
            break

    elif current.upper() == 'C':
        current = input('Waarop wilt u Omrekenen (Fh, K)')
        if current.upper() == 'FH':
            current = float(input('Kies u Celsius ...'))
            current = (current * 1.8) + 32
            print('Fahrenheit:', current)

        elif current.upper() == 'K':
            current = float(input('Kies u Celsius ...'))
            current = current + 273.15
            print('Kelvin:', current)


    elif current.upper() == 'K':
        current = input('Waarop wilt u Omrekenen (Fh, C)')
        if current.upper() == 'FH':
            current = float(input('Kies u Kelvin ...'))
            current = current * 1.8 - 459.67
            print('Fahrenheit:', current)

        elif current.upper() == 'C':
            current = float(input('Kies u Kelvin ...'))
            current = current + 273.15
            print('Celsius:', current)


    else:
        loop = True
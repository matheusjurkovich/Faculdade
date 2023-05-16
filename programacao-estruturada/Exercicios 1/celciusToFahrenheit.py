def celciusToFahrenheit(celcius):
    fahrenheit = celcius * 9 / 5 + 32
    return fahrenheit

print(celciusToFahrenheit(float(input("Digite a temperatura em celcius: "))))
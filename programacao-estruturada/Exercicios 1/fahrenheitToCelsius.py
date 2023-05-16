def fahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(fahrenheitToCelsius(float(input("Digite a temperatura em fahrenheit: "))))
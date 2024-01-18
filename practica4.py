number = int(input("Escribe un numero entero de 4 digitos: "))

is_negative = False

if number < 0: 
    number *= -1
    is_negative = True

digit1 = number // 1000

number3 = number // 100

digit2 = number3 - (number3 // 10 * 10)

number2 = number // 10

digit3 = number2 - (number2 // 10 * 10)

digit4 = number - (number // 10 * 10)

if is_negative: digit1 *= -1

result = digit1 + digit2 + digit3 + digit4

print(f"El resultado de la suma de todos los digitos es: {result}")




 
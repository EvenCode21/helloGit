number = int(input("Escribe un numero entero de tres digitos para saber cuantos numeros pares tiene: "))

digit1 = number // 100

half_number = number // 10

digit2 = half_number - (half_number // 10 * 10)

digit3 = number - (number // 10 * 10)

if(digit2 < 0): digit2 *= -1

if(digit3 < 0): digit3 *= -1

counter = 0

if(digit1 % 2 == 0):
    counter += 1
if(digit2 % 2 == 0):
    counter += 1
if(digit3 % 2 == 0):
    counter += 1

print(f"El numero tiene {counter} digitos pares")
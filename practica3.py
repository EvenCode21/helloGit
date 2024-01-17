number = int(input("Escribe un numero entero de tres digitos: "))

digit1 = number // 100

half_number = number // 10

digit2 = half_number - (half_number // 10 * 10)

digit3 = number - (number // 10 * 10)

if(digit2 < 0): digit2 *= -1
if(digit3 < 0): digit3 *= -1

sum1 = digit1 + digit2
sum2 = digit1 + digit3
sum3 = digit2 + digit3

if(digit1 == sum3):
    print(f"el digito {digit1} es igual a la suma de {digit2} y {digit3}")
elif(digit2 == sum2):
    print(f"el digito {digit2} es igual a la suma de {digit1} y {digit3}")
elif(digit3 == sum1):
    print(f"el digito {digit3} es igual a la suma de {digit1} y {digit2}")
else:
    print("ningun digito es igual a la suma de los otros")
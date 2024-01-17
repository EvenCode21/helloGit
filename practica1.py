"""
Leer tres numeros enteros y determinar cual es el mayor. Usar solo dos variables



number1 = int(input("Escribe el primer numero: "))

number2 = int(input("Escribe el segundo numero: "))

if(number1 > number2):
    number2 = number1

number1 = int(input("Escribe el tercer numero: "))

if(number1 > number2):
    print(f"El {number1} es el numero mayor!")
elif(number2 > number1):
    print(f"El {number2} es el numero mayor")
else:
    print(f"el {number1} y {number2} son los mayores, pero son iguales")

"""


#leer tres numeros enteros y mostrarlos ascendentemente

number1 = int(input("Escribe el primer numero entero: "))
number2 = int(input("escribe el segundo numero entero: "))
number3 = int(input("Escribe el tercer numero entero: "))

if(number1 <= number2):
    if(number2 <= number3):
        print(f"{number1} {number2} {number3}")
    else:
        if(number3 >= number1):
            print(f"{number1} {number3} {number2}")
        else:
            print(f"{number3} {number1} {number2}")
elif(number2 <= number1):
    if(number1 <= number3):
        print(f"{number2} {number1} {number3}")
    else:
        if(number3 >= number2):
            print(f"{number2} {number3} {number1}")
        elif(number3 <= number2):
            print(f"{number3} {number2} {number1}")
elif(number1 >= number3):
    if(number3 <= number2):
        print(f"{number3} {number2} {number1}")
    
        









    





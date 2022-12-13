"""Escribir un programa que reciba por teclado dos números y un operador matemático(+,-,*,/). Realice la operación
correspondiente e imprima el resultado. En caso el operador sea distinto a los mencionados imprimir "Operador no aceptado"""

# num1= float(input("Ingrese el numero 1: "))
# num2= float(input("Ingrese el numero 2: "))
# operador= input("Ingrese la operación que quiere realizar: (+,-,*,/): ")

# if operador == "+":
#     suma= num1 + num2
#     print(f"la suma de: {num1} + {num2} = {suma}")
# elif operador == "-":
#     resta= num1 - num2
#     print(f"la resta de: {num1} - {num2} = {resta}")
# elif operador == "*":
#     multiplicación= num1 * num2
#     print(f"la multiplicación de: {num1} - {num2} = {multiplicación}")
# elif operador == "/":
#     if num2 == 0:
#         print("No se puede dividir, cualquier numero entre 0")
#     else:
#         division= num1 / num2
#         print(f"la suma de: {num1} / {num2} = {division}")
# else:
#     print("Operador no aceptado")

"""Una empresa ha decidido dar una bonificación del 5% al empleado cuyo tiempo de servicio sea superior a 3 años.
Escribir un programa que reciba por teclado el monto del salario y los años de servicio e imprima la cantidad neta de la bonificación."""

# salario= float(input("Ingrese el monto de su salario, en números: "))
# tiempo= int(input("Cuantos años lleva laborando: "))

# if tiempo > 3:
#     bonificacion= (5*(salario))/100
#     print(f"Su bonificación es de: {bonificacion}")
# else:
#     print("Aún no tiene derecho a una bonificación.")

"""Escribir un programa que reciba por teclado la edad de 3 personas ingresadas por el usuario y determinar la edad del más joven entre ellos."""

# while True:
#     edad1= int(input("Ingrese su edad: "))
#     edad2= int(input("Ingrese su edad: "))
#     edad3= int(input("Ingrese su edad: "))
#     if edad1 < edad2 and edad1 < edad3:
#         print(f"La persona mas joven entre los tres es la que tiene {edad1} años.")
#     elif edad2 < edad1 and edad2 < edad3:
#         print(f"La persona mas joven entre los tres es la que tiene {edad2} años.")
#     else:
#         print(f"La persona mas joven entre los tres es la que tiene {edad3} años.")

#     pregunta= input(f"Desea seguir preguntando?: (Ingrese 'si' o 'no'): ")
#     if pregunta == "no":
#         print("Gracias por participar.")
#         break

"""Escribir un programa que reciba por teclado los tres lados(cm) de un triángulo ingresados por el usuario y compruebe si es un triángulo equilátero, isósceles o escaleno.

Un triángulo es equilátero si tiene los tres lados iguales.
Un triángulo es escaleno si tiene los tres lados desiguales.
Un triángulo es isósceles si tiene al menos dos lados iguales."""

# lado1= float(input("Ingrese el lado a: "))
# lado2= float(input("Ingrese el lado b: "))
# lado3= float(input("Ingrese el lado c: "))

# if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
#     if lado1 == lado2 == lado3:
#         print("El triangulo es un triangulo equilátero")
#     elif lado1 != lado2 != lado3 and  lado1 != lado3:
#         print("El triangulo es un triangulo escaleno")
#     else:
#             print("El triangulo es un triangulo isósceles")
# else:
#     print("Segun las medidas ingresados la figura no es un triangulo")

"""Escriba un programa que reciba un número n ingresado por teclado por el usuario e imprima la tabla de multiplicar de n desde 1 hasta 100."""

# n= int(input("Ingrese el numero que la tabla de multiplicar: "))

# for i in range(1,101):
#     tabla= i*n
#     print(tabla)

"""Escribir un programa que imprima la serie de Fibonacci entre 0 y 100. La serie de Fibonacci; es una secuencia ordenada de números donde cada número siguiente
 se encuentra sumando los dos números anteriores."""

# primer_num= 0
# segundo_num= 1
# sum= 0
# count= 1
# print(f"Fibonacci sequence: ")
# while(count<=12):
#     print(sum)
#     count= count + 1
#     primer_num = segundo_num
#     segundo_num=sum
#     sum= primer_num + segundo_num

"""Escribir un programa que reciba por teclado dos cadenas ingresadas por el usuario, luego el programa deberá crear una nueva cadena
 formada por las dos cadenas dadas, estas deben estar separadas por un espacio y sin vocales.

Ejemplo: si las cadenas son "cincuenta" y "sesenta" entonces la nueva cadena deverá ser "cncnt ssnt"."""


# cadena1= list(input("Ingrese la primera cadena: "))
# cadena2= list(input("Ingrese la segunda cadena: "))
# #cadena1.extend(cadena2)
# vocales= ["A","E","I","O","U"]

# for i in cadena1:
#     if i.upper() in vocales:
#         cadena1.remove(i)
# for n in cadena2:
#     if n.upper() in vocales:
#         cadena2.remove(n)
# cadenaUnida= "".join(list(cadena1.extend(cadena2)))
# print(cadenaUnida)
# **************************************************

"""Dada una lista L, escribir un programa que cree una nueva lista sin los elementos duplicados. Utilice operador in o not in.

Si la lista es [500,100,200,300,200,100,600,400,800,400,500,900] el programa debe crear una nueva lista que contenga
[500, 100, 200, 300, 600, 400, 800, 900]"""

# L= [500,100,200,300,200,100,600,400,800,400,500,900]
# lista_nueva= []
# for i in L:
#     if L.count(i) > 1:
#         L.remove(i)
#         if i in L:
#             lista_nueva.append(i)
#             print(lista_nueva)

# L= [500,100,200,300,200,100,600,400,800,400,500,900]
# lista_nueva= []

# for i in L:
#     if i not in lista_nueva:  #se va colocando en cada elemento una unica vez por que cuando realice otra iteracion con el elemento duplicado ya no lo aceptará porque ya se encuentra.
#         lista_nueva.append(i)

# print(lista_nueva)
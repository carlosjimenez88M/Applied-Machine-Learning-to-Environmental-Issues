'''
Control flow
'''

# Condicionales pa ser más claro



# Condición if 

#%%
x = 10

if x > 0:
    print("x es positivo")
elif x == 0:
    print("x es cero")
else:
    print("x es negativo")

# %%
# Identation  ==========
saldo_celular = 500
recarga_nequi = 1000
saldo_nequi = 2000
if saldo_celular < 800:
    recarga_nequi -= 1000
    saldo_nequi -=1000
    saldo_celular +=1000

print(saldo_celular,saldo_nequi)
# %%
# Función para calcular el IMC
def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

# Función para clasificar el IMC
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Solicitar al usuario su peso y estatura
peso = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, estatura)

# Clasificar el IMC
clasificacion = clasificar_imc(imc)

# Mostrar el resultado
print(f"Tu IMC es {imc:.2f}, lo que indica una clasificación de: {clasificacion}.")


#===================================#
## Ejemplo completo como debe ser   #
#===================================#


#%%

def calcular_imc(peso, estatura):
    try :
        imc = peso / (estatura ** 2)
        return imc 
    except:
        print("el dato esta chueco!!")
        pass  



# Función para clasificar el IMC
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Solicitar al usuario su peso y estatura
peso = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, estatura)

# Clasificar el IMC
clasificacion = clasificar_imc(imc)

# Mostrar el resultado
print(f"Tu IMC es {imc:.2f}, lo que indica una clasificación de: {clasificacion}.")

#=========+=================#
# Ejercicio super completo  #
#===========================#
#%%

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"
def calcular_imc():
    peso = input("Ingresa tu peso mi amig@ : ")
    
    if peso == int(peso) :
        print("EL dato esta bueno {} como peso".format(peso))
    else :
        print('Ingresa nuevamente el valor de peso en kilogramos!!!')
        
    estatura = float(input("Ingresa tu Estatura mi amig@ : "))
    if estatura == float(estatura) :
        print("EL dato esta bueno {} como estatura".format(estatura))
    else :
        print('Ingresa nuevamente el valor de tu estatura !!!')
    try:
        imc = peso / (estatura ** 2)
        print("esta operación si se puede hacer")
        return clasificar_imc(imc)
    except:
        print("Esta operación no se puede realizar")
        pass 
    
calcular_imc()

#%%

peso = input("Ingresa tu peso mi amig@ : ")
if peso:
    print("EL dato esta bueno {} como peso".format(peso))
else :
    print('Ingresa nuevamente el valor de peso en kilogramos!!!')
#%%
peso = input("Ingresa tu peso mi amig@ : ")
try:
    peso_int = int(peso)
    print("El dato está bueno {} como peso".format(peso_int))
except ValueError:
    print('Ingresa nuevamente el valor de peso en kilogramos!!!')
# %%

## Ejercicio completo con try and except 

def imc_con_try_except():
    peso = 





# For ====================
# Un  ejemplo muy pero muy sencillo

ciudades = ['barranquilla', 'bogotá', 'Santa Marta', 'pereira']

for i in ciudades:
    print(i.title())
# %%
for i in ciudades:
    print(i.upper())
# %%
# Ahora haciendolo de manera más oportuna
ciudades_con_cl = []

for i in ciudades:
    ciudades_con_cl.append(i.title())
    print(i.title())

# %%
ciudades_con_cl
# %%


print(list(range(4)))
# %%
print(list(range(2,8,2)))
# %%
for index in range(len(ciudades)):
    ciudades[index] = ciudades[index].title()
    
# %%
ciudades
# %%


# While Loops =============
def calcular_factorial(n):
    factorial = 1
    contador = n
    while contador > 0:
        factorial *= contador
        contador -= 1
    return factorial

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Verificar que el número sea positivo
while numero < 0:
    print("El número debe ser positivo.")
    numero = int(input("Por favor, ingrese un número entero positivo: "))

# Calcular el factorial
resultado = calcular_factorial(numero)

# Mostrar el resultado
print(f"El factorial de {numero} es {resultado}.")

# %%
import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializar la variable de adivinanza del usuario
adivinanza = 0

# Bucle while para continuar pidiendo al usuario hasta que adivine correctamente
while adivinanza != numero_secreto:
    # Solicitar al usuario que ingrese su adivinanza
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    
    # Proporcionar retroalimentación al usuario
    if adivinanza < numero_secreto:
        print("Demasiado bajo, intenta de nuevo.")
    elif adivinanza > numero_secreto:
        print("Demasiado alto, intenta de nuevo.")

# Mensaje de felicitación cuando el usuario adivina correctamente
print("¡Felicidades! Adivinaste el número correcto.")
# %%

# Inicializar la variable para almacenar la suma de números positivos
suma = 0

print("Ingresa números para sumarlos. Ingresa 0 para terminar. Se omitirán los números negativos.")

while True:
    # Solicitar al usuario que ingrese un número
    numero = int(input("Ingresa un número: "))
    
    # Si el número es 0, salir del bucle
    if numero == 0:
        print("Fin del programa.")
        break
    
    # Si el número es negativo, omitir el resto del bucle y continuar con la siguiente iteración
    if numero < 0:
        print("Número negativo omitido.")
        continue
    
    # Sumar el número positivo a la variable suma
    suma += numero
    print(f"Suma actual: {suma}")

# Mostrar la suma final de todos los números positivos ingresados
print(f"La suma total de los números positivos ingresados es: {suma}")

# %%
#zip: Combina dos o más iterables (como listas) elemento a elemento, retornando un iterable de tuplas.
#enumerate: Añade un contador a un iterable y lo retorna en forma de un objeto enumerado, el cual puede ser convertido en una lista de tuplas.

# Listas de ejemplo
nombres = ["Ana", "Luis", "Carlos", "Marta"]
edades = [25, 30, 35, 40]

# Usar zip para combinar nombres y edades
combinados = list(zip(nombres, edades))

# Mostrar la lista combinada
print("Lista combinada (usando zip):")
for nombre, edad in combinados:
    print(f"{nombre} tiene {edad} años")

# Usar enumerate para numerar los elementos combinados
print("\nLista numerada (usando enumerate):")
for indice, (nombre, edad) in enumerate(combinados, start=1):
    print(f"{indice}. {nombre} tiene {edad} años")

# %%
# Generar una lista de números del 1 al 10
numeros = [i for i in range(1, 11)]
print(f"Lista de números del 1 al 10: {numeros}")

# Filtrar números pares usando List Comprehension
pares = [num for num in numeros if num % 2 == 0]
print(f"Números pares del 1 al 10: {pares}")

# Calcular el cuadrado de cada número usando List Comprehension
cuadrados = [num ** 2 for num in numeros]
print(f"Cuadrados de los números del 1 al 10: {cuadrados}")

# Crear una lista de tuplas (número, cuadrado) para números impares
impares_cuadrados = [(num, num ** 2) for num in numeros if num % 2 != 0]
print(f"Tuplas de números impares y sus cuadrados: {impares_cuadrados}")

# Crear una lista de cadenas que describen los números
descripciones = [f"El número {num} es {'par' if num % 2 == 0 else 'impar'}" for num in numeros]
print(f"Descripciones de los números del 1 al 10: {descripciones}")

# %%

'''
Escribiendo, como debe ser 
Funciones
'''
#%%
def imc(peso,altura):
    '''
    Peso en kilos/ altura **2
    input:
        peso: kilos
        altura: metros
    output:
        relación entre el peso y la altura
    '''
    indice = peso/(altura)**2
    return indice

# %%
imc(100,1.90)



### Ejemplo while con  soporte 
# %%
## Tarea en clase 
# Proponga esta función con multiples prints para los 
# caso que aplique el imc , como por ejemplo el sobre peso



def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def obtener_peso():
    intentos = 0
    while intentos < 3:
        peso = input("Ingresa tu peso mi amig@ : ")
        try:
            peso = float(peso) 
            print("El dato está bueno {} como peso".format(peso))
            return peso
        except ValueError:
            print('Ingresa nuevamente el valor de peso en kilogramos!!!')
            intentos += 1
    print('Número máximo de intentos alcanzado para el peso.')
    return None

def obtener_estatura():
    intentos = 0
    while intentos < 3:
        estatura = input("Ingresa tu estatura mi amig@ : ")
        try:
            estatura = float(estatura)
            print("El dato está bueno {} como estatura".format(estatura))
            return estatura
        except ValueError:
            print('Ingresa nuevamente el valor de la estatura en Metros!!!')
            intentos += 1
    print('Número máximo de intentos alcanzado para la estatura.')
    return None

def imc_con_try_except():
    peso = obtener_peso()
    estatura = obtener_estatura()
    if peso is not None and estatura is not None:
        imc = peso / (estatura ** 2)
        return clasificar_imc(imc)
    else:
        return "No se pudo calcular el IMC debido a datos incorrectos."
    
resultado = imc_con_try_except()
print("Tu clasificación de IMC es: {}".format(resultado))
#%%
def population_density(population, land_area):
    return population/land_area

test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))
# %%


# Variable Scope ---------------
# Scope: variable que se puede referenciar
# o aquella que se puede utilizar 
#%%
word = "hello"

def some_function():
    print(word)

# %%


# Expresiones Lambda (desde acá esto se pone interesante) --------- 
# Las lambdas se usan para crear funciones anonímas

def double(x):
    return x * 2

double = lambda x : x * 2
print(double(2))
# %%

## Manejo de errores --------------

mensaje = 'Hola chicos, todo va bien!!'
print(mensaje)

x = int(input("Ingresa un numero: "))
x += 20
print(x)

# %%
try:
    x = int(input("Ingresa un número: "))
    x += 10
    print(x)
except :
    print("No es un valor valido!")
    
# %%
while True:
    try:
        x = int(input("Ingresa un número: "))
        print(x)
        break
    except:
        print("No es un valor valido")
        
    print("\nEsperando el valor\n")
# %%
while True:
    try:
        x = int(input("Ingresa un número: "))
        print(x)
        break
    except:
        print("No es un valor valido")
    finally:  
        print("\nValor Ingresado\n")
# %%


## Leyendo datos -------------
# en teoría esta es la forma nativa de leer aarchivos

f = open("un path/un archivo.txt", 'r')
file_data = f.read()
f.close()

print(file_data)
#%%
## Ahora si, asi es como se deben leer
with open('unpath.txt','r') as f:
    file_data = f.read()
print(file_data)
# %%

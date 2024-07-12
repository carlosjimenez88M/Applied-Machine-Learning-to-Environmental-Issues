'''
Tipos de datos en Python
Clase de Introducción  a la programación de AI
2024
'''


# Tipos de datos ===========
# Aritmeticos --------

# Python tiene una serie de operadores 
# para ejecutar operaciones aritmeticas
# + 
# -
# *
# /
# // -> Int Division, que da un valor entero cercano a la división 
# ** -> Elevado
# % -> Da el restante de una división
#%%
print(1 + 2 + 3  - 4  * 5)
# %%
# Modular
print(9 % 2)



# Asignaciones de variables ===============


a = 1
b =2 

print(a+b)

# %%


# Enteros y flotantes
print(5/6) # Esto es un flotante
print(int(3/1)) # esto debería ser un entero

# %%

# Booleanos y operadores lógicos =================
# Booleanos son valores de verdadero o falso, no hay más , no insista solo hay esos dos !!!

se_llama_angie = True
manana_es_martes=False

print(se_llama_angie)
# %%

x = 45 > 90
print(x)

# %%
y = 45 < 90

print(y)
# %%
# Las operaciones booleanas son ==============
# >
# <
# <=
# >= -> Ojo no cambiar esto
# ==
# != -> Diferente


# and
# or
# not


edad = 18
es_joven = edad > 12 and edad < 30
print(es_joven)
# %%


# Strings =================

print("Hola gente que estudia en la Nacional!!!!")

texto = 'Hola gente que estudia en la Nacional!!!!'
print(len(texto))
# %%

# Partiendo textos ==============

new_str = "Julio Verne escribio 5 semanas en globo"
new_str.split()
# %%
new_str.split(' ', 3)
# %%

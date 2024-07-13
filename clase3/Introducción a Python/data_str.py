# listas ===================


#%%
# Crear una lista
# Las listas van dentro de [] -> No negociable
mi_lista = [1, 2, 3, 4, 5]

# Acceder a elementos
print(mi_lista[0])  # Imprime 1
print(mi_lista[-1])  # Imprime 5
#%%

# Modificar elementos
mi_lista[0] = 10
print(mi_lista)  # Imprime [10, 2, 3, 4, 5]

# Agregar elementos ------
mi_lista.append(6)
print(mi_lista)  # Imprime [10, 2, 3, 4, 5, 6]

#Eliminar elementos
mi_lista.remove(10)
print(mi_lista)  # Imprime [2, 3, 4, 5, 6]

# Longitud de la lista
print(len(mi_lista))  # Imprime 5

# Slicing (rebanado)
print(mi_lista[1:4])  # Imprime [3, 4, 5]

#En la programación de IA, las listas son extremadamente 
# útiles para manejar conjuntos de datos, realizar operaciones 
# en vectores y matrices, y almacenar resultados intermedios 
# durante el procesamiento y análisis de datos. 

#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos
data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

# Convertir las etiquetas de clase a números
label_encoder = LabelEncoder()
data["class"] = label_encoder.fit_transform(data["class"])

#%%
# # Dividir los datos en características (X) y etiquetas (y)
# X = data.iloc[:, :-1].values.tolist()
# y = data.iloc[:, -1].values.tolist()

# print('='*32)
# print('Aqui usamos una lista')

# # Dividir el conjunto de datos en entrenamiento y prueba
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Crear y entrenar el modelo
# model = RandomForestClassifier()
# model.fit(X_train, y_train)
#
# # Predecir las etiquetas en el conjunto de prueba
# y_pred = model.predict(X_test)
#
# # Calcular la precisión del modelo
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Precisión del modelo: {accuracy:.2f}")
# # %%
#
#
# # Slice ===========
#%%
algo = [1,2,3,'Maria', 'pedro']
print(algo[1:2])

# %%
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'uno'
print(my_lst)
# %%
name = "-".join(["García", "O'Kelly", "Davis"])
print(name)

# %%
## Append es mnuy importante ---
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
# # %%
# #Tuplas =========
#
# # Son listas que no se pueden alterar
# # Crear una tupla
# mi_tupla = (1, 2, 3, 4, 5)
#
# # Acceder a elementos
# print(mi_tupla[0])  # Imprime 1
# print(mi_tupla[-1])  # Imprime 5
#
# # Intentar modificar elementos (esto causará un error)
# # mi_tupla[0] = 10  # Esto causará un TypeError
#
# # Longitud de la tupla
# print(len(mi_tupla))  # Imprime 5
#
# # Slicing (rebanado)
# print(mi_tupla[1:4])  # Imprime (2, 3, 4)
#
# # %%
# # Set ==================
# # Mostrar valores únicos
# numbers = [99, 100, 1, 3, 4, 99, 100]
# unique_nums = set(numbers)
# print(unique_nums)
# # %%
#
#
#
# # Diccionarios =========
# #Los diccionarios se crean utilizando llaves {} y contienen pares clave-valor. Aquí tienes algunos ejemplos básicos de cómo trabajar con diccionarios:
#
# # Crear un diccionario
# mi_diccionario = {
#     "nombre": "Pepe",
#     "edad": 300,
#     "ciudad": "en la Bogotá"
# }
#
# # Acceder a elementos
# print(mi_diccionario["nombre"])  # Imprime "Juan"
#
# # Modificar elementos
# mi_diccionario["edad"] = 31
# print(mi_diccionario)  # Imprime {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Bogotá'}
#
# # Agregar nuevos elementos
# mi_diccionario["profesión"] = "Ingeniero"
# print(mi_diccionario)  # Imprime {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Bogotá', 'profesión': 'Ingeniero'}
#
# # Eliminar elementos
# del mi_diccionario["ciudad"]
# print(mi_diccionario)
# # %%
#
# Operadores de identidad
# is: Evalúa si dos variables apuntan al mismo objeto.
# is not: Evalúa si dos variables no apuntan al mismo objeto.
# Crear dos listas con los mismos valores

#%%
a = [1, 2, 3]
b = [1, 2, 3]

# Verificar si a y b son el mismo objeto
print(a is b)  # Imprime False

# Verificar si a y b no son el mismo objeto
print(a is not b)  # Imprime True

# Asignar a a una nueva variable c
c = a

# Verificar si a y c son el mismo objeto
print(a is c)  # Imprime True

# %%
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
# %%
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]
# %%
hydrogen = elements["hydrogen"]  # get the helium dictionary
helium_weight = elements["helium"]["weight"]

hydrogen_weight is helium_weight
# %%


def hobby():
    name =str(input("pasa tu nombre: "))
    if name =='Elkin':
        print('Hobby es la bici')

hobby()
# %%
# != -> None
# == 

#%%

'''
Construyendo un paquete
'''

# Vamos a construir una clase que determine las propiedades 
# de una distribución de Poisson


# librerias -------
#%%
import matplotlib.pyplot as plt
import math
import numpy as np

class Poisson:
    """
    Clase para representar una distribución de Poisson.

    Atributos:
    -----------
    lambda_ : float
        La tasa promedio de ocurrencia de eventos (lambda).
    """

    def __init__(self, lambda_):
        """
        Inicializa la distribución de Poisson con un valor lambda (tasa promedio de ocurrencia de eventos).
        
        Parámetros:
        -----------
        lambda_ : float
            La tasa promedio de ocurrencia de eventos.
        """
        self.lambda_ = lambda_

    def valor_esperado(self):
        """
        Devuelve el valor esperado de la distribución de Poisson.

        Returns:
        --------
        float
            El valor esperado de la distribución de Poisson.
        """
        return self.lambda_

    def varianza(self):
        """
        Devuelve la varianza de la distribución de Poisson.

        Returns:
        --------
        float
            La varianza de la distribución de Poisson.
        """
        return self.lambda_

    def probabilidad(self, k):
        """
        Calcula la probabilidad de que ocurran exactamente k eventos.

        Parámetros:
        -----------
        k : int
            Número de eventos.

        Returns:
        --------
        float
            La probabilidad de que ocurran exactamente k eventos.
        """
        return (self.lambda_ ** k) * math.exp(-self.lambda_) / math.factorial(k)

    def graficar_distribucion(self, k_max=20):
        """
        Grafica la distribución de Poisson hasta k_max eventos.

        Parámetros:
        -----------
        k_max : int, opcional
            Número máximo de eventos para graficar. El valor predeterminado es 20.
        """
        k_values = np.arange(0, k_max + 1)
        probabilities = [self.probabilidad(k) for k in k_values]

        plt.bar(k_values, probabilities, color='skyblue')
        plt.xlabel('Número de eventos (k)')
        plt.ylabel('Probabilidad')
        plt.title(f'Distribución de Poisson (λ={self.lambda_})')
        plt.show()

    def graficar_funcion_masa(self, k_max=20):
        """
        Grafica la función de masa de probabilidad de la distribución de Poisson hasta k_max eventos.

        Parámetros:
        -----------
        k_max : int, opcional
            Número máximo de eventos para graficar. El valor predeterminado es 20.
        """
        k_values = np.arange(0, k_max + 1)
        probabilities = [self.probabilidad(k) for k in k_values]

        plt.plot(k_values, probabilities, 'bo-', markersize=8)
        plt.xlabel('Número de eventos (k)')
        plt.ylabel('Probabilidad')
        plt.title(f'Función de Masa de Probabilidad de Poisson (λ={self.lambda_})')
        plt.grid()
        plt.show()
        
#%%
poisson = Poisson(lambda_=10)

# Calcular y mostrar el valor esperado y la varianza
print(f"Valor esperado: {poisson.valor_esperado()}")
print(f"Varianza: {poisson.varianza()}")

# Calcular y mostrar la probabilidad de que ocurran 2 eventos
k = 4
print(f"Probabilidad de que ocurran {k} eventos: {poisson.probabilidad(k):.4f}")

# Graficar la distribución de Poisson
poisson.graficar_distribucion()

# Graficar la función de masa de probabilidad de Poisson
poisson.graficar_funcion_masa()
# %%


## Metódos Mágicos ---------

#%%
# Son métodos que explican  como ejecutar operaciones
import math
import matplotlib.pyplot as plt
import numpy as np

class Poisson:
    """
    Clase para representar una distribución de Poisson.

    Atributos:
    -----------
    lambda_ : float
        La tasa promedio de ocurrencia de eventos (lambda).
    """

    def __init__(self, lambda_):
        """
        Inicializa la distribución de Poisson con un valor lambda (tasa promedio de ocurrencia de eventos).
        
        Parámetros:
        -----------
        lambda_ : float
            La tasa promedio de ocurrencia de eventos.
        """
        self.lambda_ = lambda_

    def valor_esperado(self):
        """
        Devuelve el valor esperado de la distribución de Poisson.

        Returns:
        --------
        float
            El valor esperado de la distribución de Poisson.
        """
        return self.lambda_

    def varianza(self):
        """
        Devuelve la varianza de la distribución de Poisson.

        Returns:
        --------
        float
            La varianza de la distribución de Poisson.
        """
        return self.lambda_

    def probabilidad(self, k):
        """
        Calcula la probabilidad de que ocurran exactamente k eventos.

        Parámetros:
        -----------
        k : int
            Número de eventos.

        Returns:
        --------
        float
            La probabilidad de que ocurran exactamente k eventos.
        """
        return (self.lambda_ ** k) * math.exp(-self.lambda_) / math.factorial(k)

    def graficar_distribucion(self, k_max=20):
        """
        Grafica la distribución de Poisson hasta k_max eventos.

        Parámetros:
        -----------
        k_max : int, opcional
            Número máximo de eventos para graficar. El valor predeterminado es 20.
        """
        k_values = np.arange(0, k_max + 1)
        probabilities = [self.probabilidad(k) for k in k_values]

        plt.bar(k_values, probabilities, color='skyblue')
        plt.xlabel('Número de eventos (k)')
        plt.ylabel('Probabilidad')
        plt.title(f'Distribución de Poisson (λ={self.lambda_})')
        plt.show()

    def graficar_funcion_masa(self, k_max=20):
        """
        Grafica la función de masa de probabilidad de la distribución de Poisson hasta k_max eventos.

        Parámetros:
        -----------
        k_max : int, opcional
            Número máximo de eventos para graficar. El valor predeterminado es 20.
        """
        k_values = np.arange(0, k_max + 1)
        probabilities = [self.probabilidad(k) for k in k_values]

        plt.plot(k_values, probabilities, 'bo-', markersize=8)
        plt.xlabel('Número de eventos (k)')
        plt.ylabel('Probabilidad')
        plt.title(f'Función de Masa de Probabilidad de Poisson (λ={self.lambda_})')
        plt.grid()
        plt.show()

    def __add__(self, other):
        """
        Suma dos distribuciones de Poisson.

        Parámetros:
        -----------
        other : Poisson
            Otra instancia de Poisson.

        Returns:
        --------
        Poisson
            Nueva instancia de Poisson con lambda sumado.
        """
        if isinstance(other, Poisson):
            return Poisson(self.lambda_ + other.lambda_)
        else:
            raise TypeError("Solo se pueden sumar instancias de Poisson")

    def __repr__(self):
        """
        Representación de la instancia de la clase Poisson.
        
        Returns:
        --------
        str
            Representación en cadena de la instancia de Poisson.
        """
        return f"Poisson(lambda_={self.lambda_})"

# Crear instancias de la clase Poisson
poisson1 = Poisson(lambda_=3)
poisson2 = Poisson(lambda_=4)

# Sumar las dos distribuciones de Poisson
poisson_sum = poisson1 + poisson2

# Mostrar la nueva instancia de Poisson resultante de la suma
print(poisson_sum)

# Calcular y mostrar el valor esperado y la varianza de la distribución sumada
print(f"Valor esperado: {poisson_sum.valor_esperado()}")
print(f"Varianza: {poisson_sum.varianza()}")

# Graficar la distribución de Poisson sumada
poisson_sum.graficar_distribucion()

# Graficar la función de masa de probabilidad de Poisson sumada
poisson_sum.graficar_funcion_masa()

# %%
## Inheritance -----

# La herencia es un concepto fundamental en la programación orientada a objetos que permite crear una nueva clase a partir de una existente. La nueva clase (subclase o clase derivada) hereda atributos y métodos de la clase existente (superclase o clase base), lo que permite reutilizar y extender el código existente.

# Conceptos Básicos
# Superclase (Clase Base): La clase de la cual se hereda.
# Subclase (Clase Derivada): La clase que hereda de otra clase.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} ladra.")


mi_animal = Animal("Animal Genérico")
mi_animal.hacer_sonido()  # Output: Animal Genérico hace un sonido.

mi_perro = Perro("Fido")
mi_perro.hacer_sonido() 
# %%
# Notese que sobre escribio que hace sonido
# En machine learning se vería como esto

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class RegresionLineal(ModeloML):
    def __init__(self):
        super().__init__("Regresión Lineal")
        self.model = LinearRegression()

    def entrenar(self, X, y):
        self.model.fit(X, y)
        print(f"{self.nombre} modelo entrenado.")

    def predecir(self, X):
        return self.model.predict(X)

    def evaluar(self, X, y):
        predicciones = self.predecir(X)
        error = mean_squared_error(y, predicciones)
        print(f"Error cuadrático medio: {error}")
        
        
## Volviendo al ejemplo de la ropa

class Camiseta:
     # La linea de abajo inicializa los atributos con los valores propios de las operaciones
     def __init__(self, color, talla, estilo, precio):
         self.color= color
         self.talla= talla
         self.estilo = estilo
         self.precio = precio
        
     def cambio_de_precio(self, new_price):
        self.precio =  new_price
        
     
     def descuento(self, off):
         return self.precio * (1- off)
     
class CamisetaDeportiva(Camiseta):
  
    def __init__(self, color, talla, estilo, precio, deporte):
        #La función super().__init__() se utiliza en el contexto de la herencia en programación orientada a objetos (OOP) para llamar al constructor de la clase base (superclase) desde una subclase
        super().__init__(color, talla, estilo, precio)
        self.deporte = deporte

    def descuento(self, off):

        descuento_adicional = 0.05  # Descuento adicional del 5% para camisetas deportivas
        return self.precio * (1 - off - descuento_adicional)


camiseta_basica = Camiseta("Rojo", "M", "Casual", 20.0)
print(f"Precio original de la camiseta básica: {camiseta_basica.precio}")
print(f"Precio de la camiseta básica con un descuento del 10%: {camiseta_basica.descuento(0.10)}")

# Crear una instancia de la clase CamisetaDeportiva
camiseta_deportiva = CamisetaDeportiva("Azul", "L", "Deportiva", 30.0, "Fútbol")
print(f"Precio original de la camiseta deportiva: {camiseta_deportiva.precio}")
print(f"Precio de la camiseta deportiva con un descuento del 10%: {camiseta_deportiva.descuento(0.10)}")
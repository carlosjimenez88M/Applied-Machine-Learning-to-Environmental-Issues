# poisson_distribution/poisson.py
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

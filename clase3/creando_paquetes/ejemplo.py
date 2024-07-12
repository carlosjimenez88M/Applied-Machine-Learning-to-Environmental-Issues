#%%
from poisson import Poisson

# Crear una instancia de la clase Poisson
poisson = Poisson(lambda_=3)

# Calcular y mostrar el valor esperado y la varianza
print(f"Valor esperado: {poisson.valor_esperado()}")
print(f"Varianza: {poisson.varianza()}")

# Calcular y mostrar la probabilidad de que ocurran 2 eventos
k = 2
print(f"Probabilidad de que ocurran {k} eventos: {poisson.probabilidad(k):.4f}")

# Graficar la distribución de Poisson
poisson.graficar_distribucion()

# Graficar la función de masa de probabilidad de Poisson
poisson.graficar_funcion_masa()

# %%

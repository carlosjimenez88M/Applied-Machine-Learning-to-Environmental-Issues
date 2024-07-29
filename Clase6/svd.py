#%%
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)  # Relación lineal con ruido

X_b = np.c_[np.ones((100, 1)), x]

# Calcular los coeficientes usando la ecuación normal (pseudo-inversa)
theta_best = np.linalg.pinv(X_b).dot(y)

# Obtener los valores predichos
y_pred = X_b.dot(theta_best)

# Gráfica de los datos originales y la línea de regresión ajustada
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x, y_pred, color='red', label='Línea de regresión ajustada', 
         linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal usando la Pseudo-Inversa')
plt.legend()
plt.grid(True)
plt.show()

theta_best

# %%

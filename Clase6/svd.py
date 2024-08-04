

#%%
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(42)
x = 2 * np.random.rand(10, 1)
y = 4 + 3 * x + np.random.randn(10, 1)  # Relación lineal con ruido

X_b = np.c_[np.ones((10, 1)), x]

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


plt.hist(y)
plt.title('Como deberian ser la predicciones')
plt.show()

plt.hist(y_pred)
plt.title('Como son predicciones, en este caso estan super chuecas')
plt.show()
# %%
plt.hist(y_pred)
plt.hist(y, color='red', alpha=0.4)
plt.show()
# %%
diff = y - y_pred
plt.hist(diff, bins=5)
# %%

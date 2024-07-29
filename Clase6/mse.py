#%%
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)  # Relación lineal con ruido

# Inicializar parámetros
w = 0.0
b = 0.0
learning_rate = 0.001
epochs = 1000

# Función para calcular el MSE (Mean Squared Error)
def compute_mse(y, y_pred):
    return np.mean((y - y_pred) ** 2)

# Descenso de gradiente para minimizar el MSE
mse_history = []
for epoch in range(epochs):
    # Hacer predicciones
    y_pred = w * x + b
    
    # Calcular gradientes
    dw = -2 * np.mean(x * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    
    # Actualizar parámetros
    w -= learning_rate * dw
    b -= learning_rate * db
    
    # Calcular y registrar el MSE
    mse = compute_mse(y, y_pred)
    mse_history.append(mse)

    # Imprimir el progreso cada 100 épocas
    if epoch % 100 == 0:
        print(f'Epoch {epoch}: MSE = {mse:.4f}, w = {w:.4f}, b = {b:.4f}')

# Gráfica de la historia del MSE y de la línea de regresión final
plt.figure(figsize=(14, 6))

# Historia del MSE
plt.subplot(1, 2, 1)
plt.plot(mse_history, label='MSE')
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.title('MSE History')
plt.grid(True)
plt.legend()

# Datos y línea de regresión ajustada
plt.subplot(1, 2, 2)
plt.scatter(x, y, color='blue', label='Datos originales')
plt.plot(x, w * x + b, color='red', label='Línea de regresión ajustada', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal usando Gradient Descent')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

w, b

# %%
import numpy as np
import matplotlib.pyplot as plt

# Definir la función de costo y su gradiente para visualización
def cost_function(w, b, x, y):
    return np.mean((y - (w * x + b)) ** 2)

def gradient_w(w, b, x, y):
    return -2 * np.mean(x * (y - (w * x + b)))

def gradient_b(w, b, x, y):
    return -2 * np.mean(y - (w * x + b))

# Generar datos de ejemplo
np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)  # Relación lineal con ruido

# Generar valores para w y b para el gráfico
w_values = np.linspace(0, 5, 100)
b_values = np.linspace(0, 10, 100)
cost_values = np.zeros((len(w_values), len(b_values)))

# Calcular el costo para cada combinación de w y b
for i, w in enumerate(w_values):
    for j, b in enumerate(b_values):
        cost_values[i, j] = cost_function(w, b, x, y)

# Crear el gráfico de superficie del costo
W, B = np.meshgrid(w_values, b_values)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(W, B, cost_values.T, cmap='viridis', alpha=0.8)
ax.set_xlabel('Weight (w)')
ax.set_ylabel('Bias (b)')
ax.set_zlabel('Cost (MSE)')
ax.set_title('Cost Function Surface')
plt.show()

# %%



#%%
import numpy as np

import matplotlib.pyplot as plt

# Initialize some parameters
np.random.seed(0)  # For reproducibility
x = np.random.randn(10, 1)
y = 5 * x + np.random.randn(10, 1)  # Adding noise to y

# Parameters
w = 0.0 
b = 0.0 
# Hyperparameter
learning_rate = 0.01

def compute_loss(y, yhat):
    """
    Calculate the Mean Squared Error (MSE) loss.
    
    Parameters:
    y (np.ndarray): True values.
    yhat (np.ndarray): Predicted values.
    
    Returns:
    float: The MSE loss.
    """
    loss = np.mean((y - yhat) ** 2)
    return loss

def descend(x, y, w, b, learning_rate):
    """
    Perform one step of gradient descent.
    
    Parameters:
    x (np.ndarray): Input features.
    y (np.ndarray): True values.
    w (float): Weight parameter.
    b (float): Bias parameter.
    learning_rate (float): Learning rate for gradient descent.
    
    Returns:
    tuple: Updated weights and bias.
    """
    N = len(y)
    yhat = w * x + b
    dldw = -2 * np.sum(x * (y - yhat)) / N
    dldb = -2 * np.sum(y - yhat) / N
    
    w -= learning_rate * dldw
    b -= learning_rate * dldb
    
    return w, b

# Initialize lists to store loss and parameters history
loss_history = []
w_history = []
b_history = []

# Iteratively make updates
for epoch in range(800): 
    w, b = descend(x, y, w, b, learning_rate)
    yhat = w * x + b
    loss = compute_loss(y, yhat)
    loss_history.append(loss)
    w_history.append(w)
    b_history.append(b)
    if epoch % 100 == 0:  # Print every 100 epochs
        print(f'Epoch {epoch} loss is {loss:.4f}, parameters w: {w:.4f}, b: {b:.4f}')

# Plotting the loss and parameter history
plt.figure(figsize=(14, 6))

# Loss history
plt.subplot(1, 2, 1)
plt.plot(loss_history, label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss History')
plt.grid(True)
plt.legend()

# Parameter history
plt.subplot(1, 2, 2)
plt.plot(w_history, label='Weight (w)')
plt.plot(b_history, label='Bias (b)')
plt.xlabel('Epoch')
plt.ylabel('Parameter values')
plt.title('Parameter History')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

w, b, x, y

# %%

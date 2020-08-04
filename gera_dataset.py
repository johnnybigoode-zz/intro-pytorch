import numpy as np
import os

dname = 'dataset'

# Cria diretório
os.makedirs(dname, exist_ok=True)

# Cria Dataset
a_true, b_true = -4, np.pi
n_samples = 500

def linear_model(x, a, b):
    return a*x + b

x_data = np.linspace(-5, 5, n_samples)
y_data = linear_model(x_data, a_true, b_true) + np.random.normal(scale=3, size=n_samples)

for i, (x, y) in enumerate(zip(x_data, y_data)):
    fname = os.path.join(dname, "{:04d}.npy".format(i+1)) 
    np.savetxt(fname, [x, y])

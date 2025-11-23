import matplotlib.pyplot as plt
from spectral_pipeline.math_core.statistics import convergence_bound
import numpy as np

# Validate theoretical bounds
N_values = np.logspace(2, 6, 50)
bounds = [convergence_bound(int(N)) for N in N_values]

plt.loglog(N_values, bounds)
plt.xlabel('Sample Size (N)')
plt.ylabel('Convergence Bound')
plt.title('Theoretical Convergence Guarantees')
plt.grid(True)
plt.show()
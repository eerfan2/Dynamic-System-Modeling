import numpy as np
import matplotlib.pyplot as plt

# Parameter
W0 = 500  # Jumlah wisatawan awal
r = 0.2   # Laju pertumbuhan per minggu
t = np.linspace(0, 20, 100)  # Waktu dalam minggu (0 hingga 20 minggu)

# Fungsi model
W = W0 * np.exp(r * t)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, W, label='Jumlah Wisatawan', color='b')
plt.xlabel('Waktu (minggu)')
plt.ylabel('Jumlah Wisatawan')
plt.title('Pertumbuhan Jumlah Wisatawan di Pantai Santolo')
plt.legend()
plt.grid(True)
plt.show()

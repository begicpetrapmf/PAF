import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
sredina = np.mean(mase_ciste)
medijan = np.median(mase_ciste)

plt.figure(figsize=(8,5))
plt.hist(
    mase_ciste,
    bins=10,
    edgecolor='black'
)
plt.axvline(
    sredina,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'Sredina = {sredina:.3f}'
)
plt.axvline(
    medijan,
    color='blue',
    linestyle='-.',
    linewidth=2,
    label=f'Medijan = {medijan:.3f}'
)

plt.xlabel("Masa [M☉]")
plt.ylabel("Frekvencija")
plt.title("Histogram mase_ciste")
plt.legend()
plt.grid(True)
plt.show()
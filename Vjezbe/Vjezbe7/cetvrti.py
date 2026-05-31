import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(
    loc=2.06,
    scale=0.05,
    size=57
).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

def medijan(podaci):
    sortirani = sorted(podaci)
    n = len(sortirani)
    if n % 2 == 1:
        return sortirani[n // 2]
    else:
        return (
            sortirani[n // 2 - 1]
            + sortirani[n // 2]
        ) / 2

sredina_sve = np.mean(mase)
medijan_sve = medijan(mase)

mase_bez = mase_ciste
sredina_bez = np.mean(mase_bez)
medijan_bez = medijan(mase_bez)

print("REZULTATI SA SVIM MJERENJIMA")
print("Aritmetička sredina =", sredina_sve)
print("Medijan =", medijan_sve)

print("REZULTATI BEZ POGREŠNIH MJERENJA")
print("Aritmetička sredina =", sredina_bez)
print("Medijan =", medijan_bez)

print("PROMJENA ARITMETIČKE SREDINE")
print(abs(sredina_sve - sredina_bez))

print("PROMJENA MEDIJANA")
print(abs(medijan_sve - medijan_bez))

plt.figure(figsize=(10, 6))
plt.hist(
    mase,
    bins=10,
    edgecolor='black',
    label='Sva mjerenja'
)

plt.axvline(
    sredina_sve,
    color='red',
    linestyle='--',
    linewidth=2,
    label='Sredina (sve)'
)
plt.axvline(
    medijan_sve,
    color='yellow',
    linestyle='-.',
    linewidth=1.75,
    label='Medijan (sve)'
)
plt.axvline(
    sredina_bez,
    color='purple',
    linestyle='--',
    linewidth=1.5,
    label='Sredina (bez pogrešaka)'
)
plt.axvline(
    medijan_bez,
    color='green',
    linestyle='-.',
    linewidth=1.25,
    label='Medijan (bez pogrešaka)'
)

plt.xlabel("Masa [M☉]")
plt.ylabel("Frekvencija")
plt.title("Histogram svih mjerenja i usporedba sredine i medijana")
plt.legend()
plt.grid(True)
plt.show()
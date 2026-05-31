import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()

def histogram(podaci, k):
    xmin = min(podaci)
    xmax = max(podaci)

#širina razreda
    h = (xmax - xmin) / k

#rubovi razreda
    rubovi = []
    for i in range(k + 1):
        rubovi.append(xmin + i * h)

#frekvencije
    frekvencije = [0] * k
    for x in podaci:
        for i in range(k):

#zadnji razred uključuje maksimalnu vrijednost
            if i == k - 1:
                if rubovi[i] <= x <= rubovi[i + 1]:
                    frekvencije[i] += 1
                    break
            else:
                if rubovi[i] <= x < rubovi[i + 1]:
                    frekvencije[i] += 1
                    break

#tekstualni histogram
    print("Histogram:\n")
    for i in range(k):
        print(f"[{rubovi[i]:.3f}, {rubovi[i+1]:.3f}) : {frekvencije[i]}")
    return rubovi, frekvencije

k = 10
rubovi, frekvencije = histogram(mase_ciste, k)
plt.figure(figsize=(8, 5))
sirina = rubovi[1] - rubovi[0]
plt.bar(
    rubovi[:-1],
    frekvencije,
    width=sirina,
    align='edge'
)
plt.xlabel("Masa [M☉]")
plt.ylabel("Frekvencija")
plt.title("Histogram mase_ciste")
plt.grid(True)
plt.show()
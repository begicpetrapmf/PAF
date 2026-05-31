import numpy as np

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

    #neparan broj
    if n % 2 == 1:
        med = sortirani[n // 2]

    #paran broj
    else:
        med = (
            sortirani[n // 2 - 1]
            + sortirani[n // 2]
        ) / 2
    return med

#paran broj elemenata
a = [3, 1, 4, 1, 5, 9, 2, 6]
print("Lista a:")
print(a)
med_a = medijan(a)
print("Medijan =", med_a)

#neparan broj elemenata
b = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Lista b:")
print(b)
med_b = medijan(b)
print("Medijan =", med_b)

#primjena na skup mase
med_mase = medijan(mase)
print("Medijan skupa mase:")
print(med_mase)

#provjera, numpy
numpy_medijan = np.median(mase)
print("NumPy medijan:")
print(numpy_medijan)

if med_mase == numpy_medijan:
    print("Rezultat se podudara s numpy.median().")
else:
    print("Rezultat se ne podudara s numpy.median().")
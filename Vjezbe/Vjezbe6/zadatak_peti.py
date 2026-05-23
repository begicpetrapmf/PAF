import math
import numpy as np

#mjerenja temperature vrenja vode
malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

#10000 mjerenja (simulacija)
np.random.seed(42)

veliko_n = np.random.normal(
    loc=100.0,
    scale=0.2,
    size=10000
).tolist()

#srednja vrijednost
def srednja_vrijednost(lista):
    return sum(lista) / len(lista)

#sigma_n
#dijeli s n
def sigma_n(lista):
    n = len(lista)
    x_sr = srednja_vrijednost(lista)
    suma = 0
    for x in lista:
        suma += (x - x_sr) ** 2
    sigma = math.sqrt(suma / n)
    return sigma

#s
#dijeli s (n-1)
def s(lista):
    n = len(lista)
    x_sr = srednja_vrijednost(lista)
    suma = 0
    for x in lista:
        suma += (x - x_sr) ** 2
    rezultat = math.sqrt(suma / (n - 1))
    return rezultat

#standardna devijacija srednje vrijednosti
def sigma_x_crta(lista):
    n = len(lista)
    s_vrijednost = s(lista)
    sigma = s_vrijednost / math.sqrt(n)
    return sigma

#relativna razlika
def relativna_razlika(a, b):
    return abs(a - b) / b * 100

sigma_n_mali = sigma_n(malo_n)
s_mali = s(malo_n)
sigma_x_mali = sigma_x_crta(malo_n)
sigma_n_veliki = sigma_n(veliko_n)
s_veliki = s(veliko_n)
sigma_x_veliki = sigma_x_crta(veliko_n)

rel_mali = relativna_razlika(
    sigma_n_mali,
    s_mali
)

rel_veliki = relativna_razlika(
    sigma_n_veliki,
    s_veliki
)

numpy_std_mali = np.std(malo_n)
numpy_std_veliki = np.std(veliko_n)

print(f"NAPOMENA: Odlučila sam radije ne koristiti već gotove funkcije iz svakog od zadataka ovih vježbi, već copy-pasteati kod za funkciju koja mi treba jer mi je tako bilo lakse.")

print(f"sigma_n = {sigma_n_mali:.6f}")
print(f"s = {s_mali:.6f}")
print(f"sigma_x = {sigma_x_mali:.6f}")
print(f"Relativna razlika između sigma_n i s = {rel_mali:.6f} %")
print(f"np.std() = {numpy_std_mali:.6f}")

print(f"sigma_n = {sigma_n_veliki:.6f}")
print(f"s = {s_veliki:.6f}")
print(f"sigma_x = {sigma_x_veliki:.6f}")
print(f"Relativna razlika između sigma_n i s = {rel_veliki:.6f} %")
print(f"np.std() = {numpy_std_veliki:.6f}")

print(f"a) Kada povećamo broj mjerenja, vrijednost s ostaje približno ista,dok se sigma_x smanjuje.")
print(f"b) Za mali skup, razlika između sigma_n i s je veća jer je broj mjerenja mali dok za veliki skup razlika poszaje vrlo mala.")
print(f"c) np.std() dijeli s n, što je ispravno kada imamo cijelu populaciju podataka, ali a uzorak podataka češće koristimo dijeljenje s (n-1).")
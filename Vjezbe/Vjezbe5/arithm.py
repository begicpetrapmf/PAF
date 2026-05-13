import math
brojevi = []
print("Unesite 10 brojeva:")

for i in range(10):
    broj = float(input(f"Unesite broj {i+1}: "))
    brojevi.append(broj)

suma = 0
for broj in brojevi:
    suma += broj

n = len(brojevi)
aritm_sredina = suma / n
suma_kvadrata = 0

for broj in brojevi:
    razlika = broj - aritm_sredina
    suma_kvadrata += razlika ** 2

standardna_devijacija = math.sqrt(
    suma_kvadrata / (n*(n-1))
)

print("\n---------------------------------")
print(f"Aritmeticka sredina = {aritm_sredina}")
print(f"Standardna devijacija = {standardna_devijacija}")
print("---------------------------------")
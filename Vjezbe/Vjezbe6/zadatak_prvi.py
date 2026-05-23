import math

valjak1_D = [19.98, 20.18, 20.10, 20.08, 19.74]
valjak2_D = [19.92, 19.82, 19.96, 19.98, 19.88]
valjak3_D = [24.96, 24.98, 24.98, 24.92, 24.94]

valjak1_L = [49.80, 49.00, 50.48, 49.80, 49.96]
valjak2_L = [52.56, 52.50, 52.62, 52.58, 52.54]
valjak3_L = [55.34, 55.40, 55.30, 55.44, 55.48]

valjak1_m = [138.92, 138.98, 139.20, 138.90, 138.92]
valjak2_m = [128.65, 128.60, 128.65, 128.35, 128.50]
valjak3_m = [71.89, 71.90, 71.79, 71.85, 71.70]

#srednja vrijednost
def srednja_vrijednost(lista):
    return sum(lista) / len(lista)

#standardno odstupanje
def standardno_odstupanje(lista):
    n = len(lista)
    x_sr = srednja_vrijednost(lista)
    suma = 0

    for x in lista:
        suma += (x - x_sr) ** 2
    sigma = math.sqrt(suma / (n * (n - 1)))
    return sigma

#dijametar -> radijus i mm -> cm
R1 = [d / 2 / 10 for d in valjak1_D]
R2 = [d / 2 / 10 for d in valjak2_D]
R3 = [d / 2 / 10 for d in valjak3_D]

#mm -> cm
L1 = [l / 10 for l in valjak1_L]
L2 = [l / 10 for l in valjak2_L]
L3 = [l / 10 for l in valjak3_L]

# VALJAK 1
R1_sr = srednja_vrijednost(R1)
sigma_R1 = standardno_odstupanje(R1)
L1_sr = srednja_vrijednost(L1)
sigma_L1 = standardno_odstupanje(L1)
m1_sr = srednja_vrijednost(valjak1_m)
sigma_m1 = standardno_odstupanje(valjak1_m)

# VALJAK 2
R2_sr = srednja_vrijednost(R2)
sigma_R2 = standardno_odstupanje(R2)
L2_sr = srednja_vrijednost(L2)
sigma_L2 = standardno_odstupanje(L2)
m2_sr = srednja_vrijednost(valjak2_m)
sigma_m2 = standardno_odstupanje(valjak2_m)

# VALJAK 3
R3_sr = srednja_vrijednost(R3)
sigma_R3 = standardno_odstupanje(R3)
L3_sr = srednja_vrijednost(L3)
sigma_L3 = standardno_odstupanje(L3)
m3_sr = srednja_vrijednost(valjak3_m)
sigma_m3 = standardno_odstupanje(valjak3_m)

print("VALJAK 1")
print(f"R = ({R1_sr:.5f} ± {sigma_R1:.5f}) cm")
print(f"L = ({L1_sr:.5f} ± {sigma_L1:.5f}) cm")
print(f"m = ({m1_sr:.5f} ± {sigma_m1:.5f}) g")

print("VALJAK 2")
print(f"R = ({R2_sr:.5f} ± {sigma_R2:.5f}) cm")
print(f"L = ({L2_sr:.5f} ± {sigma_L2:.5f}) cm")
print(f"m = ({m2_sr:.5f} ± {sigma_m2:.5f}) g")

print("VALJAK 3")
print(f"R = ({R3_sr:.5f} ± {sigma_R3:.5f}) cm")
print(f"L = ({L3_sr:.5f} ± {sigma_L3:.5f}) cm")
print(f"m = ({m3_sr:.5f} ± {sigma_m3:.5f}) g")
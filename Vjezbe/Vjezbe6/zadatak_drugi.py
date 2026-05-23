import math

#volumen valjka
def volumen_valjka(R, L):
    V = math.pi * R**2 * L
    return V

#pogreška volumena
def sigma_volumena(R, sigma_R, L, sigma_L):
    dV_dR = 2 * math.pi * R * L
    dV_dL = math.pi * R**2
    sigma_V = math.sqrt(
        (dV_dR * sigma_R) ** 2 +
        (dV_dL * sigma_L) ** 2
    )
    return sigma_V

#Valjak 1
R1 = 1.0008
sigma_R1 = 0.0073
L1 = 4.9808
sigma_L1 = 0.0244

#Valjak 2
R2 = 0.9946
sigma_R2 = 0.0030
L2 = 5.2560
sigma_L2 = 0.0021

#Valjak 3
R3 = 1.2478
sigma_R3 = 0.0011
L3 = 5.5392
sigma_L3 = 0.0033

#VOLUMEN
V1 = volumen_valjka(R1, L1)
V2 = volumen_valjka(R2, L2)
V3 = volumen_valjka(R3, L3)

#POGREŠKA
sigma_V1 = sigma_volumena(R1, sigma_R1, L1, sigma_L1)
sigma_V2 = sigma_volumena(R2, sigma_R2, L2, sigma_L2)
sigma_V3 = sigma_volumena(R3, sigma_R3, L3, sigma_L3)

print(f"Valjak 1: V = ({V1:.5e} ± {sigma_V1:.5e}) cm^3")
print(f"Valjak 2: V = ({V2:.5e} ± {sigma_V2:.5e}) cm^3")
print(f"Valjak 3: V = ({V3:.5e} ± {sigma_V3:.5e}) cm^3")
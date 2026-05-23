import math

#gustoća
def gustoca(m, V):
    rho = m / V
    return rho

#pogreška gustoćE
def sigma_gustoce(m, sigma_m, V, sigma_V):
    drho_dm = 1 / V
    drho_dV = -m / (V**2)
    sigma_rho = math.sqrt(
        (drho_dm * sigma_m) ** 2 +
        (drho_dV * sigma_V) ** 2
    )
    return sigma_rho

#VALJAK 1
m1 = 138.984
sigma_m1 = 0.0561
V1 = 15.6859
sigma_V1 = 0.1147

#VALJAK 2
m2 = 128.550
sigma_m2 = 0.0550
V2 = 16.2917
sigma_V2 = 0.0494

#VALJAK 3
m3 = 71.826
sigma_m3 = 0.0398
V3 = 27.0946
sigma_V3 = 0.0498

#GUSTOĆE
rho1 = gustoca(m1, V1)
rho2 = gustoca(m2, V2)
rho3 = gustoca(m3, V3)

#POGREŠKA GUSTOĆE
sigma_rho1 = sigma_gustoce(m1, sigma_m1, V1, sigma_V1)
sigma_rho2 = sigma_gustoce(m2, sigma_m2, V2, sigma_V2)
sigma_rho3 = sigma_gustoce(m3, sigma_m3, V3, sigma_V3)

print(f"Valjak 1: rho = ({rho1:.5e} ± {sigma_rho1:.5e}) g/cm^3")
print(f"Valjak 2: rho = ({rho2:.5e} ± {sigma_rho2:.5e}) g/cm^3")
print(f"Valjak 3: rho = ({rho3:.5e} ± {sigma_rho3:.5e}) g/cm^3")
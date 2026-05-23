import math

#relativna pogreška
def relativna_pogreska(rho, rho_lit):
    delta = abs(rho - rho_lit) / rho_lit * 100
    return delta

rho1 = 8.8610
rho2 = 7.8906
rho3 = 2.6506

#ODREDIO KOJI SU MATERIJALI U PITANJU AI
#aluminij ≈ 2.70 g/cm^3
#željezo ≈ 7.87 g/cm^3
#bakar ≈ 8.96 g/cm^3

rho_bakar = 8.96
rho_zeljezo = 7.87
rho_aluminij = 2.70

#Valjak 1 -> bakar
delta1 = relativna_pogreska(rho1, rho_bakar)

#Valjak 2 -> željezo
delta2 = relativna_pogreska(rho2, rho_zeljezo)

#Valjak 3 -> aluminij
delta3 = relativna_pogreska(rho3, rho_aluminij)

print("Valjak 1")
print("Materijal: bakar")
print(f"Relativna pogreška = {delta1:.3f} %")
print("Valjak 2")
print("Materijal: željezo")
print(f"Relativna pogreška = {delta2:.3f} %")
print("Valjak 3")
print("Materijal: aluminij")
print(f"Relativna pogreška = {delta3:.3f} %")
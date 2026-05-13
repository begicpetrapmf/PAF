import math

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

n = len(M)
suma_xy = 0
suma_x2 = 0
suma_y2 = 0

for i in range(n):
    x = phi[i]
    y = M[i]
    suma_xy += x * y
    suma_x2 += x ** 2
    suma_y2 += y ** 2

xy_srednje = suma_xy / n
x2_srednje = suma_x2 / n
y2_srednje = suma_y2 / n

a = xy_srednje / x2_srednje
sigma_a = math.sqrt(
    (1 / n) * ((y2_srednje / x2_srednje) - a ** 2)
)

print(f"Modul torzije Dt = {a}")
print(f"Greska sigma_a = {sigma_a}")
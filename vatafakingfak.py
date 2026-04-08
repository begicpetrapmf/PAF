import math
import matplotlib.pyplot as plt
from particle import Particle

v0 = 10
kut = 60
g = 9.81

R = (v0**2 * math.sin(math.radians(2*kut))) / g

dt_vrijednost = []
greske = []

dt = 0.001

while dt <= 0.1:
    p = Particle(v0, kut)   # ✅ BITNO
    num = p.range(dt)

    greska = abs(R - num) / R

    dt_vrijednost.append(dt)
    greske.append(greska)

    dt += 0.0005   # ✅ gušći graf

plt.plot(dt_vrijednost, greske)
plt.xlabel('dt')
plt.ylabel('Relativna pogreška')
plt.title('Ovisnost pogreške o dt')
plt.grid()
plt.show()
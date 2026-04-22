import projectile
from projectile import Projectile
import numpy as np
import matplotlib.pyplot as plt
#masa 0.145kg (loptica), v0=50m/s, kut=45
p = Projectile(0, 0, 50, 45, 0.145, 0.47, 0.013)
time_steps = [0.1, 0.01, 0.001]
results = {}

for dt in time_steps:
    proj = Projectile(0, 0, 50, 45, 0.145, 0.47, 0.013)
    proj.simulate(dt)
    results[dt] = (proj.x, proj.y)

plt.figure(figsize=(10, 6))
for dt, (x, y) in results.items():
    plt.plot(x, y, label=f'dt = {dt} s')

plt.title('Kosi hitac s otporom zraka: Utjecaj $\Delta t$')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.show()
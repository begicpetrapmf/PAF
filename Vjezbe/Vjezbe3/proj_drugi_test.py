import numpy as np
import matplotlib.pyplot as plt
from projectile import Projectile
from proj_drugi import Projectile

dt = 0.01

# Euler metoda
p_euler = Projectile(0, 0, 50, 45, 0.145, 0.47, 0.013)
p_euler.simulate(dt)

# RK4 metoda
p_rk4 = Projectile(0, 0, 50, 45, 0.145, 0.47, 0.013)
p_rk4.simulate_rk4(dt)

plt.figure(figsize=(10,6))
plt.plot(p_euler.x, p_euler.y, label='Euler')
plt.plot(p_rk4.x, p_rk4.y, label='RK4')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Usporedba: Euler vs RK4 (dt = 0.01)')
plt.legend()
plt.grid()
plt.ylim(bottom=0)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x0, y0, v0, angle, mass, cd, area, rho=1.225):
        self.x = [x0]
        self.y = [y0]
        self.vx = [v0 * np.cos(np.radians(angle))]
        self.vy = [v0 * np.sin(np.radians(angle))]
        self.t = [0]
        
        self.m = mass
        self.cd = cd 
        self.area = area
        self.rho = rho
        self.g = 9.81

    def simulate(self, dt):
        """Simulira kosi hitac koristeći Eulerovu metodu."""
        while self.y[-1] >= 0:
            v = np.sqrt(self.vx[-1]**2 + self.vy[-1]**2)
            f_drag = 0.5 * self.cd * self.rho * self.area * v**2
            ax = -(f_drag * (self.vx[-1] / v)) / self.m if v > 0 else 0
            ay = -self.g - (f_drag * (self.vy[-1] / v)) / self.m if v > 0 else -self.g
            self.x.append(self.x[-1] + self.vx[-1] * dt)
            self.y.append(self.y[-1] + self.vy[-1] * dt)
            self.vx.append(self.vx[-1] + ax * dt)
            self.vy.append(self.vy[-1] + ay * dt)
            self.t.append(self.t[-1] + dt)

# AI je radio matematiku.
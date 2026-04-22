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

    def acceleration(self, vx, vy):
        v = np.sqrt(vx**2 + vy**2)
        if v == 0:
            return 0, -self.g

        f_drag = 0.5 * self.cd * self.rho * self.area * v**2
        ax = -(f_drag * (vx / v)) / self.m
        ay = -self.g - (f_drag * (vy / v)) / self.m
        return ax, ay

    def simulate(self, dt):
        """Euler metoda"""
        while self.y[-1] >= 0:
            vx, vy = self.vx[-1], self.vy[-1]
            ax, ay = self.acceleration(vx, vy)

            self.x.append(self.x[-1] + vx * dt)
            self.y.append(self.y[-1] + vy * dt)
            self.vx.append(vx + ax * dt)
            self.vy.append(vy + ay * dt)
            self.t.append(self.t[-1] + dt)

    def simulate_rk4(self, dt):
        """Runge-Kutta 4. reda"""
        while self.y[-1] >= 0:
            x, y = self.x[-1], self.y[-1]
            vx, vy = self.vx[-1], self.vy[-1]

            ax1, ay1 = self.acceleration(vx, vy)
            k1_vx, k1_vy = ax1 * dt, ay1 * dt
            k1_x, k1_y = vx * dt, vy * dt

            ax2, ay2 = self.acceleration(vx + k1_vx/2, vy + k1_vy/2)
            k2_vx, k2_vy = ax2 * dt, ay2 * dt
            k2_x, k2_y = (vx + k1_vx/2) * dt, (vy + k1_vy/2) * dt

            ax3, ay3 = self.acceleration(vx + k2_vx/2, vy + k2_vy/2)
            k3_vx, k3_vy = ax3 * dt, ay3 * dt
            k3_x, k3_y = (vx + k2_vx/2) * dt, (vy + k2_vy/2) * dt

            ax4, ay4 = self.acceleration(vx + k3_vx, vy + k3_vy)
            k4_vx, k4_vy = ax4 * dt, ay4 * dt
            k4_x, k4_y = (vx + k3_vx) * dt, (vy + k3_vy) * dt

            self.vx.append(vx + (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) / 6)
            self.vy.append(vy + (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy) / 6)
            self.x.append(x + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6)
            self.y.append(y + (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6)
            self.t.append(self.t[-1] + dt)

#AI je zasluzan za matematiku.
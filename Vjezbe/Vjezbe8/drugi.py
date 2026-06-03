import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

g=9.81
kut_deg = np.array([
    0, 5, 10, 15, 20, 25, 30, 35, 40,
    45, 50, 55, 60, 65, 70, 75, 80, 85
])
T_120 = np.array([
    0.8020, 0.8187, 0.8327, 0.8660,
    0.8980, 0.9153, 0.9293, 0.9653,
    0.9747, 1.0200, 1.0373, 1.1160,
    1.1780, 1.2733, 1.4180, 1.6373,
    1.9100, 2.5460
])
T_240 = np.array([
    1.0140, 1.0320, 1.0433, 1.0673,
    1.0840, 1.1320, 1.1440, 1.1720,
    1.1980, 1.2293, 1.2813, 1.3573,
    1.4200, 1.5600, 1.7413, 1.9840,
    2.4473, 3.1573
])

def period(theta_deg, l):
    theta_rad = np.radians(theta_deg)
    return 2*np.pi*np.sqrt(
        l/(g*np.cos(theta_rad))
    )

l_teorija_120 = 0.120
param120, cov120 = curve_fit(
    period,
    kut_deg,
    T_120,
    p0=[0.12]
)
l_fit_120 = param120[0]

l_teorija_240 = 0.240
param240, cov240 = curve_fit(
    period,
    kut_deg,
    T_240,
    p0=[0.24]
)
l_fit_240 = param240[0]

rel120 = abs(l_fit_120-l_teorija_120)/l_teorija_120*100
rel240 = abs(l_fit_240-l_teorija_240)/l_teorija_240*100

print("L=120mm")
print(f"Teorijska duljina = {l_teorija_120}m")
print(f"Fit duljina = {l_fit_120}m")
print(f"Relativna pogreška = {rel120}%")
print("L=240mm")
print(f"Teorijska duljina = {l_teorija_240}m")
print(f"Fit duljina = {l_fit_240}m")
print(f"Relativna pogreška = {rel240}%")

theta = np.linspace(0,85,300)
plt.figure(figsize=(8,5))
plt.scatter(
    kut_deg,
    T_120,
    label="Mjerenja"
)
plt.plot(
    theta,
    period(theta, l_teorija_120),
    label="Teorija"
)
plt.plot(
    theta,
    period(theta, l_fit_120),
    label="curve_fit"
)
plt.xlabel("Kut (°)")
plt.ylabel("Period T (s)")
plt.title("Njihalo L = 120 mm")
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(
    kut_deg,
    T_240,
    label="Mjerenja"
)
plt.plot(
    theta,
    period(theta, l_teorija_240),
    label="Teorija"
)
plt.plot(
    theta,
    period(theta, l_fit_240),
    label="curve_fit"
)
plt.xlabel("Kut (°)")
plt.ylabel("Period T (s)")
plt.title("Njihalo L = 240 mm")
plt.grid()
plt.legend()
plt.show()
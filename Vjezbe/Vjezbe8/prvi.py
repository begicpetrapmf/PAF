import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

h0=0.54      
m=0.5257    
r=4.025e-3   
g=9.81      
h = np.array([0.14, 0.17, 0.19, 0.22, 0.25,
              0.28, 0.31, 0.34, 0.37, 0.40])
t = np.array([1.740, 1.793, 2.043, 2.190, 2.280,
              2.417, 2.540, 2.640, 2.670, 2.813])

s = h0 - h
def pravac(x, a, b):
    return a*x + b

def linearna_regresija(x, y):
    n = len(x)
    a = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / \
        (n*np.sum(x**2) - (np.sum(x))**2)
    b = (np.sum(y) - a*np.sum(x)) / n
    return a, b


# a) log(s)-log(t)
log_s = np.log10(s)
log_t = np.log10(t)
a1, b1 = linearna_regresija(log_t, log_s)
parametri1, kov1 = curve_fit(pravac, log_t, log_s)
da1 = np.sqrt(kov1[0,0])
db1 = np.sqrt(kov1[1,1])

print("log(s)-log(t)")
print(f"Nagib a = {a1:.6f} ± {da1:.6f}")
print(f"Odsječak b = {b1:.6f} ± {db1:.6f}")

x = np.linspace(min(log_t), max(log_t), 100)
y = a1*x+b1

plt.figure(figsize=(8,5))
plt.scatter(log_t, log_s, label="Mjerenja")
plt.plot(x, y, label="Linearni fit")
plt.xlabel("log(t)")
plt.ylabel("log(s)")
plt.title("log(s) - log(t)")
plt.grid()
plt.legend()
plt.show()


# b) s - t²
t2 = t**2
a2, b2 = linearna_regresija(t2, s)
parametri2, kov2 = curve_fit(pravac, t2, s)
da2 = np.sqrt(kov2[0,0])
db2 = np.sqrt(kov2[1,1])

print("s - t²")
print(f"Nagib a = {a2:.6f} ± {da2:.6f}")
print(f"Odsječak b = {b2:.6f} ± {db2:.6f}")

x2 = np.linspace(min(t2), max(t2), 100)
y2 = a2*x2+b2

plt.figure(figsize=(8,5))
plt.scatter(t2, s, label="Mjerenja")
plt.plot(x2, y2, label="Linearni fit")
plt.xlabel("t² (s²)")
plt.ylabel("s (m)")
plt.title("s - t²")
plt.grid()
plt.legend()
plt.show()


# c) efekt. ubrzanje
a_ef = 2*abs(a2)
da_ef = 2*da2
print(f"a_ef = {a_ef:.6f} ± {da_ef:.6f}m/s²")

# moment tromosti
Iz = m*r**2*(g/a_ef-1)
print(f"Iz = {Iz:.8e} kgm²")

# pogreska momenta tromostu
dIz_da = abs(-(m*r**2*g)/(a_ef**2))
dIz = dIz_da*da_ef

print(f"dIz = {dIz:.8e}kgm²")
print(f"Iz = ({Iz:.8e} ± {dIz:.8e})kgm²")
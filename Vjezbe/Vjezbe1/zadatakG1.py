# Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, 
# a program crta x − t, v − t i a − t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. 
# Diferencijalne jednadžbe rješavajte numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import matplotlib.pyplot as plt
F=float(input(f'Unesi silu(N):'))
m=float(input(f'Unesi masu(kg):'))

# F=m*a
a=F/m
dt=0.01
t_max=10

# za t=0
t=0
v=0
x=0

t_podaci=[]
x_podaci=[]
v_podaci=[]
a_podaci=[]

while t<=t_max:
    t_podaci.append(t)
    x_podaci.append(x)
    v_podaci.append(v)
    a_podaci.append(a)
    x=x+v*dt
    v=v+a*dt
    t=t+dt

plt.figure()
plt.plot(x_podaci, t_podaci)
plt.xlabel(f't (s)')
plt.ylabel(f'x (m)')
plt.title(f'x - t graf')
plt.show()

plt.figure()
plt.plot(t_podaci, v_podaci)
plt.xlabel(f't (s)')
plt.ylabel(f'v (m/s)')
plt.title(f'v - t graf')
plt.show()

plt.figure()
plt.plot(t_podaci, a_podaci)
plt.xlabel(f't (s)')
plt.ylabel(f'a (m/s^2)')
plt.title(f'a - t graf')
plt.show()
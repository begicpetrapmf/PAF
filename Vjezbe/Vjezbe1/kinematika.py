# Napišite svoj modul "kinematika.py" koji će sadržavati funckiju jednoliko_gibanje(). 
# Neka funkcije kao ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, masa, ...) 
# i neka crta iste grafove kao i u prošlom zadatku. 
# Napravite novi program u kojem ćete uključiti razvijeni modul i pozvati funkciju.

def jednoliko_gibanje(F,m,t_max):   
    import matplotlib.pyplot as plt
    dt=0.1   # fiksni dt
    a=F/m
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

# Ovaj put sam radila razdvojene grafove, no znam da postoji i subplot.
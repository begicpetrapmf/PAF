import kosi_hitac
from kosi_hitac import KosiHitac

projektil = KosiHitac(
    v0=30,
    kut=45
)

# 1. putanja
projektil.crtaj_putanju()

# 2. maksimalna visina
h = projektil.maksimalna_visina()
print("Maksimalna visina:")
print(f"{h:.4f} m")

# 3. domet
R = projektil.domet()
print("\nDomet:")
print(f"{R:.4f} m")

# 4. maksimalna brzina
vmax = projektil.maksimalna_brzina()
print("\nMaksimalna brzina:")
print(f"{vmax:.4f} m/s")

# 5. meta
projektil.pogodi_metu(
    xm=float(input("Unesite x koordinatu mete: ")),
    ym=float(input("Unesite y koordinatu mete: ")),
    r=float(input("Unesite radijus mete: "))
)




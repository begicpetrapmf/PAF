import math
import matplotlib.pyplot as plt

class KosiHitac:
    def __init__(self, v0, kut, x0=0, y0=0):
        self.v0 = v0
        self.kut = math.radians(kut)
        self.x0 = x0
        self.y0 = y0
        self.g = 9.81
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.kut)
        self.vy = self.v0 * math.sin(self.kut)

    def __move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt - 0.5 * self.g * dt**2
        self.vy -= self.g * dt

    def simulacija(self, dt=0.001):
        self.reset()
        xs = [self.x]
        ys = [self.y]
        brzine = [math.sqrt(self.vx**2 + self.vy**2)]

        while True:
            stari_x = self.x
            stari_y = self.y
            self.__move(dt)
            if self.y < 0:
                # interpolacija točke udara u tlo
                omjer = stari_y / (stari_y - self.y)
                x_tlo = stari_x + omjer * (self.x - stari_x)
                xs.append(x_tlo)
                ys.append(0)
                brzine.append(
                    math.sqrt(self.vx**2 + self.vy**2)
                )
                break

            xs.append(self.x)
            ys.append(self.y)
            brzine.append(
                math.sqrt(self.vx**2 + self.vy**2)
            )

        return xs, ys, brzine

    def crtaj_putanju(self, dt=0.001):
        xs, ys, _ = self.simulacija(dt)
        plt.figure(figsize=(10, 6))
        plt.plot(
            xs,
            ys,
            linewidth=2,
            label="Putanja"
        )
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.title("Kosi hitac")
        plt.grid(True, linestyle='--')
        plt.legend()
        plt.xticks(range(0, 101, 5))
        plt.yticks(range(0, 31, 5))
        plt.show()

    def maksimalna_visina(self, dt=0.001):
        _, ys, _ = self.simulacija(dt)
        return max(ys)

    def domet(self, dt=0.001):
        xs, _, _ = self.simulacija(dt)
        return xs[-1]

    def maksimalna_brzina(self, dt=0.001):
        _, _, brzine = self.simulacija(dt)
        return max(brzine)

    def pogodi_metu(self, xm, ym, r, dt=0.001):
        xs, ys, _ = self.simulacija(dt)
        minimalna_udaljenost = float("inf")
        pogodak = False

        for x, y in zip(xs, ys):
            udaljenost_centar = math.sqrt(
                (x - xm)**2 +
                (y - ym)**2
            )
            if udaljenost_centar <= r:
                pogodak = True
            udaljenost_do_ruba = max(0, udaljenost_centar - r)
            if udaljenost_do_ruba < minimalna_udaljenost:
                minimalna_udaljenost = udaljenost_do_ruba

        # crtanje mete
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(xs, ys, label="Putanja")
        meta = plt.Circle(
            (xm, ym),
            r,
            fill=False,
            color="red",
            linewidth=2
        )

        ax.add_patch(meta)
        ax.plot(xm, ym, 'ro')
        ax.set_aspect('equal')
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.xticks(range(0, 101, 5))
        plt.yticks(range(0, 31, 5))
        plt.grid(True, linestyle='--')
        plt.legend()
        plt.show()

        if pogodak:
            print("META JE POGOĐENA")
        else:
            print("META NIJE POGOĐENA")
            print(
                f"Najbliža udaljenost od mete: "
                f"{minimalna_udaljenost:.4f} m"
            )
        return pogodak
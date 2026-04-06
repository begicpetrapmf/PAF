# Unaprijedite kod iz prethodnog zadatka koristeći modul matplotlib.pyplot tako da nacrtate unesene koordinate i 
# pravac koji prolazi kroz njih. 
# Ponudite u funkciji opciju da se graf prikaže na ekranu ili da se spremi kao PDF. 
# Dopustite korisniku da bira ime pod kojim će se spremiti graf.

import matplotlib.pyplot as plt
def koordinate_tocaka_za_pravac(x1,y1,x2,y2):

# y=kx+l -> l=y-kx ; k=(y2-y1)/(x2-x1)
    if x1==x2:
        print(f'Pravac je y={x1}.')
    else:
        k=(y2-y1)/(x2-x1)
        l=y1-k*x1
    
        x = [x1,x2]
        y = [y1,y2]

        plt.plot(x, y)
        plt.scatter([x1, x2], [y1, y2])
        plt.xlabel(f'x')
        plt.ylabel(f'y')
        plt.title(f'Graf pravca y={k}x+{l}')

        spremanje_prikaz = input(f'Upiši p za prikaz ili s za spremanje:')

        if spremanje_prikaz == 'p':
            plt.show()
        elif spremanje_prikaz == 's':
            ime_pdfa = input(f'Unesi ime datoteke (bez .pdf):')
            plt.savefig(ime_pdfa + ".pdf")
        else:
            print(f'Nisi napisao niti p niti s...')

koordinate_tocaka_za_pravac(7,3,8,4)
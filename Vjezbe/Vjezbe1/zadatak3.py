# Napišite program koji će korisnika tražiti da upiše (x, y) koordinate za dvije točke. 
# Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. 
# Nakon što je korisnik uspješno upisao dvije koordinate ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke.

import numpy as np
def koordinate_str(unos):
    while True:
        try:
            vrijednost_koordinate=float(input(unos))
            return vrijednost_koordinate
        except:
            print(f'Krivo. Ponovi.')

x1=koordinate_str(f'Unesi koordinatu x1:')
y1=koordinate_str(f'Unesi koordinatu y1:')
x2=koordinate_str(f'Unesi koordinatu x2:')
y2=koordinate_str(f'Unesi koordinatu y2:')

# y=kx+l -> l=y-kx ; k=(y2-y1)/(x2-x1)
if x1==x2:
    print(f'Pravac je y={x1}.')
else:
    k=(y2-y1)/(x2-x1)
    l=y1-k*x1
    print(f'Pravac je y={k}x+{l}')



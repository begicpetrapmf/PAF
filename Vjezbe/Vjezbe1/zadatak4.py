# Napišite funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije točke. 
# Neka ta funkcija na ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. Pozovite tu funkciju u svom programu.

def koordinate_tocaka_za_pravac(x1,y1,x2,y2):

# y=kx+l -> l=y-kx ; k=(y2-y1)/(x2-x1)
    if x1==x2:
        print(f'Pravac je y={x1}.')
    else:
        k=(y2-y1)/(x2-x1)
        l=y1-k*x1
        print(f'Pravac je y={k}x+{l}')

koordinate_tocaka_za_pravac(7,3,8,4)
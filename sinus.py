import math

def sinus(x, precision):
    ''' oblicza wartosc funkcji sinus dla zadanej wartosci konta używając rozwinięcia MacLaurina o zadanej precyzji
    (ilości wyrazów). Sinus jest obliczany dla kątów z pierwszej ćwiartki.
    Dla kątów z innych ćwiartek przeliczamy wartość sinusa korzystając z jego okresowości
    '''
    
    # najpierw sprowadzamy x do pierwszej ćwiartki
    # w przypadku x = <Pi, 2Pi>, wynik trzeba będzie przemnożyć przez (-1)
    x = x % (2 * math.pi)
    mnoznik = 1
    if x > math.pi:
        mnoznik = -1
        x = x - math.pi
    if x > math.pi / 2:
        x = math.pi - x

    # obliczamy licznik i mianownik dla kolejnych wyrazów rozwinięcia MacLaurina
    licznik = [x]
    mianownik = [1.0]
    x2 = x**2.0
    for n in range(1,precision):
        licznik.append((-1) * licznik[n-1]*x2)
        mianownik.append(mianownik[n-1] * 2*n*(2*n + 1))
    
    # sumujemy wyrazy i zwracamy wynik
    wynik = 0
    for ( l,m ) in zip(licznik,mianownik):
        wynik += l/m
    return wynik * mnoznik

while True:
    # wczytanie argumentów
    print("Podaj kąt: ", end = '')
    angle = float(input())
    while True:
        print("1 - stopnie, 2 - radiany")
        typ = input()
        if typ == '1' or typ == '2':
            break
    if typ == '1':
        angle = (angle / 360) * 2 * math.pi
    print("Podaj liczbę wyrazów w rozwinięciu Maclaurina: ", end = '')
    precision = int(input())

    # obliczenia i wydrukowanie wyników (rozwinięcie pierwszych 15 cyfr po przecinku)
    nasz_sin = "%.15f" % sinus(angle, precision)
    wbudowany_sin = "%.15f" % math.sin(angle)
    print("Obliczona przybliżona wartość sinus", nasz_sin)
    print("Obliczona wartość z math.sin()     ", wbudowany_sin)

    # na koniec porównamy zapis obu liczb i znajdziemy pierwszą cyfrę którą się różnią
    nasz_sin = nasz_sin[nasz_sin.find('.')+1:]
    wbudowany_sin = wbudowany_sin[wbudowany_sin.find('.')+1:]
    licznik = 0
    for (c1, c2) in zip (nasz_sin, wbudowany_sin):
        licznik += 1
        if c1 != c2:
            break
    if licznik < len(nasz_sin):
        print("Pierwsza różnica znaleziona na %d miejscu po przecinku." % licznik)
    else:
        print("Nie znaleziono różnicy.")
    print("Koniec? (T/N)")
    koniec = input()
    if koniec.lower() == 't':
        break

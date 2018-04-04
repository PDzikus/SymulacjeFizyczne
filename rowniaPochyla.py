# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:18:33 2018

@author: s13626
"""
import numpy as np
import matplotlib.pyplot as plt

# dane podstawowe
kroki = 500
deltaT = 0.01
masa = 1.0
g = 10.0
r = 2.0
alpha = 30.0
wysokosc = 20.0
alphaRadian = (alpha % 360) / 180 * np.pi

# wzory zależne od rodzaju bryły
I = masa * r**2 * 2 / 5
mnoznikI = 1.0 / (1 + 2.0 / 5)   # moment bezwladnosci: 1/2 dla walca, 2/5 dla kuli, 2/3 dla sfery
a = mnoznikI * g * np.sin(alphaRadian)
epsilon = a / r

szybkosc = np.empty((kroki,), dtype = float)
szybkosc[0] = 0
droga = np.empty((kroki,), dtype = float)
droga[0] = 0

omega = np.empty((kroki,), dtype = float)
beta = np.empty((kroki,), dtype = float)
omega[0] = 0
beta[0] = 0


energiaKinetyczna = np.empty((kroki,), dtype = float)
energiaKinetyczna[0] = 0



for moment in range(1,kroki):
    # rownania ruchu liniowego
    szybkoscPol = szybkosc[moment-1] + a*deltaT/2
    szybkosc[moment] = szybkosc[moment-1] + a * deltaT 
    droga[moment] = droga[moment-1] + szybkoscPol * deltaT
    # rownania ruchu obrotowego
    omegaPol = omega[moment-1] + epsilon * deltaT/2
    omega[moment] = omega[moment-1] + epsilon * deltaT
    beta[moment] = beta[moment-1] + omegaPol*deltaT
    
    energiaKinetyczna[moment] = masa * szybkosc[moment]**2 / 2 + I * omega[moment]**2 / 2 

x = droga * np.cos(alphaRadian)
y = wysokosc + r - droga * np.sin(alphaRadian)
energiaPotencjalna = y * g * masa

xCykloida = x  + r * np.sin(beta)
yCykloida = y + r * np.cos(beta)


moments = np.linspace(0,kroki*deltaT,kroki)
plt.figure(0)
plt.plot(moments, szybkosc, 'r')
plt.plot(moments, droga, 'g')

plt.figure(1)
plt.plot(moments, energiaKinetyczna, 'y')
plt.plot(moments, energiaPotencjalna, 'g')

plt.figure(2)
plt.plot(x, y)
plt.plot(xCykloida, yCykloida)
plt.axis('equal')
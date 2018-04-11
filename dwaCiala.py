# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:00:07 2018

@author: pawel
"""
import numpy as np
import matplotlib.pyplot as plt

masaOrbit = 10
distance = 10000
g = 10
kroki = 100000
deltaT = 0.01

def pierwszaPredkoscKosmiczna(g, distance):
    return np.sqrt(g * distance)

x = np.linspace(0, 10000, 500)
y = pierwszaPredkoscKosmiczna(g, x)

plt.figure(0)
plt.plot(x,y)
plt.title('Pierwsza prędkosć kosmiczna')
plt.ylabel('prędkosć w m/s')
plt.xlabel('wysokosć w m')
plt.show

distance = 100
vx = 0
vy = np.sqrt(2) * pierwszaPredkoscKosmiczna(g, distance)

x = np.empty((kroki,))
y = np.empty((kroki,))
x[0] = 0
y[0] = distance
ay = -g
ax = 0 

for moment in range(1, kroki):
    x[moment] = x[moment-1] + vx*deltaT
    y[moment] = y[moment-1] + vy*deltaT
    distance = np.sqrt(x[moment]**2 + y[moment]**2)
    ax = -g * x[moment]/distance
    ay = -g * y[moment]/distance
    vx = vx + ax * deltaT
    vy = vy + ay * deltaT

plt.figure(1)
plt.plot(x,y)
plt.axis('equal')
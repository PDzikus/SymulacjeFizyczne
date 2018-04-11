# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:00:07 2018

@author: pawel
"""
import numpy as np
import matplotlib.pyplot as plt

masaOrbit = 1
masaZiemi = 5.972 * 10**13
stalaG = 6.67 
promienZiemi = 6.37 * 10**6
g = 9.81
kroki = 100000
deltaT = 1
masy = stalaG * masaZiemi * masaOrbit


def pierwszaPredkoscKosmiczna(distance):
    ''' oblicza pierwsza prędkosć kosmiczną dla ciała na wysokosci "distance" nad poziomem morza '''
    return np.sqrt(stalaG*masaZiemi/(distance+promienZiemi))

x = np.linspace(0, 10000000, 100)
y = pierwszaPredkoscKosmiczna(x)
print('Pierwsza prędkosć kosmiczna: {}'.format(y[0]))
print('Druga prędkosć kosmiczna: {}'.format(np.sqrt(2)*y[0]))
plt.figure(0)
plt.plot(x,y)
plt.title('Pierwsza prędkosć kosmiczna')
plt.ylabel('prędkosć w m/s')
plt.xlabel('wysokosć w m nad ziemią')
plt.show

distance = promienZiemi + 1000
vx = 10700
vy = 0

x = np.empty((kroki,))
y = np.empty((kroki,))
x[0] = 0
y[0] = distance
f = masy / distance**2
fx = -f * x[0]/distance 
fy = -f * y[0]/distance
ax = fx / masaOrbit
ay = fy / masaOrbit

for moment in range(1, kroki):
    x[moment] = x[moment-1] + vx*deltaT
    y[moment] = y[moment-1] + vy*deltaT
    distance = np.sqrt(x[moment]**2 + y[moment]**2)
    f = masy / distance**2
    fx = -f * x[moment]/distance 
    fy = -f * y[moment]/distance
    ax = fx / masaOrbit
    ay = fy / masaOrbit
    vx = vx + ax * deltaT
    vy = vy + ay * deltaT

plt.figure(1)
plt.plot(x,y)

plt.axis('equal')
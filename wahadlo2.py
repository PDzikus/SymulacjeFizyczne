# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:21:56 2018

@author: pawel
"""
import math
import matplotlib.pyplot as plt
import numpy as np

# parametry startowe:
# kat, dlugosc wahadla, masa, grawitacja, delta T
alphaStart = 60
l = 3
m = 1
g = 10
deltaT = 0.01
kroki = 1000

def przyblizenie(steps, typ = 1):
    aLin = g / l
    alphaRadian = (180-alphaStart % 360) / 180 * math.pi

    alpha = np.empty((steps,), dtype = float)
    alpha[0] = alphaRadian
    omega = np.empty((steps,), dtype = float)
    omega[0] = 0
    epsilon = np.empty((steps,), dtype = float)
    epsilon[0] = m*g*math.sin(alpha[0])/l  

    if typ == 1:
        for moment in range(1,steps):
            omegaPol = omega[moment-1] + epsilon[moment-1]*deltaT/2
            alphaPol =alpha[moment-1] + omega[moment-1]*deltaT/2
            epsilonPol = aLin*math.sin(alphaPol)

            alpha[moment] = alpha[moment-1] + omegaPol*deltaT
            omega[moment] = omega[moment-1] + epsilonPol*deltaT
            epsilon[moment] = aLin*math.sin(alpha[moment-1])
    else:
        for moment in range(1,steps):
            epsilon[moment] = aLin * math.sin(alpha[moment-1])
            omega[moment] = omega[moment-1] + epsilon[moment-1]*deltaT
            alpha[moment] = alpha[moment-1] + omega[moment-1]*deltaT    

    return (alpha, omega)

# TODO    
fig, wykresy = plt.subplots(2,2)
for metoda in range(2):
    alpha, omega = przyblizenie(kroki, metoda)
    x = l*np.sin(alpha)
    y = l*np.cos(alpha) + l
    Ek = m * (omega**2) * (l**2) / 2
    Ep = m * g * y
    Ex = np.linspace(0, kroki*deltaT, kroki)

    wykresy[metoda,0].plot(x, y, 'b')
    wykresy[metoda,0].set_title('L = {0}, alpha = {1}, deltaT = {2}'.format(l, alphaStart, deltaT))
    wykresy[metoda,0].plot(x[0], y[0], 'r*',)
    wykresy[metoda,0].axis('equal')
    wykresy[metoda,0].grid()

    wykresy[metoda,1].plot(Ex, Ek, 'r', label = 'Ek')
    wykresy[metoda,1].plot(Ex, Ep, label = 'Ep')
    wykresy[metoda,1].grid()
    wykresy[metoda,1].legend(fancybox=True)
    wykresy[metoda,1].set_title('Energia kin(red) i pot (blue)')

plt.show()

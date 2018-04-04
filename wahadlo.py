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
alphaStart = 45
l = 3
m = 1
g = 10
deltaT = 0.01
kroki = 1000

# obliczenia pomocnicze wspólne dla wszystkich algorytmów
aLin = g / l
alphaRadian = (180-alphaStart % 360) / 180 * math.pi



def przyblizenieLepsze(steps):
    alpha = [alphaRadian]
    omega = [0]
    epsilon = [m*g*math.sin(alpha[0])/l]  

    x = [l*math.sin(alpha[0])]
    y = [l*math.cos(alpha[0]) + l]
    Ek = [0]
    Ep = [m * g * y[0]]

    for moment in range(1,steps):
        omegaPol = omega[moment-1] + epsilon[moment-1]*deltaT/2
        alphaPol =alpha[moment-1] + omega[moment-1]*deltaT/2
        epsilonPol = aLin*math.sin(alphaPol)

        alpha.append(alpha[moment-1] + omegaPol*deltaT)
        omega.append(omega[moment-1] + epsilonPol*deltaT)
        epsilon.append(aLin*math.sin(alpha[moment-1]))
        
        x.append(l*math.sin(alpha[moment]))    
        y.append(l*math.cos(alpha[moment])+l)
        Ek.append(m * (omega[moment]**2) * (l**2) / 2 )
        Ep.append(m * g * y[moment])

    return (x,y, Ek, Ep)

def przyblizenieEulera(steps):
    alpha = [alphaRadian]
    omega = [0]
    epsilon = [m*g*math.sin(alpha[0])/l]  

    x = [l*math.sin(alpha[0])]
    y = [l*math.cos(alpha[0]) + l]
    Ek = [0]
    Ep = [m * g * y[0]]
    
    for moment in range(1,steps):
        epsilon.append(aLin * math.sin(alpha[moment-1]))
        omega.append(omega[moment-1] + epsilon[moment-1]*deltaT)
        alpha.append(alpha[moment-1] + omega[moment-1]*deltaT)
    
        x.append(l*math.sin(alpha[moment]))    
        y.append(l*math.cos(alpha[moment])+l)
        Ek.append(m * (omega[moment]**2) * (l**2) / 2 )
        Ep.append(m * g * y[moment]) 
    
    return (x,y, Ek, Ep)
    

fig, wykresy = plt.subplots(2,2)
x, y, Ek, Ep = przyblizenieLepsze(kroki)

wykresy[0,0].plot(x, y, 'b')
wykresy[0,0].set_title('L = {0}, alpha = {1}'.format(l, alphaStart))
wykresy[0,0].plot(x[0], y[0], 'r*',)
wykresy[0,0].axis('equal')
wykresy[0,0].grid()
energy_x = np.linspace(0, kroki*deltaT, kroki)
wykresy[0,1].plot(energy_x, Ek, 'r')
wykresy[0,1].plot(energy_x, Ep)
wykresy[0,1].grid()
wykresy[0,1].set_title('Energia kinetyczna (red) i potencjalna (blue)')

x, y, Ek, Ep = przyblizenieEulera(kroki)
wykresy[1,0].plot(x, y, 'b')
wykresy[1,0].plot(x[0], y[0], 'r*',)
wykresy[1,0].axis('equal')
wykresy[1,0].grid()
wykresy[1,1].plot(energy_x, Ek)
wykresy[1,1].plot(energy_x, Ep)
wykresy[1,1].grid()


plt.show()

import numpy as np
import matplotlib.pyplot as plt

# dane początkowe
masa = 1
gx = 0
gy = -10
k = 0.6
dt = 0.1

def Fo(v):
	return -k*v
	
Vx = [10]
Vy = [10]
Sx = [0]
Sy = [0]
Ax = []
Ay = []

moment = 0
while (Sy[-1] >= 0):
	Ax.append(masa*gx + Fo(Vx[-1]))
	Ay.append(masa*gy + Fo(Vy[-1]))
	Vx_t2 = Vx[moment] + Ax[moment]*dt/2
	Vy_t2 = Vy[moment] + Ay[moment]*dt/2
	Sx.append(Sx[moment]+Vx_t2*dt)
	Sy.append(Sy[moment]+Vy_t2*dt)
	Ax_t2 = masa*gx + Fo(Vx_t2)
	Ay_t2 = masa*gy + Fo(Vy_t2)
	Vx.append(Vx[moment] + Ax_t2*dt)
	Vy.append(Vy[moment] + Ay_t2*dt)
	moment += 1
	print (Sy[moment], Sx[moment])

x = np.array(Sx)
y = np.array(Sy)
plt.plot(x,y, 'r-')
plt.plot(x,y, 'b+')
plt.grid()
plt.show()
	

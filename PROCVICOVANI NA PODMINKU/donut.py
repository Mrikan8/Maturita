import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Nastavení parametrů donutu
R = 1
r = 0.3
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Výpočet souřadnic donutu
X = (R + r * np.cos(theta)) * np.cos(phi)
Y = (R + r * np.cos(theta)) * np.sin(phi)
Z = r * np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Funkce pro aktualizaci rotace
def update(num, X, Y, Z, ax):
    ax.clear()
    ax.plot_surface(X, Y, Z, color='b')
    ax.view_init(elev=30, azim=num)

ani = animation.FuncAnimation(fig, update, frames=360, fargs=(X, Y, Z, ax), interval=50)
plt.show()
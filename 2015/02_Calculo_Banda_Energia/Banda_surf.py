from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-1.9,1.9, 0.1)#0.02 fica bom o grafico... mas fica lento
Y = np.arange(-1.9, 1.9, 0.1) #0.02 fica bom o grafico... mas fica lento

X, Y = np.meshgrid(X, Y)

Z = (1+4*np.cos(np.sqrt(3)*X*2.456/2.0)*np.cos(Y*2.456/2.0)+4*(np.cos(Y*2.456/2.0))**2)**(1.0/2.0)
G = -1*(1+4*np.cos(np.sqrt(3)*X*2.456/2.0)*np.cos(Y*2.456/2.0)+4*(np.cos(Y*2.456/2.0))**2)**(1.0/2.0)


surf = ax.plot_surface(X, Y,Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False,alpha=1)
surf = ax.plot_surface(X, Y,G, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False,alpha=1)

#obs: voce pode ir no site do matplotlib e ver a tabelac de cm. (colormap)... eu escolhi coolwarm

ax.set_zlim(-1.5, 1.5)

#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

#fig.colorbar(surf, shrink=1, aspect=1)

plt.show()


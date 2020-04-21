import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

wavelength = 630e-9
D = 0.05
distance = np.arange(-20,20,0.5)
k = 2*np.pi/wavelength  

def michelson_intensity_x(x,kk, dd):
    intensity = (1+np.cos(2*kk*dd*np.cos(x/D)))
    return x
  
def michelson_intensity_y(y,kk, dd):
    intensity = (1+np.cos(2*kk*dd*np.cos(y/D)))
    return y

def michelson_intensity_z(x, y, kk, dd):
    r = np.sqrt(x**2+y**2)
    intensity = (1+np.cos(2*kk*dd*np.cos(r/D)))
    return r

X = [michelson_intensity_x(x,k,D) for x in distance]
Y = [michelson_intensity_y(y,k,D) for y in distance]
X, Y = np.meshgrid(X, Y)
Z = np.sin([[michelson_intensity_z(x,y,k,D) for x in distance]for y in distance]) 

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)
plt.xlabel("Distànica(mm)")
plt.ylabel("Distànica(mm)")
ax.set_zlabel("Intensitat(W/m^2")
plt.show()
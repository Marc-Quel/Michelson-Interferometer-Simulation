import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, widgets

wavelength = 630e-9
theta_max = 0.15
D = 0.5
x_max = D*theta_max
distance = np.arange(-x_max,x_max,x_max*0.01)
k= 2*np.pi/wavelength

def michelson_intensity(x,y,kk,dd):
    r = np.sqrt(x**2+y**2)
    intensity = (1+np.cos(2*kk*dd*np.cos(r/D)))
    return intensity

steps = [n/16 for n in range(9)]
max_d_wl = [(50+i)*wavelength for i in steps]
mdi_n_wl = [[[michelson_intensity(x,y,k,d)for x in distance]for y in distance]for d in max_d_wl]

ims = []

def mdi_nframes(d_miralls):
    image = plt.imshow(mdi_n_wl[d_miralls],cmap="viridis",animated = True)
    ims.append([image])
    plt.xlabel("Distància(mm)")
    plt.ylabel("Distància(mm)")
    cbar = plt.colorbar(image)
    cbar.ax.set_ylabel("Intensitat(W/m^2)")
    plt.show()
interact(mdi_nframes,d_miralls=widgets.IntSlider(min=0,max=8,step=1,value=2))

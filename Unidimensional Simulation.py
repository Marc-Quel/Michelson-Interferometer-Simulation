import matplotlib.pyplot as plt
import math as m
import numpy as np
from matplotlib.widgets import Slider

distance = [i for i in np.arange(0,0.2,0.001)]
wavelength = 630e-9
k = 2*m.pi/wavelength
d = 0.05


def michelson_intensity(x, kk, dd):
  intensity = (1+np.cos(2*kk*d*np.cos(x/2*d)))
  return intensity

  
vector_distance_intensity = [michelson_intensity(x,k,d) for x in distance]


fig,axes = plt.subplots(figsize=(8.6,4.8))
plt.subplots_adjust(left=0.1,bottom=0.35)

interferencia, = plt.plot(distance,vector_distance_intensity)
plt.xlabel("Distànica de la pantalla(m)")
plt.ylabel("Intensitat(W/m^2)")

    
axdistance = plt.axes([0.25, 0.2, 0.6, 0.05])
axwavelength = plt.axes([0.25, 0.1, 0.6, 0.05])


sdistance = Slider(ax = axdistance,
              label = "Distància entre miralls",
              valstep = d/100,
              valmax = d,
              valmin = d/2,
              valinit = 3*d/2 )

swavelength = Slider(ax = axwavelength,
              label = "Longitud d'ona",
              valstep = wavelength/10,
              valmax = wavelength,
              valmin = wavelength/2,
              valinit = wavelength/2 )

def update(val):
    dval = sdistance.val
    wval = swavelength.val
    interferencia.set_ydata([(1+np.cos(2*(2*m.pi/wval)*dval*np.cos(x/2*dval)))for x in distance])
    fig.canvas.draw_idle()
    
sdistance.on_changed(update)

swavelength.on_changed(update)


plt.show()
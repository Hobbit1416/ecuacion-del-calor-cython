"""
/*************************************************
** 			Universidad Sergio Arboleda 		**
** 	Escuela de Ciencias exactas e Ingeniería 	**
**  Ingeniería de Sistemas y Telecomunicaciones **
**												**
**      Parcial 3 Computación paralela          **
**                      y                       **
**                 distribuida                  **
**												**
** Autores: 									**
**	  -Valentina Del Pilar Franco 				**
**    valentina.franco01@correo.usa,edu.co 		**
**    -Emmanuel Mora 							**
**    emmanuel.mora01@correo.usa.edu.co 		**
**    -Juan Pablo Blanco 						**
**    juan.blanco01@correo.usa.edu.co 			**
**    -Jofre Eduardo Oliveros                   **
**    jofre.oliveros01@correo.usa.edu.co        **
**                                              **
** Fecha: 28/05/21                              **
**************************************************/
"""

#cython: language_level=3
import matplotlib

#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
cimport cython
import numpy as np
cimport numpy as np


# Set the colormap
#plt.rcParams['image.cmap'] = 'BrBG'

cdef evolve( u, u_previous, float a, float dt, float dx2, float dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    cdef int n, m = len(u) #np.shape(u)

    #print(type(n))

    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
             (u_previous[i+1, j] - 2*u_previous[i, j] + \
              u_previous[i-1, j]) / dx2 + \
             (u_previous[i, j+1] - 2*u_previous[i, j] + \
                 u_previous[i, j-1]) / dy2 )
    u_previous[:] = u[:]
    
    #contador+=1
    #print("Prueba Cython: ", u_previous.shape, contador)
def iterate(field, field0, a, dx, dy, timesteps, image_interval):
    """Run fixed number of time steps of heat equation"""

    dx2 = dx**2
    dy2 = dy**2
    
    

    # For stability, this is the largest interval possible
    # for the size of the time-step:
    dt = dx2*dy2 / ( 2*a*(dx2+dy2) )    

    for m in range(1, timesteps+1):
        evolve(field, field0, a, dt, dx2, dy2)
        #if m % image_interval == 0:
            #write_field(field, m)

def init_fields(filename):
    # Read the initial temperature field from file
    field = np.loadtxt(filename)
    field0 = field.copy() # Array for field of previous time step
    return field, field0

#def write_field(field, step):
    #plt.gca().clear()
    #plt.imshow(field)
    #plt.axis('off')
    #plt.savefig('heat_{0:03d}.png'.format(step))

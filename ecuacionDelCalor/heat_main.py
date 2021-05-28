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

from __future__ import print_function
import time
import argparse
import sys
import os
#from heat import init_fields, write_field, iterate
import heat
import Cy_heat


def main(objeto, input_file='bottle.dat', a=0.5, dx=0.1, dy=0.1, 
         timesteps=200, image_interval=4000):

    # Initialise the temperature field
    field, field0 = objeto.init_fields(input_file)

    #print("Heat equation solver")
    #print("Diffusion constant: {}".format(a))
    #print("Input file: {}".format(input_file))
    #print("Parameters")
    #print("----------")
    #print("  nx={} ny={} dx={} dy={}".format(field.shape[0], field.shape[1],
    #                                         dx, dy))
    #print("  time steps={}  image interval={}".format(timesteps,
    #                                                     image_interval))

    # Plot/save initial field
    #write_field(field, 0)
    # Iterate
    t0 = time.time()
    objeto.iterate(field, field0, a, dx, dy, timesteps, image_interval)
    t1 = time.time()
    # Plot/save final field
    #write_field(field, timesteps)
	
    #print("{0}".format(t1-t0))
    return (t1-t0)


if __name__ == '__main__':

    #botella=int(sys.argv[1])
    #nEjecuciones=int(sys.argv[2])
    #for i in range(nEjecuciones):
    #    if(botella==1):
    #        peque()
    #    elif(botella==2):
    #        media()
    #    elif(botella==3):
    #        larga()
    parser = argparse.ArgumentParser(description='Heat equation')
    parser.add_argument('-dx', type=float, default=0.01,
                        help='grid spacing in x-direction')
    parser.add_argument('-dy', type=float, default=0.01,
                        help='grid spacing in y-direction')
    parser.add_argument('-a', type=float, default=0.5,
                        help='diffusion constant')
    parser.add_argument('-n', type=int, default=200,
                        help='number of time steps')
    parser.add_argument('-i', type=int, default=4000,
                        help='image interval')
    parser.add_argument('-f', type=str, default='bottle.dat', 
                        help='input file')
    parser.add_argument('-e', type=int, default=1,
                        help='number of executions')

    args = parser.parse_args()
    totalPy = 0
    totalCy = 0
    for i in range(args.e):
        tPy = main(heat,args.f, args.a, args.dx, args.dy, args.n, args.i)
        totalPy+=tPy
        tCy = main(Cy_heat,args.f, args.a, args.dx, args.dy, args.n, args.i)
        totalCy+=tCy
    
    promPy = totalPy/args.e
    promCy = totalCy/args.e

    file = open("Soluciones/"+args.f+".txt", "w")
    file.write("{0}".format(promPy) + os.linesep)
    file.write("{0}".format(promCy) + os.linesep)
    file.write("{0}".format(promPy/promCy))
    file.close()
    #heat_main.py [-h] [-dx DX] [-dy DY] [-a A] [-n N] [-i I] [-f F]
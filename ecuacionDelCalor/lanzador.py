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

import sys
from __future__ import print_function
import time
import argparse

#from heat import init_fields, write_field, iterate
from heat import init_fields, iterate
import heat_main


if len(sys.argv)!=2:
    print("El programa debe recibir un argumento, el número de ejecuciones que se harán.")
else:
    b=int(sys.argv[1])
    n=int(sys.argv[2])
    potencia(b,n)
if __name__ == '__main__':

    # Process command line arguments
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

    args = parser.parse_args()

    main(args.f, args.a, args.dx, args.dy, args.n, args.i)
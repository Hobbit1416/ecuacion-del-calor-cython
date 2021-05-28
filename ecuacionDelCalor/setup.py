"""
/*************************************************
** 			Universidad Sergio Arboleda 		        **
** 	Escuela de Ciencias exactas e Ingeniería 	  **
**  Ingeniería de Sistemas y Telecomunicaciones **
**												                      ** 
**      Parcial 3 Computación paralela          **
**                      y                       **
**                 distribuida                  **
**												                      **
** Autores: 									                  **
**	  -Valentina Del Pilar Franco 			      	**
**    valentina.franco01@correo.usa,edu.co  		**
**    -Emmanuel Mora 					              		**
**    emmanuel.mora01@correo.usa.edu.co     		**
**    -Juan Pablo Blanco 					            	**
**    juan.blanco01@correo.usa.edu.co 		    	**
**    -Jofre Eduardo Oliveros                   **
**    jofre.oliveros01@correo.usa.edu.co        **
**                                              **
** Fecha: 28/05/21                              **
**************************************************/
"""
#from distutils.core import setup, Extension
#from Cython.Build import cythonize


#setup(ext_modules=exts)
from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from distutils.extension import Extension
import numpy 

#exts = (cythonize('heat.pyx'))
exts=(cythonize('Cy_heat.pyx'))
setup(name = 'heat', cmdclass={"build_ext": build_ext},
  ext_modules=exts, 
  include_dirs=[numpy.get_include()])
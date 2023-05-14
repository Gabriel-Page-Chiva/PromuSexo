import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datoncios = pd.read_excel('saltoncio_promu.xlsx')
#la data del salto de robinardo

t = np.array(datoncios['t'])
a = np.array(datoncios['a'])

ax = np.array(datoncios['ax'])

ay = np.array(datoncios['ay'])
az = np.array(datoncios['az'])

plt.figure()
plt.plot(t,ax)
plt.plot(t,ay)
plt.plot(t,az)
plt.plot(t,a)
plt.grid('on')
plt.xlabel('tiempo [s]')
plt.ylabel('aceleracopm [m/s$^2$]')
plt.title('CARAPENES')
plt.legend(['$a_x$','$a_y$','$a_z$','$|a|$'])
plt.show()


#-------------CORRECCION--------------

a_modulo = np.abs(a)
a_fixed=a_modulo*np.sign(ay)

plt.figure()
plt.plot(t,a_fixed)
plt.plot(t,a,'--')
plt.grid(True)
plt.xlabel('tiempo [s]')
plt.ylabel('aceleracopm [m/s$^2$]')
plt.title('mod aceleracion medida')
plt.legend(['$|a|$ Corregida','$|a|$ Original'])
plt.show()


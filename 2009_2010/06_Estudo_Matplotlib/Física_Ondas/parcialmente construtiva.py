# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.001)


A=5
B=10


y1=A*np.sin(x)
y2=B*np.sin(x+np.pi/2)#coloquei uma fase de 180� para poder anular com a onda y1 , assim temos uma onda destruitiva

y=y1+y2

plt.plot(x,y,'y-',x,y1,'r-',x,y2,'b-',20)


plt.show()
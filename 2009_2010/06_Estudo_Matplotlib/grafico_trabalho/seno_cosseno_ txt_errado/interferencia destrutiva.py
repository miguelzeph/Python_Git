# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,100,0.001)


A=5

y=A*np.sin(x)+A*np.sin(x+np.pi)


plt.plot(x,y,'ro',20)

plt.show()
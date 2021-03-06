#!/usr/bin/env python
# python
import matplotlib.pyplot as plt
import numpy as np


dt = 0.01
t = np.arange(0,10,dt)
nse = np.random.random(len(t))
r = np.exp(-t/0.05)

cnse =np.convolve(nse, r)*dt
cnse1 = cnse[:len(t)]
s = 0.1*np.sin(2*np.pi*t) + cnse1

plt.subplot(211)
plt.plot(t,s)
plt.subplot(212)
plt.psd(s, 500, 1)

plt.show()
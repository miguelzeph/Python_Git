﻿import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

ax = plt.subplot(111) # nem precisa... (largura,comprimento,numero de grafico)
plt.subplots_adjust(left=0.25, bottom=0.25)
#------
dados = [2,2,4,5,5,5,5,5,5,7,8,9,9]
xm = np.mean(dados)#media
dp = np.std(dados)#desvio padrao
#-----


t = np.arange(0.0, 10.0, 0.1)
A = xm#media
f = dp#desvio padrao

y = 1/(f*np.sqrt(2*np.pi))*np.exp((-1/2)*((t-A)/f)**2)
l, = plt.plot(t,y, lw=2, color='red')#tem que ter a virgula...
plt.axis([0, 10, 0, 0.5])#([xi,xf,yi,yf])

axcolor = 'lightgoldenrodyellow' # pode colocar (r,g,b) , e a cor dos botoes tela (part branca)
axfreq = plt.axes([0.25, 0.10, 0.65, 0.03], axisbg=axcolor)#(pos(x da barra),pos(y da barra),comprimento,largura)
axamp  = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)
#barra de frequencia
sfreq = Slider(axfreq, 'Desvio Padrao', -10, 10, valinit=f)# valinit e o traco vermelho que marca inicial (..,..,valor_i,valor_f,..)
#barra de amplitude
samp = Slider(axamp, 'Media', -20, 20.0, valinit=A)

def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(1/(freq*np.sqrt(2*np.pi))*np.exp((-1/2)*((t-amp)/freq)**2))
    #l.set_xdata(-t) Teste para entender o funcionamento
    plt.draw() # refaz o grafico
sfreq.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04]) #posicao do botao...
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
def reset(event):
    sfreq.reset()#volta pARA O VALINIT
    samp.reset()
button.on_clicked(reset) #precisa de um click

rax = plt.axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)#(pos(x da barra),pos(y da barra),comprimento,largura)
button1 = RadioButtons(rax, ('red', 'blue', 'green'), active=0)#se vc colocar active=1 ele vai para o blue... 2 ele vai para green
def colorfunc(label):
    l.set_color(label)
    plt.draw()
button1.on_clicked(colorfunc)

plt.show()
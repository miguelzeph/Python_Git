from visual import *





v=1
dv=0.001

Sol = sphere(pos = (200,0,0),radius = 60,color=(1,v,0),material = materials.emissive)

local_light(pos=Sol.pos,color=(1,1,1))

Terra = sphere(radius = 15,material = materials.earth)

quadro = frame(pos=(100,0,100))

Lua = sphere(frame=quadro,pos=Terra.pos,radius = 2,material = materials.rough)
#trajetoria = curve(color=(1,1,1))
trajetoria1 = curve(color=(1,1,1))

t=0
dt = 0.01
r=35


p=0
dp = 0.001


nucleo = Sol.radius
nc=0.1

while True:
	rate(100)
	
	t=t+dt
	
	p=p+dp
	
	#Elipse
	X=sin(p)*350
	Z=cos(p)*200
	
	#Sol---- Melhor nao...
	#nucleo = nucleo + nc
	
	#if nucleo > 70:
	#	nc = -nc
	#if  nucleo < 60:
	#	nc = -nc
	
	#Sol.radius = nucleo
	
	#COr_SOl
	v = v - dv
	
	if abs(v) >=1 :
		dv = -dv
	elif abs(v) < 0.8:
		dv = -dv
	
	Sol.color=(1,v,0)
	
	
	
	
	
	#Lua----------------
	x =sin(t)*r 
	z =cos(t)*r
	
	Lua.pos =(x,0,z)
	
	
	quadro.pos=Terra.pos #como se fosse um ponto fixo
	#------------------
	
	Terra.pos =(X,0,Z)
	
	Terra.rotate(axis=(0,1,0), angle=0.008)
	
	#trajetoria.append(Lua.pos)
	trajetoria1.append(Terra.pos)
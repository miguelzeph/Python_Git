#Resumo: a vantagem deste modelo ao anterior a ele e que sempre a bola vermelha tem que cair por ultimo , mas agora
#eu tentarei fazer que qual seja a bola que cair antes ou depois por ultima , pause o sistema...



from visual import * #assim n preciso colocar vs ou visual... blabla


# blue(azul) ->  coloquei nada...,green->verde , red->vermelho 
ball=sphere(pos=(-50,0,0),radius=2,color=color.blue)#(0,2,0) fiz uma caixa com 2 de altura
ballg=sphere(pos=(-50,0,0),radius=2,color=color.green)
ballr=sphere(pos=(-50,0,0),radius=2,color=color.red)



ground=box(pos=(0,-3,0),size=(250,3,50))


#-----------Dados----------------
seconds=0
g=0
r=0
dt= 0.01
v0=40
#---------------Bola azul-------
angulo=45
angulo=angulo*(pi/180)
vx=v0*cos(angulo)
vy=v0*sin(angulo)
#--------------Bola Verde ------
angulog=75
angulog=angulog*(pi/180)
vxg=v0*cos(angulog)
vyg=v0*sin(angulog)
#------------Bola vermelha------
angulor=60
angulor=angulor*(pi/180)
vxr=v0*cos(angulor)
vyr=v0*sin(angulor)

#---------------------------------------------
finished= False

while not finished:
	rate(100)
	seconds=seconds+dt
	g=g+dt
	r=r+dt
	
	#bola azul
	alcance=-50+vx*seconds
	altura= 0+vy*seconds-0.5*9.8*seconds**2
	ball.pos=vector(alcance,altura,0)
	
	#bola verde
	alcanceg=-50+vxg*g
	alturag= 0+vyg*g-0.5*9.8*g**2
	ballg.pos=vector(alcanceg,alturag,0)
	#bola vermelha
	alcancer=-50+vxr*r
	alturar= 0+vyr*r-0.5*9.8*r**2
	ballr.pos=vector(alcancer,alturar,0)
	if altura <=0:
		seconds=seconds-dt#unica jogada que achei , pois se n fosse assim eu teria de dar um print e achar valor depois chamar seconds = a tal... assim eu mantenho o seconds constante ate chegao fim o programa.
		
		#------------aqui em baixo esta a jogada ruin ...-------------
		#print seconds
		#seconds=3.43
		#--------------------------------------------------------------
		
		ball.pos=vector(alcance,0,0)
		
	if alturag <=0:
		g=g-dt #analogamente , irei manter constante....
		
		#--------------jogada ruim-----------------------------------
		#print g
		#g=4.85
		#------------------------------------------------------------
		
		ballg.pos=vector(alcanceg,0,0)
	
	if alturar <=0:
	
		r=r-dt #analogamente , irei manter constante ate todos ficarem em altura zero....
		
		#--------------jogada ruim-----------------------------------
		#print r
		#r=....
		#------------------------------------------------------------
		
		ballr.pos=vector(alcancer,0,0)
		
	#quanto tudo estiver em y=0 ai sim , podemos efetuar o calculo
	if (altura <=0 and alturag <=0 and alturar <=0):#quando altura for igual ou menor a 0 , perceba q esta dentro do loop , entao no primeiro(comeco) zero ele n ira parar...
	
		finished=True#vai brecar o loop
		#bola azul
		alcance_max=alcance-(-50)
		label(pos=(0,20,0),text='alcance maximo da bola azul='+str(alcance_max),color=color.blue)
		#bola verde
		alcance_max=alcanceg-(-50)
		label(pos=(0,30,0),text='alcance maximo da bola verde='+str(alcance_max),color=color.green)
		#bola vermelha
		alcance_max=alcancer-(-50)
		label(pos=(0,40,0),text='alcance maximo da bola vermelha='+str(alcance_max),color=color.red)
		
	
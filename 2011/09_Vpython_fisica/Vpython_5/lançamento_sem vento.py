from visual import * #assim n preciso colocar vs ou visual... blabla

#scene.width=800#largura
#scene.height=600#altura

#scene.autoscale=0
#scene.range=(100,100,100)
#scene.center=(0,40,0)




ball=sphere(pos=(-50,0,0),radius=2,color=color.blue)#(0,2,0) fiz uma caixa com 2 de altura
ground=box(pos=(0,-1,0),size=(100,1,100))

#-----------Dados----------------
seconds=0
dt= 0.01
v0=33.6
angulo=30
angulo=angulo*(pi/180) #degree
vx=v0*cos(angulo)
vy=v0*sin(angulo)
vz=0

#agora iremos modificar , em vez de utilizar vx e vy , iremos utilizar um vetor que tem todos juntos ... fica mais elegante
vel_jogada=vector(vx,vy,vz)
#vento esta vindo de lado...
vel_vento=vector(0,0,-2)
#soma vetorial....  somar vetor jogado com o vetor do vento...

#vel_total= vel_jogada + vel_vento


#----------Dicas de Fisica-------------------

#-->Quanto tempo a bola fica no ar ?<---

#y=y0+v*t-0.5*9.8*t**2 , onde : v=v0*sen(alfa)
#jogando valor de y final (queremos quando ele estiver no chao).... ou seja y=0... 
#perceba que encontraremos para y=0 2 raizes , t=0 e t= ao que precisamos achar...
#isolando tudo temos e sus y0 = 0, encontramos t=v0sen(alfa)/4.9

#--->qual alcance max ?<---

#subs tempo que fica no ar na eq da posic do eixo x ... logo

#x(MRU)=x0+v*t , v=v0*cos(alfa)

#temos  que alcance maximo e : x-x0=v0^2*cos(alfa)*sen(alfa)/4.9

#foi assim que eu achei um valor aproximado para a v0 fazer o percurso inteiro ate chegar na outra ponta... 
#perceba que a placa tem 100 m de comprimento... (100 de x comecando no centro do eixo , logo e -50 pra um lado e +50 para outro... bem logico)

#assim quando eu achei que ...

#v0=((100-0)*4.9/(cos(alfa)*sen(alfa)))^(1/2) = aproximadamente 33.6


#---> para achar a distancia max foi preciso utilizar as formulas ?<---

#n , uma vez que o computador vai armazenando os valores na func "alcance" ,
#como saiu do loop sgnifica que ja temos alcance que ele percorreu , logo , (alcance -(-x0))

#---------------------------------------------
finished= False

while not finished:
	rate(100)
	seconds=seconds+dt
	
	alcance=-50+vel_jogada.x*seconds 
	
	altura= 0+vel_jogada.y*seconds-0.5*9.8*seconds**2
	
	#fazer variar o vetor em x e y...
	ball.pos=vector(alcance,altura,0)
	
	if altura <=0:#quando altura for igual ou menor a 0 , perceba q esta dentro do loop , entao no primeiro zero ele n ira parar...
		
		alcance_max=alcance-(-50)
		finished=True#parar o loop
		label(pos=(0,30,0),text='alcance maximo='+str(alcance_max))
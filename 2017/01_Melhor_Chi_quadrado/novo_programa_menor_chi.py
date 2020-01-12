﻿from __future__ import division
import numpy as np
import scipy.integrate as si
import os

def raman0(x,L,w0,wo,Gama):
	return ((np.exp(-(x**2)*((L)**2)/4))*(x**2)*4*np.pi)/(((w0-(wo-120*((x/(2*np.pi))**2)))**2)+((Gama/2)**2))

def raman1(x,Io,L,w0,wo,Gama):
	return Io*((np.exp(-(x**2)*((L)**2)/4))*(x**2)*4*np.pi)/(((w0-(wo-120*((x/(2*np.pi))**2)))**2)+((Gama/2)**2))

principal = os.getcwd()
#os.chdir('./dados')
os.chdir('./Dados')

lista=os.listdir('.')
txts=[]

for i in range(0,len(lista)):

	if (lista[i].find('.txt') == -1):
	#if (lista[i].find('.txt') == -1):#find quando n tem ele retorna -1
		continue
	else:
		txts.append(lista[i])
		
for n in range(0,len(txts)):
	arq_entrada=open('./'+txts[n],'r')
	arq_dados=arq_entrada.readlines()
	arq_entrada.close()
	

	x = []
	y = []

	for i in range(0,len(arq_dados)):
		
		vetor = arq_dados[i].split(' ')
		
		x.append(float(vetor[0]))
		
		y.append(float(vetor[1]))


	DR=[]
	IR=[]


	for j in range(0,len(arq_dados)):

		DR.append(x[j])
		
		IR.append(y[j])

	a=0.54 #nm Si-c	

	Arm_L=[]
	Arm_Gama=[]
	#Arm_wo=[]
	CHI=[]
	chi=0
	os.chdir(principal)
	os.chdir('./Analise')
	V = open('./menor_chi_'+str(txts[n]),'w')
	V.write('wo(1/cm) L(nm) Gama(1/cm) Chi-quad\n')
	
	
	for i in range(0,len(IR)):
		
		if IR[i] == max(IR):
					
			wpico= DR[i]
	wo = wpico
	l=np.arange(5,20,0.5)
	g=np.arange(4.5,9,0.5)
		
	#comeca aqui !
	for largura in g:

		Gama = largura
			
			
		for cristalito in l:
				
			L = cristalito
				
			#Resolucao da Integral
				
			QTX=DR
			QTY=[]

			for i in range(0,len(DR)):
								
				w0 = DR[i]
				a = 0
				b = 1
				args0=(L,w0,wo,Gama)
				Q0= si.quad(raman0,a,b,args0)# primeira Integral*****
				QTY.append(Q0[0])
						   
			QT0max = max(QTY) 
			IRRmax = max(IR)

			Io=IRRmax/QT0max 
				
				
			QTX1=QTX
			QTY1=[]


			for i in range(0,len(DR)):
				w0=DR[i]
					
				args1=(Io,L,w0,wo,Gama)
				a = 0
				b = 1
				Q = si.quad(raman1,a,b,args1)
				QTY1.append(Q[0])

			IT = QTY1	
			
			#Programa Chi-quad
				
			for i in range(0,len(IT)):
		
				chi= chi + (((IT[i]-IR[i])**2)/IR[i])
				
			grau = chi/len(IR)
			Arm_L.append(L)
			Arm_Gama.append(Gama)
			#Arm_wo.append(wo)
			CHI.append(grau)
				
			chi=0 # AQUI ESTA A SOLUCAO...
		
		#Qual o Menor Chi-quad para este valor de L ?
		for j in range(0,len(CHI)):

			if CHI[j] == min(CHI):
							
				gravar ='%03.2f   %04.2f   %02.2f   %f\n'%(wo,Arm_L[j]*0.54,Arm_Gama[j],CHI[j])
				V.write(gravar)
				print gravar
		#Reset		
		Arm_L=[]
		Arm_Gama=[]
		#Arm_wo=[]
		CHI=[]
	
	os.chdir(principal)
	os.chdir('./Dados')	
	V.close()
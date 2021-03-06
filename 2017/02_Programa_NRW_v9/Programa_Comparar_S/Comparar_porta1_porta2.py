#Criar Par-s FONTE: LIVRO NRW

from __future__ import division
import os 
import numpy as np
import matplotlib.pyplot as plt



#---------------LER ARQUIVO TXT NA PASTA-------------
TXT =[]

for arquivo in os.listdir('.'):
	if arquivo[len(arquivo)-4:] == '.txt':
		TXT.append(arquivo)
		
		
arq = open(TXT[0],'r')
ler = arq.readlines()
arq.close()
#----------------------------------------------------



# L1 = Referencia da porta 1 ... L = d = espessura da amostra .... L2 = ref da porta 2....
#Portanto, se vc encostar amostra de 5mm na porta 1, sobrara 5 mm em L2.. pois o offset tem 10 mm

#offset = 9.76mm
#-----------------------------Constantes BASE--------------


L1 = 0e-3 #[m] #Plano de referencia porta 1
L2 = 4.76e-3 #[m]   #Plano de referencia porta 2

d = 5e-3 #[m] #Espessura da amostra


e_a = 2.04 -0j #Analitico teflon
u_a = 1.0 - 0j   #Analitico teflon




a =22.86e-3 #[m] # base maior do guia de onda (Banda-X)
c =2.998e8 #[m/s] #velocidade da Luz

u0=4*np.pi*1e-7 # permeabilidade do vacuo

freq_corte = 6.56e9 # [Hz]

onda_cut= c/freq_corte #[m] #lambda de corte
#---------------------------------------------------------




#-------------------------VETORES-1-------------------		
F=[] #frequencia [Hz] DE CALCULO
F_grafic=[] #FREQUENCIA PARA PLOTAR EM [GHz]


s11=[] # real - j imag
s21=[] # real - j imag

s11c=[] # real - j imag (Adaptado)
s21c=[] # real - j imag (Adaptado)


s22=[] # real - j imag
s12=[] # real - j imag

s22c=[] # real - j imag (Adaptado)
s12c=[] # real - j imag (Adaptado)

#-------------------------

#----------------------------ORGANIZAR PARAMETROS-S em VETOR

#ler S11 e S21
ler1_col=1
ler2_col=2
ler3_col=5
ler4_col=6
#Ler S22 e S12
ler5_col=3
ler6_col=4
ler7_col=7
ler8_col=8


for i in range(0,len(ler)):
	
	
	dados = ler[i].split(',')
	
	f_colocar = float(dados[0])
	
	F.append(f_colocar)
	
	
	
	

	#----------------------------------------------------------------------------
	#lambda zero = comprimento de onda no vacuo
	onda = c/(f_colocar) # [m]
	
	
	#Constante de propagacao da onda no espaco livre
	gama0 = (2j*np.pi)*np.sqrt((1.0)/(onda**(2.0))-(1.0)/(onda_cut**(2.0)))
	
	#Constante de propagacao da onda no material
	gamaX = (2j*np.pi/onda)*np.sqrt(e_a*u_a-(onda**2.0)/(onda_cut**2.0))
	
	
	#Impedancia analitica do vacuo
	z_a0= (1j*u0*2*np.pi*f_colocar)/(gama0)
	#impedancia Analitica do Material
	z_ma = ((1j*2*np.pi*f_colocar*u_a*u0)/(gamaX))/(z_a0) #z_a0 normliza
	
	#Coeficiente de Refelxao Analitico
	Ca = (z_ma-1)/(z_ma+1)
	#Coeficiente de transmissao Analitico
	ta = np.exp(-gamaX*d)
	
	#--------------------------------------------------------------------------
	
	
	R1 = np.exp(1*gama0*L1) #constantes
	R2 = np.exp(1*gama0*L2) #constantes
	
	
	s11_colocar =float(dados[ler1_col])+1j*float(dados[ler2_col]) # real + j imag
	s21_colocar =float(dados[ler3_col])+1j*float(dados[ler4_col]) # real + j imag
	
	s12_colocar =float(dados[ler5_col])+1j*float(dados[ler6_col]) # real + j imag
	s22_colocar =float(dados[ler7_col])+1j*float(dados[ler8_col]) # real + j imag
	
	
	
	
	#EXPERIMENTAL S11 e S21
	s11.append(R1*R1*s11_colocar) #add vetor s11
	s21.append(R2*R1*s21_colocar) #add vetor s21
	
		#EXPERIMENTAL S22 e S12
	s22.append(R2*R2*s22_colocar) #add vetor s11
	s12.append(R2*R1*s12_colocar) #add vetor s21
	
	
	
	
	#**************************************************************************
	#PARAMETRO-S ANALITICO-   S11 e S21 ------------------------------------
	s11c_colocar = R1*R1*((Ca*(1-ta**2))/(1-(Ca**2)*(ta**2))) 
	s21c_colocar = R2*R1*((ta*(1-Ca**2))/(1-(Ca**2)*(ta**2)))
	#----------------------------------------------------------
	
	#PARAMETRO-S ANALITICO-   S22 e S12 ------------------------------------
	s22c_colocar = R2*R2*((Ca*(1-ta**2))/(1-(Ca**2)*(ta**2))) 
	s12c_colocar = R2*R1*((ta*(1-Ca**2))/(1-(Ca**2)*(ta**2)))
	#----------------------------------------------------------
	#**************************************************************************
	
	
	s11c.append(s11c_colocar) #add vetor s11
	s21c.append(s21c_colocar) #add vetor s21
	
	s22c.append(s22c_colocar) #add vetor s11
	s12c.append(s12c_colocar) #add vetor s21
	
	
	F_grafic.append(f_colocar/1e9)
#--------------------------------------------------------------	
	
	
#-------------- Modulo de S11 e S21 (Prova real) ---------------

S11_mod_c=[]
S21_mod_c=[]

S11_mod=[]
S21_mod=[]	

S22_mod_c=[]
S12_mod_c=[]

S22_mod=[]
S12_mod=[]	

for i in range(0,len(s11)):
	
	S11_mod_c.append(abs(s11c[i]))#Teorico com Ajuste
	S21_mod_c.append(abs(s21c[i]))#Teorico com Ajuste
	
	S11_mod.append(abs(s11[i]))#experimental com Ajuste
	S21_mod.append(abs(s21[i]))#experimental com Ajuste
	
	S22_mod_c.append(abs(s22c[i]))#Teorico com Ajuste
	S12_mod_c.append(abs(s12c[i]))#Teorico com Ajuste
	
	S22_mod.append(abs(s22[i])) #experimental com Ajuste
	S12_mod.append(abs(s12[i])) #experimental com Ajuste

	

plt.plot(F_grafic,S11_mod_c,label ="s11_teorico_ajustado")
plt.plot(F_grafic,S21_mod_c,label="s21_teorico_ajustado")
plt.plot(F_grafic,S11_mod,label ="s11_exp_ajustado")
plt.plot(F_grafic,S21_mod,label="s21_exp_ajustado")
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()

plt.plot(F_grafic,S22_mod_c,label ="s22_teorico_ajustado")
plt.plot(F_grafic,S12_mod_c,label="s12_teorico_ajustado")
plt.plot(F_grafic,S22_mod,label ="s22_exp_ajustado")
plt.plot(F_grafic,S12_mod,label="s12_exp_ajustado")
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()

plt.plot(F_grafic,S11_mod_c,label ="s11_teorico_ajustado")
plt.plot(F_grafic,S22_mod_c,label="s22_teorico_ajustado")
plt.plot(F_grafic,S21_mod_c,label ="s21_teorico_ajustado")
plt.plot(F_grafic,S12_mod_c,label="s12_teorico_ajustado")
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()

plt.plot(F_grafic,S11_mod,label ="s11_exp_ajustado")
plt.plot(F_grafic,S21_mod,label ="s21_exp_ajustado")
plt.plot(F_grafic,S22_mod,label="s22_exp_ajustado")
plt.plot(F_grafic,S12_mod,label="s12_exp_ajustado")
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()


'''
#-----------------------------VETORES-2---------------------
s11_ph =[] #S11 Fase
s21_ph =[] #S21 Fase


s11_db =[] #S11 em dB
s21_db =[] #S21 em dB


sum = [] # somatorio -> sum = |s11|**2 + |s21|**2
A =[] #absorbance
R = [] #reflectance
TRANS = [] #Transmtance


Z_a0 =[] #impedancia analitica vacuo
Z_ma = [] #impedancia analitica do material
Z_m = [] #impedancia calculada do material
Z_nrw =[] #impedancia NRW

T =[] #coeficiente de transmissao dos Par-S
T_a =[] #coef de Transmissao analitico

Cvetor =[] #coeficiente de reflexao dos Par-S
Cvetor_a = [] #coeficiente de reflexao analitico



er_r = [] #permissividade real
er_i = [] #'''''''''''''' imag
ur_r = [] #permeabilidade real
ur_i = [] #'''''''''''''' imag

er_abs=[] #permissividade modulo
ur_abs=[] #permeabilidade modulo

# ANALITICO------------------------
er_ra = [] #permissividade real
er_ia = [] #'''''''''''''' imag
ur_ra = [] #permeabilidade real
ur_ia = [] #'''''''''''''' imag

er_absa=[] #permissividade modulo
ur_absa=[] #permeabilidade modulo
#-----------------------------------


#-------- CURTO TEORICO-----------------------------
Zin_a =[] #Zin Teorico com CURTO

Cvetor_curto_a =[] #Coeficiente de Reflexao com CURTO TEORICO


#-------- CURTO EXPERIMENTAL S11 e S21-----------------------------
Zin =[] #Zin EXPERIMENTAL com CURTO

Cvetor_curto =[] #Coeficiente de Reflexao com CURTO EXPERIMENTAL


#-------- CURTO EXPERIMENTAL S11-----------------------------

Cvetor_c =[] #Coeficiente de Reflexao com CURTO EXPERIMENTAL


#------------------------------------------------------------



for n in range(0,len(F)):

	#----------------FASE-------------------------
	#Calcular fase em radianos (conta basica de vetor)
	s11_ph_calc = np.arctan(s11c[n].imag/s11c[n].real)
	s21_ph_calc = np.arctan(s21c[n].imag/s21c[n].real)
	
	#Converter rad para graus
	s11_ph_calc_grau = 360*s11_ph_calc/(2*np.pi)
	s21_ph_calc_grau = 360*s21_ph_calc/(2*np.pi)
	
	#add no vetor da phase
	s11_ph.append(s11_ph_calc_grau)
	s21_ph.append(s21_ph_calc_grau)
	#-----------------------------------------
	
	
	#------------------- dB------------------------
	#Transformar S11  S21 para dB
	s11_db_calc = 20*np.log10(abs(s11c[n]))
	s21_db_calc = 20*np.log10(abs(s21c[n]))
	
	#add no vetor DB
	s11_db.append(s11_db_calc)
	s21_db.append(s21_db_calc)
	#-------------------------------------------------
	
	#------------- ABSORBANCE =1 - TRANSMITANCE - REFLECTANCE---
	reflectance = abs(s11c[n])**2
	transmitance = abs(s21c[n])**2
	absorvance = 1 - reflectance - transmitance
	
	#add vetor A,TRANS and R
	A.append(absorvance)
	TRANS.append(transmitance)
	R.append(reflectance)
	#-----------------------------------------------------------
	
	
	#--------------SUM-----------------------------------------
	#Isso mostra as perdas
	soma = reflectance + transmitance
	
	#add vetor sum
	sum.append(soma)
	#----------------------------------------------------------

	
	
	#----------------------NRW PAR-S---------------------------------
	#OBS: SE EU USAR O s11c[n] e s21c[n] daqui pra baixo da problema!!!!
	
	
	#frequencia
	f = F[n]
	
	
	#lambda zero = comprimento de onda no vacuo
	onda = c/(f) # [m]
	
	
	#Constante de propagacao da onda no espaco livre
	gama0 = (2j*np.pi)*np.sqrt((1.0)/(onda**(2.0))-(1.0)/(onda_cut**(2.0)))
	
	
	#Constante de propagacao da onda no material(analitico) 
	gamaX = (2j*np.pi/onda)*np.sqrt(e_a*u_a-(onda**2.0)/(onda_cut**2.0))
	
	
	#impedancia Analitica do Vacuo(za0)
	z_a0= (1j*u0*2*np.pi*f)/(gama0)
	
	Z_a0.append(z_a0)
	
	
	#impedancia analitica do material (zma)
	z_ma = ((1j*2*np.pi*f*u_a*u0)/(gamaX))/(z_a0) #z_a0 normliza
	
	Z_ma.append(z_ma.real)
	
	
	#impedancia do material calculada  com par-S (zm)  #IGUAL DO NRW
	z_m = np.sqrt(((1+s11c[n])**(2)-s21c[n]**2)/((1-s11c[n])**(2)-s21c[n]**(2)))
	
	Z_m.append(z_m.real)
	
	
	#coeficiente de transmissao Calculado 
	t = s21c[n]/(1-s11c[n]*((z_m-1)/(z_m+1)))
	
	T.append(abs(t))
	
	
	#Coeficiente de transmissao Analitico
	ta = np.exp(-gamaX*d)
	
	T_a.append(abs(ta))
	
	
	#Valor K
	K = ((s11c[n])**(2.0)-(s21c[n])**(2.0)+1)/(2*s11c[n]) 
	
	
	#Coeficiente de reflexao Par-S
	#positivo
	C_p = K + np.sqrt(K**2-1)
	#negativo
	C_n = K - np.sqrt(K**2-1)
	#condicao para valor do sinal do coeficiente de reflexao
	if C_p < 1:
		sinal = 1
	elif C_n <= 1:
		sinal =-1
	#coeficiente de reflexao com sinal ok
	C = K+sinal*(np.sqrt(K**2-1))
	
	Cvetor.append(abs(C))
	
	#velocidade da luz no guia
	c_lab = f/onda_cut
	
	#Coeficiente de refelxao Analitico 
	#C_analitico = ((gama0)/(u0)-(gamaX)/(u_a))/((gama0)/(u0)+(gamaX)/(u_a))
	#C_analitico = (((c)/(c_lab))*np.sqrt((u_a)/(e_a))-1)/(((c)/(c_lab))*np.sqrt((u_a)/(e_a))+1)
	C_analitico = (z_ma-1)/(z_ma+1)
	
	
	Cvetor_a.append(abs(C_analitico))
	
	
	#constante P
	P2=-((1.0)/(2*np.pi*d)*np.log(1.0/t))**2
	P=1.0/np.sqrt(P2)
	
	
	#constante Lamb
	lamb = np.sqrt((1.0)/(onda)**(2)-(1.0)/(onda_cut)**(2))
	
	
	#impedancia NRW (z_nrw) #IGUAL AO Z CALCULADO COM PAR-S (z_m)
	z_nrw = (1+C)/(1-C)
	Z_nrw.append(z_nrw.real) #somente real
	
	
	#Permeabilidade NRW
	#ux = ux = z_nrw/(P*lamb)
	ux = ux = z_m/(P*lamb) #poco melhor com z_m
	
	ur_r.append(ux.real)
	ur_i.append(ux.imag)
	ur_abs.append(abs(ux))
	
	
	#Permissividade NRW
	ex = ((onda)**(2)/ux)*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/t))**2)
	#ex = ((onda)**(2)/abs(ux))*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/t))**2) #abs(ux)
	
	er_r.append(ex.real)
	er_i.append(ex.imag)
	er_abs.append(abs(ex))
	#------------------------------------------------------
	
	#------------------NRW - Analitico----------------------
	
	#constante P (ANALITICO
	P2_a=-((1.0)/(2*np.pi*d)*np.log(1.0/ta))**2
	P_a=1.0/np.sqrt(P2_a)
	
	#Permeabilidade NRW sem par-S
	ux_a = z_ma/(P_a*lamb)
	
	ur_ra.append(ux_a.real)
	ur_ia.append(ux_a.imag)
	ur_absa.append(abs(ux_a))
	
	#Permissividade NRW sem par-S
	ex_a = ((onda)**(2)/ux_a)*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/ta))**2)
	er_ra.append(ex_a.real)
	er_ia.append(ex_a.imag)
	er_absa.append(abs(ex_a))
	
	
	
	#----------Calculo do Coeficiente de Reflexao com Curto - TEORICO---------------------
	
	np.seterr(divide='ignore', invalid='ignore')
	# Zin teorico com curto
	#zin_a = (1j*(u_a/e_a)**(1.0/2.0))*np.tan((2*np.pi*f*d)*((u_a*e_a)**(1.0/2.0))) #CERTO,mas buga a escala
	zin_a = (1j*(u_a/e_a)**(1.0/2.0))*np.tan((2*np.pi*d/onda)*((u_a*e_a)**(1.0/2.0)))
	
	Zin_a.append(abs(zin_a))
	
	#Coeficiente de Reflexao com curto
	C_curto_a = (zin_a-1)/(zin_a+1)
	
		
	Cvetor_curto_a.append(abs(C_curto_a))
	
	
	#----------Calculo do Coeficiente de Reflexao com Curto - EXPERIMENTAL (S11 e S21)---------------------
	#Precisa calcular o NRW e obter o e and mu experimental
	# Zin teorico com curto
	#zin = (1j*(ux/ex)**(1.0/2.0))*np.tan((2*np.pi*f*d)*((ux*ex)**(1.0/2.0))) #Certo, mas buga escala
	zin = (1j*(ux/ex)**(1.0/2.0))*np.tan((2*np.pi*d/onda)*((ux*ex)**(1.0/2.0)))
	
	Zin.append(abs(zin))
	
	#Coeficiente de Reflexao com curto
	C_curto = (zin-1)/(zin+1)
		
	Cvetor_curto.append(abs(C_curto))
	
	
	#--------Calculo do Coeficiente de REFLEXAO COM MEDICAO DO PAR-S NO CURTO - EXPERIMENTAL(S11 apenas)
	#NESTE TEORICO N VOU USAR OS e and mu, apenas o S11 da medida com CURTO (refletividade)
	#Coeficiente de reflexao Par-S11
	#K_c = ((s11[n])**(2.0)-(0)**(2.0)+1)/(2*s11[n]) 
	K_c = ((1)**(2.0)-(0)**(2.0)+1)/(2*1) 
	#positivo
	C_p_c = K_c + np.sqrt(K_c**2-1)
	#negativo
	C_n_c = K_c - np.sqrt(K_c**2-1)
	#condicao para valor do sinal do coeficiente de reflexao
	if C_p_c < 1:
		sinal = 1
	elif C_n_c <= 1:
		sinal =-1
	#coeficiente de reflexao com sinal ok
	C_c = K+sinal*(np.sqrt(K_c**2-1))
	
	Cvetor_c.append(abs(C_c))
	
	
#----------------------PLOTES----------------------------	



#Plot Modulo em DB
plt.plot(F_grafic,s11_db,'.b',label ='s11_db')
plt.plot(F_grafic,s21_db,"or",label = 's21_db')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()
	


#Plot Phase em Grau
plt.plot(F_grafic,s11_ph,'.b',label ='s11_fase')
plt.plot(F_grafic,s21_ph,"or",label = 's21_fase')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()



#Plot aborbance, refletance and transmitance
plt.plot(F_grafic,A,'-b',label ='absorbance')
plt.plot(F_grafic,TRANS,'-r',label ='transmitance')
plt.plot(F_grafic,R,'-g',label ='reflectance')
plt.ylim(0,1)
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()		


#Plot Sum
plt.plot(F_grafic,sum,'-b',label ='SOMA DE S11 e S21')
plt.ylim(0,1.02)
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()


#Plot Impedancia
#plt.plot(F_grafic,Z_a0,'-b',label ='z_vacuo')
plt.plot(F_grafic,Z_ma,'-g',label ='z_material_Teorico')
plt.plot(F_grafic,Z_m,'-r',label ='z_material_Par-S') #Igual (MAS E MELHOR)
#plt.plot(F_grafic,Z_nrw,'-y',label ='z_nrw') #igual
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()


#Plot Coeficiente de Transmissao
plt.plot(F_grafic,T,'-g',label ='T_calc')
plt.plot(F_grafic,T_a,'-r',label ='T_analitico')
plt.xlim(8.2,12.4)
plt.ylim(0,1.2)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()


#Plot Coeficiente de Reflexao
plt.plot(F_grafic,Cvetor,'-g',label ='Coef_Reflex_calc')
plt.plot(F_grafic,Cvetor_a,'-r',label ='Coef_Reflex_analitico')
plt.xlim(8.2,12.4)
plt.ylim(0,1.2)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()


#plot e
plt.plot(F_grafic,er_r,'-',label="er'")
plt.plot(F_grafic,er_i,'-',label='er"')
plt.plot(F_grafic,er_ra,'-',label="er'_TEORICO")
plt.plot(F_grafic,er_ia,'-',label='er"_TEORICO')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()

#plot u
plt.plot(F_grafic,ur_r,'-',label = "ur'")
plt.plot(F_grafic,ur_i,'-',label ='ur"')
plt.plot(F_grafic,ur_ra,'-',label = "ur'_TEORICO")
plt.plot(F_grafic,ur_ia,'-',label ='ur"_TEORICO')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()

#plot e and u modulo
plt.plot(F_grafic,ur_abs,'-',label="ur_abs")
plt.plot(F_grafic,er_abs,'-',label='er_abs')
plt.plot(F_grafic,ur_absa,'-',label="ur_abs_TEORICO")
plt.plot(F_grafic,er_absa,'-',label='er_abs_TEORICO')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()

#plot Zin Teorico Curto
plt.plot(F_grafic,Zin_a,'-',label="Zin_curto_TEORICO")
plt.plot(F_grafic,Zin,'-',label="Zin_curto_EXPERIMENTAL")
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()


#plot Coeficiente de Reflexao Teorico Curto
plt.plot(F_grafic,Cvetor_curto_a,'-',label="Reflexao_curto_TEORICO")
plt.plot(F_grafic,Cvetor_curto,'-',label="Reflexao_curto_EXPERIMENTAL S11S21")
plt.plot(F_grafic,Cvetor_c,'-',label="Reflexao_curto_EXPERIMENTAL S11")
plt.xlim(8.2,12.4)
plt.ylim(0,1.2)
plt.xlabel("Freq(GHz)")
plt.legend()
plt.show()

'''


#--------------------------------------------------------

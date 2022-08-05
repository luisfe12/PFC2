import pynput.keyboard



def presiona(key):
    # key1 = convertir(key)
   pass


def libera(key):
    pass
    
def convertir( key):
    pass

    
with pynput.keyboard.Listener(on_press=presiona, on_release=libera) as listen:
    listen.join()

    csdcsdcsdcdscsdcds
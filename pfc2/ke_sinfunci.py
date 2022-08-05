from pynput import keyboard


def presiona(key):
    # key1 = convertir(key)
    print("tecla presionada: {}".format(key))


def libera(key):
    print("Tecla liberada: {}".format(key))
    if key == keyboard.Key.esc: #usarlo asi para pyrhon 9
        print("saleiendo del programa ...")
        return False
    
def convertir( key):
    pass

    
with keyboard.Listener(on_press=presiona, on_release=libera) as listen:
    listen.join()




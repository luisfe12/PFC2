import psutil
import time

while True:
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = proc.pid
            print(processName , ' ::: ', processID)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    time.sleep(20)
    print("NUEVO FOR DE PROCESOS------------------------- \n \n")
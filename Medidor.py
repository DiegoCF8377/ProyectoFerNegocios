import pyautogui as pyui
import time
import os
from git import Repo

#Datos de donde tomar la imagen
x1=319
y1=451
x2=579
y2=793




PATH_OF_GIT_REPO = r'C:\Users\diego\Documents\Python\ProyectoFerNegocios'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'XDesdePython'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    




while True:
    # Obtiene la posición actual del mouse
    time.sleep(1)
    x, y = pyui.position()
    
    # Muestra la posición del mouse
    
    
    print(f"Posición del mouse: X={x}, Y={y}")

    # Espera un segundo antes de mostrar la próxima posición

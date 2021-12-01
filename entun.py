import time
import os
from platform import system
import subprocess

color="\033[32m"

def localhost():
  print('''\n
██       ██████   ██████  █████  ██      ██   ██  ██████  ███████ ████████    ██████  ██    ██ ███    ██ 
██      ██    ██ ██      ██   ██ ██      ██   ██ ██    ██ ██         ██       ██   ██ ██    ██ ████   ██ 
██      ██    ██ ██      ███████ ██      ███████ ██    ██ ███████    ██       ██████  ██    ██ ██ ██  ██ 
██      ██    ██ ██      ██   ██ ██      ██   ██ ██    ██      ██    ██       ██   ██ ██    ██ ██  ██ ██ 
███████  ██████   ██████ ██   ██ ███████ ██   ██  ██████  ███████    ██    ██ ██   ██  ██████  ██   ████''')
  print('\nElije el puerto a entunelar')
  puerto = int(input('[~] Puerto >> '))
  if type(puerto) == int:
    subprocess.run(
      ["ssh", "-R", f"80:localhost:{puerto}", "nokey@localhost.run"])
  else:
    print('[~] El puerto no es un numero entero.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    localhost()

os.system("clear")
logo = color + '''
███████ ███    ██ ████████ ██    ██ ███    ██ ███████ ██       █████  ██████   ██████  ██████  
██      ████   ██    ██    ██    ██ ████   ██ ██      ██      ██   ██ ██   ██ ██    ██ ██   ██ 
█████   ██ ██  ██    ██    ██    ██ ██ ██  ██ █████   ██      ███████ ██   ██ ██    ██ ██████  
██      ██  ██ ██    ██    ██    ██ ██  ██ ██ ██      ██      ██   ██ ██   ██ ██    ██ ██   ██ 
███████ ██   ████    ██     ██████  ██   ████ ███████ ███████ ██   ██ ██████   ██████  ██   ██ '''

def menu():
  print(logo)
  print('\n[~] Elije una opcion')
  print('[1] Entunelar con localhost.run')
  print('[99] Salir')
  elegir = int(input('[~] Elije una opcion: '))
  if elegir == 1:
    localhost()
  elif elegir == 99:
    exit()
  else:
    print('Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    menu()
    
menu()

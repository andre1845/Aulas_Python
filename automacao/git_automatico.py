# importa bibliotecas
import pyautogui as auto
import time

# tempo que cada comando demora para executar
auto.PAUSE = 1

#pede o link do deiretório
link_diretorio = input('Link do diretório: ')

# instruções
auto.press('win')
auto.write('vscode')
auto.press('enter')

# espera 10 segundos para abrir o vscode e continuar com os comandos
time.sleep(10)

# continua as instruções=
auto.hotkey('ctrl', 'shift', "'")
time.sleep(10)
auto.write('git init')
auto.press('enter')
auto.write('git add .')
auto.press('enter')
auto.write('git commit -m "GIT automatico."')
auto.press('enter')

# espera 5 segundos para dar tempo de fazer o commit
time.sleep(5)

auto.write('git branch -M main')
auto.press('enter')

auto.write(f'git remote add origin {link_diretorio}')
auto.press('enter')

auto.write('git push -u origin main')
auto.press('enter')
#Teste de Automação para enviar msg pelo aplicativo do WhatsApp

import pyautogui
import time

pyautogui.pause = 1 #depois de cada comando esperar 1 segundo, para impedir encavalamento de comandos

pyautogui.hotkey('win')
pyautogui.write('WhatsApp')
pyautogui.press('enter')
time.sleep(2)

print(pyautogui.position()) #Pegar a posição do mouse
pyautogui.click(x=219, y=234)

time.sleep(5)
print(pyautogui.position()) #Pegar a posição do mouse
pyautogui.click(x=695, y=1005)

pyautogui.write('Bom dia "AUTOMATIZADO" para a minha poposa')
pyautogui.press('enter')
# Testando automações com o PYautogui
#pyautogui.press() -> aperta 1 tecla
#pyautogui.click() -> clica com o mouse
#pyautogui.write() -> escreve um texto
#pyautogui.hotkey() -> usa um atalho do computador ('ctrl' , 'c')

#Preencher formulário em um site
import pyautogui
import time

pyautogui.pause = 1 #depois de cada comando esperar 1 segundo, para impedir encavalamento de comandos
#Passo a passo do que eu quero automatizar

#Abrir o navegador (chrome)
pyautogui.hotkey('win') #aperta a tecla de atalho do windows
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)

#Entrar no site (específico)
pyautogui.write('https://br.investing.com/economic-calendar')
pyautogui.press('enter')
time.sleep(5)

print(pyautogui.position()) #Pegar a posição do mouse

#Preencher o formulário
pyautogui.click(x=1048, y=141)
pyautogui.write('USD/MXN')
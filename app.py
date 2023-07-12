# Passos para criar um código python  que verifica se há um botão com a cor correspondente dentro do círculo daquela cor
# O jogo que foi utilizado como referência para o teste foi: https://guitarflash.com/?lg=pt
# Para obter as coordenadas e a cor, acabei por utilizar o mouseinfo(mouseInfo).
import pyautogui
import keyboard
from time import sleep

# O código vai funcionar até que se aperte '1'
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(x, y, (0, 0, 0)): # Informar localização e a cor correspondente
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(x, y, (0, 0, 0)): # Informar localização e a cor correspondente
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(x, y, (0, 0, 0)): # Informar localização e a cor correspondente
        pyautogui.press('a')
        sleep(0.05)
    
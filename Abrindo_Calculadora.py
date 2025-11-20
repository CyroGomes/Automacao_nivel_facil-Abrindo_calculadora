import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(x=471, y=1046) 

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(x=471, y=1046)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Movendo o mouse até barra de pesquisa
posicaoMouse.moveTo(x=811, y=152)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(x=811, y=152)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(4)

#Escrevenda a palavra calc / calculadora
posicaoMouse.typewrite('calc')

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(x=674, y=337)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#print(posicaoMouse.position())
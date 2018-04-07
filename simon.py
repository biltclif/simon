from gpiozero import LED, Button
from signal import pause
from random import randint
from time import sleep



green = LED(20)
red = LED(17)
yellow = LED(26)

##greenButton = Button(3)
##redButton = Button(23)
##yellowButton = Button(16)

lights = []

def nextLight():
    lights.append(randint(1, 3))
    return lights[-1]

def showLights():
    for light in lights:
        if light == 1:
            green.on()
        
        if light == 2:
            red.on()
            
        if light == 3:
            yellow.on()
            
        sleep(1)
        turnLightsOff()
        sleep(.5)
            
def turnLightsOff():
    green.off()
    red.off()
    yellow.off()
    
turnLightsOff()

try:
    while True:
        #print(lights)
        
        nextLight()
        showLights()
        sleep(2)
        turnLightsOff()
        
        
##        greenButton.when_pressed = green.on
##        greenButton.when_released = green.off
##
##        redButton.when_pressed = red.on
##        redButton.when_released = red.off
##
##        yellowButton.when_pressed = yellow.on
##        yellowButton.when_released = yellow.off

except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    exit()

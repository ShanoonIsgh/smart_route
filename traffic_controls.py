from gpiozero import LED
from time import sleep


Red = LED(17)
Yellow = LED(27)
Green = LED(22)

def red():
    Red.on()
    sleep(3)
    Red.off()
    sleep(1)
    return("Red On ")
def amber():
    Yellow.on()
    sleep(3)
    Yellow.off()
    sleep(1)
    return(" Yellow on")
def green():
    Green.on()
    sleep(3)
    Green.off()
    sleep(1)
    return(" Green on")



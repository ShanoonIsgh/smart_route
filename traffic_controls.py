from gpiozero import LED, Button
from time import sleep


Red = LED(17)
Yellow = LED(27)
Green = LED(22)

while True:
	Red.on()
	sleep(3)
	print("At a halt")
	Red.off()
	sleep(1)

	Yellow.on()
	sleep(3)
	print("In transit")
	Yellow.off()
	sleep(1)

	Green.on()
	sleep(3)
	print("On the go")
	Green.off()
	sleep(1)


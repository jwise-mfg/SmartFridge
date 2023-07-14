from gpiozero import LED
led1 = LED(26)
led1.on()
print ("LED at 26 should be on. Press enter to exit")
input()
led1.off()


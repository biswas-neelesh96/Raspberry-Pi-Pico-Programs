#Glowing both Internal & External LED at the same time

import machine
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_external = machine.Pin(15, machine.Pin.OUT)
while True:
    led_external.value(1)
    led_onboard.value(1)
    

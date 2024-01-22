import pyfirmata
import time

comport = 'COM3'

board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')

servo_pin = 3
servo = board.get_pin('d:{}:s'.format(servo_pin))

beep_pin = 10  # Pin connected to the buzzer or piezo speaker
beep = board.get_pin('d:{}:o'.format(beep_pin))

def led(fingerUp):
    if fingerUp == [0, 1, 0, 0, 1]:
        led_1.write(1)
        led_2.write(0)
        servo.write(90)  # Rotate the servo motor to 180 degrees
        time.sleep(10)
        servo.write(0) 
    elif fingerUp == [0, 1, 0, 0, 0]:
        led_1.write(0)
        led_2.write(0)
        servo.write(0)
    else:
        beep.write(1)  # Turn on the beep sound
        time.sleep(0.5)  # Beep duration
        beep.write(0)  # Turn off the beep sound
import randomAdd commentMore actions
import time
import board
import digitalio

led1 = digitalio.DigitalInOut(board.GP15)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP14)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.GP13)
led3.direction = digitalio.Direction.OUTPUT

led4 = digitalio.DigitalInOut(board.GP12)
led4.direction = digitalio.Direction.OUTPUT

led5 = digitalio.DigitalInOut(board.GP11)
led5.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP0)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

powersystem_check = 1
loop = 0

import pwmio
import analogio
import time
knob = analogio.AnalogIn(board.A0)
led = pwmio.PWMOut(board.GP16, frequency=1000)
led2 = pwmio.PWMOut(board.GP17, frequency=1000)
led3 = pwmio.PWMOut(board.GP15, frequency=1000)
while True:
    if button1.value is True:

        if button2.value is False:
            if powersystem_check == 1:
                powersystem_check = powersystem_check - 1

            elif powersystem_check == 0:
                powersystem_check = powersystem_check + 1

        elif powersystem_check == 0:

            led1.value = True
            led2.value = True
            led3.value = True
            led4.value = True
            led5.value = True
            time.sleep(0.05)
            led1.value = False
            led2.value = False
            led3.value = False
            led4.value = False
            led5.value = False
            time.sleep(0.05)

        else:
            time_diffaculty = 0.1
            points = 0
            lap = 1
            led5.value = True
            time.sleep(.1)
            led2.value = False
            time.sleep(.1)

            led4.value = True
            time.sleep(.1)
            led1.value = False
            time.sleep(.1)

            led3.value = True
            time.sleep(.1)
            led5.value = False
            time.sleep(.1)

            led2.value = True
            time.sleep(.1)
            led4.value = False
            time.sleep(.1)

            led1.value = True
            time.sleep(.1)
            led3.value = False
            time.sleep(.1)

    knob_value = knob.value
    # detects if knob is past the middle cycle
    if knob_value < 65535 / 3:
        led.duty_cycle = knob_value * 2
        led2.duty_cycle = 0
    elif knob_value < 45000:
        led.duty_cycle = 65535
        led2.duty_cycle = (knob_value - 20000) * 2
    else:
        if points == 10 * lap:
            loop = lap
            while loop == 0:
                lap = lap + 1
                led5.value = True
                time.sleep(.1)
                led2.value = False
                time.sleep(.1)

                led4.value = True
                time.sleep(.1)
                led1.value = False
                time.sleep(.1)

                led3.value = True
                time.sleep(.1)
                led5.value = False
                time.sleep(.1)

                led2.value = True
                time.sleep(.1)
                led4.value = False
                time.sleep(.1)

                led1.value = True
                time.sleep(.1)
                led3.value = False
                time.sleep(.1)
                loop -= 1

        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        points = points + 1
        time_diffaculty -= 0.001
        time.sleep(random.randint(1, 10))

        led1.value = True
        time.sleep(time_diffaculty)
        if button1.value is False:
            led1.value = False
            led2.value = False
            led3.value = False
            led4.value = False
            led5.value = False
        else:
            led2.value = True
            time.sleep(time_diffaculty)
            if button1.value is False:
                led1.value = False
                led2.value = False
                led3.value = False
                led4.value = False
                led5.value = False
            else:
                led3.value = True
                time.sleep(time_diffaculty)
                if button1.value is False:
                    led1.value = False
                    led2.value = False
                    led3.value = False
                    led4.value = False
                    led5.value = False
                else:
                    led4.value = True
                    time.sleep(time_diffaculty)
                    if button1.value is False:
                        led1.value = False
                        led2.value = False
                        led3.value = False
                        led4.value = False
                        led5.value = False
                    else:
                        led5.value = True
                        time.sleep(time_diffaculty)
                        if button1.value is False:
                            led1.value = False
                            led2.value = False
                            led3.value = False
                            led4.value = False
                            led5.value = False
                        else:
                            loop = loop = 0
                            while loop != 60:
                                led1.value = True
                                time.sleep(0.01)
                                led1.value = False
                                time.sleep(0.01)
                                led2.value = True
                                time.sleep(0.01)
                                led2.value = False
                                time.sleep(0.01)
                                led3.value = True
                                time.sleep(0.01)
                                led3.value = False
                                time.sleep(0.01)
                                led4.value = True
                                time.sleep(0.01)
                                led4.value = False
                                time.sleep(0.01)
                                led5.value = True
                                time.sleep(0.01)
                                led5.value = False
                                time.sleep(0.01)
                                loop += 1

                            loop = points - 4
                            while loop == 0:
                                led1.value = False
                                led2.value = False
                                led3.value = False
                                led4.value = False
                                led5.value = False
                                time.sleep(1)
                                if points == points + 1:
                                    led1.value = True
                                    time.sleep(0.01)
                                    led1.value = False
                                    time.sleep(0.01)
                                elif points == points + 2:
                                    led1.value = True
                                if points == points + 3:
                                    led2.value = True
                                    time.sleep(0.01)
                                    led2.value = False
                                    time.sleep(0.01)
                                elif points == points + 4:
                                    led2.value = True
                                if points == points + 5:
                                    led3.value = True
                                    time.sleep(0.01)
                                    led3.value = False
                                    time.sleep(0.01)
                                elif points == points + 6:
                                    led3.value = True
                                if points == points + 7:
                                    led4.value = True
                                    time.sleep(0.01)
                                    led4.value = False
                                    time.sleep(0.01)
                                elif points == points + 8:
                                    led4.value = True
                                if points == points + 9:
                                    led5.value = True
                                    time.sleep(0.01)
                                    led5.value = False
                                    time.sleep(0.01)
                                elif points == points + 10:
                                    led5.value = True
                                time.sleep(3)
                                loop -= 1
        led.duty_cycle = 65535
        led2.duty_cycle = 65535
        led3.duty_cycle = 65535
        time.sleep(0.1)
        led3.duty_cycle = 0
        time.sleep(0.1)
    print(knob_value)

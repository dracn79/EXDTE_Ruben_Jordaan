import board
import pwmio
import analogio
import time
knob = analogio.AnalogIn(board.A0)
led = pwmio.PWMOut(board.GP16, frequency=1000)
led2 = pwmio.PWMOut(board.GP17, frequency=1000)
led3 = pwmio.PWMOut(board.GP15, frequency=1000)
while True:
    knob_value = knob.value
    # detects if knob is past the middle cycle
    if knob_value < 65535 / 3:
        led.duty_cycle = knob_value * 2
        led2.duty_cycle = 0
    elif knob_value < 45000:
        led.duty_cycle = 65535
        led2.duty_cycle = (knob_value - 20000) * 2
    else:
        led.duty_cycle = 65535
        led2.duty_cycle = 65535
        led3.duty_cycle = 65535
        time.sleep(0.1)
        led3.duty_cycle = 0
        time.sleep(0.1)
    print(knob_value)

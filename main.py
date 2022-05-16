temperature = 0

def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global temperature
    temperature = Math.idiv(pins.analog_read_pin(AnalogPin.P0) - 230, 12)
    basic.show_string("" + str((temperature)))
    if temperature <= 20 or temperature >= 15:
        pins.servo_write_pin(AnalogPin.P1, Math.map(temperature, 15, 20, 0, 60))
    elif temperature <= 25 or temperature >= 20:
        pins.servo_write_pin(AnalogPin.P1, Math.map(temperature, 20, 25, 60, 120))
    else:
        if temperature <= 30 or temperature >= 25:
            pins.servo_write_pin(AnalogPin.P1, Math.map(temperature, 25, 30, 120, 180))
    basic.pause(100)
basic.forever(on_forever)

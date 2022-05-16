let temperature = 0
input.onButtonPressed(Button.A, function () {
    pins.servoWritePin(AnalogPin.P1, 0)
})
basic.forever(function () {
    temperature = Math.idiv(pins.analogReadPin(AnalogPin.P0) - 230, 12)
    basic.showString("" + (temperature))
    if (temperature <= 20 || temperature >= 15) {
        pins.servoWritePin(AnalogPin.P1, Math.map(temperature, 15, 20, 0, 60))
    } else if (temperature <= 25 || temperature >= 20) {
        pins.servoWritePin(AnalogPin.P1, Math.map(temperature, 20, 25, 60, 120))
    } else {
        if (temperature <= 30 || temperature >= 25) {
            pins.servoWritePin(AnalogPin.P1, Math.map(temperature, 25, 30, 120, 180))
        }
    }
    basic.pause(100)
})

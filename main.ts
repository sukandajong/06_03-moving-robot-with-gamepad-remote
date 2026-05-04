radio.onReceivedString(function (receivedString) {
    if (receivedString == "C") {
        basic.showIcon(IconNames.Heart)
    } else if (receivedString == "W") {
        basic.showIcon(IconNames.No)
    } else if (receivedString == "F") {
        basic.showArrow(ArrowNames.North)
        iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Forward, 50)
        iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Forward, 50)
    } else if (receivedString == "B") {
        basic.showArrow(ArrowNames.South)
        iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Backward, 50)
        iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Backward, 50)
    } else if (receivedString == "R") {
        basic.showArrow(ArrowNames.East)
        iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Forward, 50)
        iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Backward, 50)
    } else if (receivedString == "L") {
        basic.showArrow(ArrowNames.West)
        iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Backward, 50)
        iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Forward, 50)
    } else if (receivedString == "S") {
        basic.showIcon(IconNames.SmallSquare)
        iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Backward, 0)
        iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Forward, 0)
    }
})
let joy_y = 0
let joy_x = 0
let is_active = false
// จัดการปัญหาเสียง (สำคัญสำหรับ Gamepad)
pins.digitalWritePin(DigitalPin.P0, 1)
// ยืนยันให้หุ่นยนต์หยุดนิ่งก่อนเริ่ม
iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Backward, 0)
iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Forward, 0)
// ตั้งค่าการสื่อสารและปุ่มกด
radio.setGroup(1)
pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
pins.setPull(DigitalPin.P16, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P13) == 0) {
        is_active = true
        basic.showIcon(IconNames.Heart)
        radio.sendString("C")
    } else if (pins.digitalReadPin(DigitalPin.P16) == 0) {
        basic.showIcon(IconNames.No)
        radio.sendString("W")
    }
    if (is_active) {
        joy_x = pins.analogReadPin(AnalogReadWritePin.P2)
        joy_y = pins.analogReadPin(AnalogReadWritePin.P1)
        if (joy_y < 400) {
            radio.sendString("F")
            basic.showArrow(ArrowNames.North)
        } else if (joy_y > 600) {
            radio.sendString("B")
            basic.showArrow(ArrowNames.South)
        } else if (joy_x < 400) {
            radio.sendString("R")
            basic.showArrow(ArrowNames.East)
        } else if (joy_x > 600) {
            radio.sendString("L")
            basic.showArrow(ArrowNames.West)
        } else {
            radio.sendString("S")
            basic.showIcon(IconNames.SmallSquare)
        }
    }
})

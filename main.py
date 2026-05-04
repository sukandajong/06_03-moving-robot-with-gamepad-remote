def on_received_string(receivedString):
    if receivedString == "C":
        basic.show_icon(IconNames.HEART)
    elif receivedString == "W":
        basic.show_icon(IconNames.NO)
    elif receivedString == "F":
        basic.show_arrow(ArrowNames.NORTH)
        iBIT.set_motor(ibitMotorCH.M1, ibitMotor.FORWARD, 50)
        iBIT.set_motor(ibitMotorCH.M2, ibitMotor.FORWARD, 50)
    elif receivedString == "B":
        basic.show_arrow(ArrowNames.SOUTH)
        iBIT.set_motor(ibitMotorCH.M1, ibitMotor.BACKWARD, 50)
        iBIT.set_motor(ibitMotorCH.M2, ibitMotor.BACKWARD, 50)
    elif receivedString == "R":
        basic.show_arrow(ArrowNames.EAST)
        iBIT.set_motor(ibitMotorCH.M1, ibitMotor.FORWARD, 50)
        iBIT.set_motor(ibitMotorCH.M2, ibitMotor.BACKWARD, 50)
    elif receivedString == "L":
        basic.show_arrow(ArrowNames.WEST)
        iBIT.set_motor(ibitMotorCH.M1, ibitMotor.BACKWARD, 50)
        iBIT.set_motor(ibitMotorCH.M2, ibitMotor.FORWARD, 50)
    elif receivedString == "S":
        basic.show_icon(IconNames.SMALL_SQUARE)
        iBIT.set_motor(ibitMotorCH.M1, ibitMotor.BACKWARD, 0)
        iBIT.set_motor(ibitMotorCH.M2, ibitMotor.FORWARD, 0)
radio.on_received_string(on_received_string)

joy_y = 0
joy_x = 0
is_active = False
# จัดการปัญหาเสียง (สำคัญสำหรับ Gamepad)
pins.digital_write_pin(DigitalPin.P0, 1)
# ยืนยันให้หุ่นยนต์หยุดนิ่งก่อนเริ่ม
iBIT.set_motor(ibitMotorCH.M1, ibitMotor.BACKWARD, 0)
iBIT.set_motor(ibitMotorCH.M2, ibitMotor.FORWARD, 0)
# ตั้งค่าการสื่อสารและปุ่มกด
radio.set_group(1)
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_UP)

def on_forever():
    global is_active, joy_x, joy_y
    if pins.digital_read_pin(DigitalPin.P13) == 0:
        is_active = True
        basic.show_icon(IconNames.HEART)
        radio.send_string("C")
    elif pins.digital_read_pin(DigitalPin.P16) == 0:
        basic.show_icon(IconNames.NO)
        radio.send_string("W")
    if is_active:
        joy_x = pins.analog_read_pin(AnalogReadWritePin.P2)
        joy_y = pins.analog_read_pin(AnalogReadWritePin.P1)
        if joy_y < 400:
            radio.send_string("F")
            basic.show_arrow(ArrowNames.NORTH)
        elif joy_y > 600:
            radio.send_string("B")
            basic.show_arrow(ArrowNames.SOUTH)
        elif joy_x < 400:
            radio.send_string("R")
            basic.show_arrow(ArrowNames.EAST)
        elif joy_x > 600:
            radio.send_string("L")
            basic.show_arrow(ArrowNames.WEST)
        else:
            radio.send_string("S")
            basic.show_icon(IconNames.SMALL_SQUARE)
basic.forever(on_forever)

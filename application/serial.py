import serial

import click
from flask import current_app, g


def init_app(app):
    app.teardown_appcontext(close_serial)


def get_serial():
    if 'serial' not in g:
        g.serial = serial.Serial(
        port = current_app.config["SERIAL_PORT"],
        baudrate = 9600,
        bytesize = serial.EIGHTBITS,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        timeout = 1
    )

    return g.serial


def send_command(cmd):
    ser = get_serial()
    ser.write(cmd)
    ser.flush()

    retval = ""
    while True:
        line = ser.readline()
        if line == b'': break
        retval = retval + line.decode("utf-8")

    return { "response": retval }


def sysinfo():
    ser = get_serial()
    ser.write(b'>>SYSInfo\r\n')
    ser.flush()

    n = 0
    sysinfo = dict()

    while True:
        line = ser.readline()
        if line == b'': break

        if n == 0: sysinfo["model"] = line.decode("utf-8")[2:].strip()
        elif n == 1: sysinfo["sw_version"] = line.decode("utf-8")[2:].strip()
        elif n == 3: sysinfo["source"] = line.decode("utf-8")[2:].strip()
        elif n == 5: sysinfo["audio"] = line.decode("utf-8")[2:].strip()
        elif n == 6: sysinfo["edid"] = line.decode("utf-8")[2:].strip()

        elif line == b'<<AUTO Switch\r\n':
            sysinfo["auto"] = True
            sysinfo["manual"] = False

        elif line == b'<<MANUAL Switch\r\n':
            sysinfo["auto"] = False
            sysinfo["manual"] = True

        elif line.startswith(b'<<HDCP'): sysinfo["hdcp"] = line.decode("utf-8").rsplit()[-1] 
        elif line.startswith(b'<<HDMI1'): sysinfo["hdmi1"] = line.decode("utf-8").rsplit()[-1] 
        elif line.startswith(b'<<HDMI2'): sysinfo["hdmi2"] = line.decode("utf-8").rsplit()[-1] 
        elif line.startswith(b'<<HDMI3'): sysinfo["hdmi3"] = line.decode("utf-8").rsplit()[-1] 
        elif line.startswith(b'<<HDMI4'): sysinfo["hdmi4"] = line.decode("utf-8").rsplit()[-1] 

        n = n + 1

    return sysinfo


def close_serial(e=None):
    ser = g.pop('serial', None)

    if ser is not None:
        ser.close()

"""Routing."""

from . import serial
from flask import current_app as app, jsonify


@app.route("/")
def home():
    """Landing page."""

    return "4x1 HDMI Switcher HDMI2.0 with Auto Sense and ARC"


@app.route("/sysinfo")
def sysinfo():
    """Get system information."""
    return jsonify(serial.sysinfo()), 200


""" --------------------------------------------------------------- """
""" -------------------- Signal Switching ------------------------- """
""" --------------------------------------------------------------- """

@app.route("/hdmi1")
def hdmi1():
    """Switch to HDMI input 1."""
    return jsonify(serial.send_command( b'>>HDMI1\r\n' )), 200


@app.route("/hdmi2")
def hdmi2():
    """Switch to HDMI input 2."""
    return jsonify(serial.send_command( b'>>HDMI2\r\n' )), 200


@app.route("/hdmi3")
def hdmi3():
    """Switch to HDMI input 3."""
    return jsonify(serial.send_command( b'>>HDMI3\r\n' )), 200


@app.route("/hdmi4")
def hdmi4():
    """Switch to HDMI input 4."""
    return jsonify(serial.send_command( b'>>HDMI4\r\n' )), 200


@app.route("/auto")
def auto():
    """Enable auto-switching mode."""
    return jsonify(serial.send_command( b'>>AUTO\r\n' )), 200


@app.route("/manual")
def manual():
    """Enable manual switching mode."""
    return jsonify(serial.send_command( b'>>MANUAL\r\n' )), 200


""" --------------------------------------------------------------- """
""" -------------------- Source Device Control -------------------- """
""" --------------------------------------------------------------- """


@app.route("/srcon")
def srcon():
    """Turn on the input source device, e.g. Blue-ray DVD."""
    return jsonify(serial.send_command( b'>>SRCOn\r\n' )), 200


@app.route("/srcoff")
def srcoff():
    """Turn off the input source device, e.g. Blue-ray DVD."""
    return jsonify(serial.send_command( b'>>SRCOff\r\n' )), 200


@app.route("/play")
def play():
    """Play"""
    return jsonify(serial.send_command( b'>>SRCPlay\r\n' )), 200


@app.route("/pause")
def pause():
    """Pause"""
    return jsonify(serial.send_command( b'>>SRCPause\r\n' )), 200


@app.route("/forward")
def forward():
    """Fast Forward x1"""
    return jsonify(serial.send_command( b'>>SRCForward\r\n' )), 200


@app.route("/rewind")
def rewind():
    """Fast Rewind x1"""
    return jsonify(serial.send_command( b'>>SRCBackward\r\n' )), 200


@app.route("/next")
def next():
    """Next Section"""
    return jsonify(serial.send_command( b'>>SRCSkipForward\r\n' )), 200


@app.route("/previous")
def previous():
    """Previous Section"""
    return jsonify(serial.send_command( b'>>SRCSkipBackward\r\n' )), 200


@app.route("/menu")
def menu():
    """Open the menu setting"""
    return jsonify(serial.send_command( b'>>SRCMenu\r\n' )), 200


@app.route("/back")
def back():
    """Go back"""
    return jsonify(serial.send_command( b'>>SRCBack\r\n' )), 200


@app.route("/ok")
def ok():
    """Confirm (OK)"""
    return jsonify(serial.send_command( b'>>SRCOk\r\n' )), 200


@app.route("/exit")
def exit():
    """Exit"""
    return jsonify(serial.send_command( b'>>SRCExit\r\n' )), 200


@app.route("/up")
def up():
    """Up direction"""
    return jsonify(serial.send_command( b'>>SRCUp\r\n' )), 200


@app.route("/down")
def down():
    """Down direction"""
    return jsonify(serial.send_command( b'>>SRCDown\r\n' )), 200


@app.route("/left")
def left():
    """Left direction"""
    return jsonify(serial.send_command( b'>>SRCLeft\r\n' )), 200


@app.route("/right")
def right():
    """Right direction"""
    return jsonify(serial.send_command( b'>>SRCRight\r\n' )), 200


""" --------------------------------------------------------------- """
""" -------------------- Audio Selection -------------------------- """
""" --------------------------------------------------------------- """


@app.route("/audexternal")
def audexternal():
    """Select ARC audio channel."""
    return jsonify(serial.send_command( b'>>AUDExternal\r\n' )), 200


@app.route("/audinternal")
def audinternal():
    """Select the HDMI audio input channel."""
    return jsonify(serial.send_command( b'>>AUDInternal\r\n' )), 200


""" --------------------------------------------------------------- """
""" -------------------- Display Device Control ------------------- """
""" --------------------------------------------------------------- """


@app.route("/tvon")
def tvon():
    """Turn on the display device, e.g. HDTV."""
    return jsonify(serial.send_command( b'>>TVOn\r\n' )), 200


@app.route("/tvoff")
def tvoff():
    """Turn off the display device, e.g. HDTV."""
    return jsonify(serial.send_command( b'>>TVOff\r\n' )), 200


@app.route("/volume_up")
def volume_up():
    """Volume up."""
    return jsonify(serial.send_command( b'>>TVVOL+\r\n' )), 200


@app.route("/volume_down")
def volume_down():
    """Volume down."""
    return jsonify(serial.send_command( b'>>TVVOL-\r\n' )), 200


@app.route("/mute")
def mute():
    """Mute."""
    return jsonify(serial.send_command( b'>>TVMUTE\r\n' )), 200


@app.route("/unmute")
def unmute():
    """Unmute."""
    return jsonify(serial.send_command( b'>>TVUNMUTE\r\n' )), 200


""" --------------------------------------------------------------- """
""" -------------------- Display Device Control ------------------- """
""" --------------------------------------------------------------- """


@app.route("/reset")
def reset():
    """System reset."""
    return jsonify(serial.send_command( b'>>RESET\r\n' )), 200
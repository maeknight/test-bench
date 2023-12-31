#!./python/bin/python
"""
use the owon dge2070/dge2035 arbitrary waveform
generator to do am radio alignment.
"""
import connections
import pyvisa
import tty
import sys

def open(awg):
    awg.write('source1:am:state on')
    awg.write('source1:am:internal:frequency 1000')
    awg.write('output1:state on')

def close(awg):
    awg.write('output1:state off')
    sys.exit()

# in milivolts
def set_amplitude(awg, amplitude):
    awg.write('source1:voltage {}mvpp'.format(amplitude))

# in kilohertz
def set_frequency(awg, frequency):
    awg.write('source1:frequency {}'.format(frequency * 1000))

def toggle_output(awg):
    if awg.query('output1:state?').strip() == '1':
        awg.write('output1:state off')
    else:
        awg.write('output1:state on')

def main():
    tty.setcbreak(sys.stdin.fileno())
    rm = pyvisa.ResourceManager('@py')
    awg = connections.open_awg(rm)

    open(awg)
    set_amplitude(awg, 500)
    set_frequency(awg, 455)

    commands = [
        ('1', 'for intermediate frequency coil alignment at 455khz',
            lambda: set_frequency(awg, 455)),
        ('2', 'for oscillator coil alignment at 530khz',
            lambda: set_frequency(awg, 530)),
        ('3', 'for oscillator trim cap alignment at 1600khz',
            lambda: set_frequency(awg, 1600)),
        ('4', 'for antenna coil alignment at 600khz',
            lambda: set_frequency(awg, 600)),
        ('5', 'for antenna trim cap alignment at 1400khz',
            lambda: set_frequency(awg, 1400)),
        ('6', 'to set the output amplitude to 250mv',
            lambda: set_amplitude(awg, 250)),
        ('7', 'to set the output amplitude to 500mv',
            lambda: set_amplitude(awg, 500)),
        ('8', 'to set the output amplitude to 1000mv',
            lambda: set_amplitude(awg, 1000)),
        ('9', 'to set the output amplitude to 2000mv',
            lambda: set_amplitude(awg, 2000)),
        [' ', 'to toggle the output on and off',
            lambda: toggle_output(awg)],
        ('q', 'to exit',
            lambda: close(awg)),
    ]

    for index, command in enumerate(commands):
        print("{}({}) {}".format(
            "Press " if index == 0 else "      ",
            command[0],
            command[1]
        ))

    while (True):
        key = sys.stdin.read(1)

        for command in commands:
            if command[0] == key:
                command[2]()

if __name__ == '__main__':
    main();

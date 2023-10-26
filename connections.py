AWG = "USB0::21317::4661::23300585::0::INSTR"
DMM = "ASRL/dev/ttyUSB0::INSTR"

def open_awg(rm):
    awg = rm.open_resource(AWG)

    return awg

def open_dmm(rm):
    dmm = rm.open_resource(DMM)
    dmm.baud_rate = 115200

    return dmm
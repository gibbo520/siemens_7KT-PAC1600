#!/usr/bin/env python3
import minimalmodbus
import serial
import sys
addr = int(sys.argv[1])
what = ""
if len(sys.argv) > 2:
    what = sys.argv[2]
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', addr)  # port name, slave address (in decimal)
instrument.serial.baudrate = 19200         # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 0.05          # seconds
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
instrument.clear_buffers_before_each_transaction = True


if what == 'voltage.fase_l1': 
    print(instrument.read_long(0x0002,3,False)/100)

elif what == "voltage.fase_l2": 
    print(instrument.read_long(0x0004,3,False)/100)

elif what == "voltage.fase_l3": 
    print(instrument.read_long(0x0006,3,False)/100)


elif what == "voltage.l1": 
    print(instrument.read_long(0x000E,3,False)/100)

elif what == "voltage.l2": 
    print(instrument.read_long(0x0010,3,False)/100)

elif what == "voltage.l3": 
    print(instrument.read_long(0x0012,3,False)/100)

elif what == "frequency": 
    print(instrument.read_long(0x0032,3,False)/1000)

elif what == "current.l1": 
    print(instrument.read_long(0x0008,3,False)/10000)

elif what == "current.l2": 
    print(instrument.read_long(0x000A,3,False)/10000)

elif what == "current.l3": 
    print(instrument.read_long(0x000C,3,False)/10000)

elif what == "power.l1": 
    print(instrument.read_long(0x0014,3,True)/100)

elif what == "power.l2": 
    print(instrument.read_long(0x0016,3,True)/100)

elif what == "power.l3": 
    print(instrument.read_long(0x0018,3,True)/100)

elif what == "": 
    #Voltage of fase L1-L2-L3
    print("voltage.fase_l1:",instrument.read_long(0x0002,3,False)/100)
    print("voltage.fase_l2:",instrument.read_long(0x0004,3,False)/100)
    print("voltage.fase_l3:",instrument.read_long(0x0006,3,False)/100)
    #Voltage L1-L2-L3
    print("voltage.l1:",instrument.read_long(0x000E,3,False)/100)
    print("voltage.l2:",instrument.read_long(0x0010,3,False)/100)
    print("voltage.l3:",instrument.read_long(0x0012,3,False)/100)
    #Frequency
    print("frequency:",instrument.read_long(0x0032,3,False)/1000)
    #Current L1-L2-L3
    print("current.l1:",instrument.read_long(0x0008,3,False)/10000)
    print("current.l2:",instrument.read_long(0x000A,3,False)/10000)
    print("current.l3:",instrument.read_long(0x000C,3,False)/10000)
    #Energia Attiva L1-L2-L3
    print("power.l1:",instrument.read_long(0x0014,3,True)/100)
    print("power.l2:",instrument.read_long(0x0016,3,True)/100)
    print("power.l3:",instrument.read_long(0x0018,3,True)/100)
else: 
    print("NaN")

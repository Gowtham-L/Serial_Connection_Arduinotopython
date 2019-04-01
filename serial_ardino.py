import serial
import datetime

now=datetime.datetime.now()

ser = serial.Serial('/dev/ttyACM0',9600)
s=[0]

while True:
    s[0] = ser.readline()
    print str(now)
    print s

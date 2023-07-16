import serial
import time

serialcomm = serial.Serial('COM13',9600)
while True:
    i = input()
    serialcomm.write(i.encode())
    time.sleep(0.5)

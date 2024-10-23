import serial
import sys

try:
    ser = serial.Serial(
            port='/dev/ttyUSB0',    
            baudrate=115200,
            bytesize=serial.EIGHTBITS, 
            parity=serial.PARITY_NONE, 
            stopbits=serial.STOPBITS_ONE, 
            timeout=1           
            )
    print("Open done")

    ser.write(b'1234567890')
    print("Send done")
    
    ser.close()

except serial.SerialException:

    print("Error: ", file=sys.stderr)



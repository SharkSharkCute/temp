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

    data_to_send = bytearray([1,1,1,1,1,1,1,1,1,1])
    print(len(data_to_send))
    ser.write(data_to_send)
    print("Send done")
    
    ser.close()

except serial.SerialException:

    print("Error: ", file=sys.stderr)



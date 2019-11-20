#!/usr/bin/python3

import serial, string
import time
output =" "

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=3)



while 1:
    
    print ("----")
    while output !="":
        output = ser.readline()
        output=output.decode("utf-8")
        print (output)
     
        
        
    
    
    
    
    
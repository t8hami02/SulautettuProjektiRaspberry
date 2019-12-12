#!/usr/bin/python3
#from picamera import PiCamera
import os
import pygame, sys
from pygame.locals import *
import pygame.camera
from time import sleep
import serial, string
import time
output =" "
filename =""
convertInt = ""
nucleoPIR = ""
nucleoLDR = ""
width = 1280
height =720
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(width, height))
cam.start()

#camera = PiCamera()
try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=3)
except:
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout=3)
p=0
s=0
v=0
basepath = '/home/pi/Riistakamerakuvat/'
for entry in os.listdir(basepath):
    filename = entry[0:-4]
    #print(filename)
    p=int(filename)
    if(p>s):s=p
             
    #print(s)
    
def takePic(picNum):   
    if( picNum >= 100 ):
        picNum = 0
    
    picNum+=1
    image = cam.get_image()
    cam.stop()
    pygame.image.save(image, '/home/pi/Riistakamerakuvat/'+str(picNum)+'.jpg')
    return picNum

while 1:
        
        output = ser.read()
        if(v==1):
            cam.start()
            v=0
        output=output.decode("utf-8")
        #print(output)
        #output = output.replace("\\r\\n","9")
        if (output!=""):
            nucleoLDR=int(output)

            print(nucleoLDR)
            
            #print(nucleoLDR + "\n")
            if(nucleoLDR == 1):
                print("ottaa kuvan\n")
                s = takePic(s)
                v=1
                """s+=1
                image = cam.get_image()
                cam.stop()
                v=1
                pygame.image.save(image, '/home/pi/Riistakamerakuvat/'+str(s)+'.jpg')"""
                #camera.capture('/home/pi/Riistakamerakuvat/'+str(s)+'.jpg')

        """if(nucleoLDR==0 or nucleoLDR ==1):
            print("ottaa kuvan")
            s+=1
            image = cam.get_image()
            cam.stop()
            v=1
            pygame.image.save(image, '/home/pi/Riistakamerakuvat/'+str(s)+'.jpg')"""
            #camera.capture('/home/pi/Riistakamerakuvat/'+str(s)+'.jpg')
            
            
        

    
    
    
    
#Ratespiel
import RPi.GPIO as GPIO
import time
import random
durchgang = 0
aktiv = True
ratezahl = random.randint(1,10)

LED_1 = 14            #LED_ wird auf den Pin 14 gesetzt  
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_1, GPIO.OUT)

LED_2 = 18            #LED_ wird auf den Pin 18 gesetzt  
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_2, GPIO.OUT)

LED_3 = 17            #LED_ wird auf den Pin 17 gesetzt  
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_3, GPIO.OUT)

while aktiv:
    durchgang = durchgang + 1
    print()
    print(durchgang)
    benutzereingabe = int(input("Zahl eingeben:"))
    
    
    if(durchgang == 5):
        if(benutzereingabe == ratezahl):
            print("Sehr knapp aber noch gewonnen")
        else:
            print("Ende, verloren")
            print("Es war die Zahl " +str(ratezahl))
        aktiv = False
      
        
        
    def switch_mit_if(benutzereingabe):
        if benutzereingabe == ratezahl:
            print("grün")
            print("Ende")
            GPIO.output(14,True) 
            time.sleep(2)
            GPIO.output(14,False) 
            time.sleep(0.5)    
            aktiv = False
           
    
        elif benutzereingabe > ratezahl:
                print("rot")
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(18, GPIO.OUT)
                GPIO.output(18,True) 
                time.sleep(2)
                GPIO.output(18,False)  
                time.sleep(0.5)
             
            
        
        else:
            print("gelb")
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(LED_3, GPIO.OUT)
            GPIO.output(17,True) 
            time.sleep(2)
            GPIO.output(17,False)  
            time.sleep(0.5)
           
        
          
  
benutzereingabe = int(input("Zahl eingeben:"))
print(switch_mit_if(benutzereingabe))
    












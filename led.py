import time
from pinpong.board import Board,Pin

Board("leonardo","COM3").begin()
led = Pin(Pin.D13, Pin.OUT)

while True:


     led.write_digital(1) #Output high level method 2

     print("1") #Terminal printing information.

     time.sleep(1) #Wait for 1 second and keep the state



     led.write_digital(0) #Output Low Level Method 1

     print("0") #Terminal printing information.

     time.sleep(1) #Wait for 1 second and keep the state
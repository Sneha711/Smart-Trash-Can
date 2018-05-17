#Libraries
import RPi.GPIO as GPIO
import time
import smtplib
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 22
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

flag = 0
i = 0
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
	try:
		while True:
			dist = distance()

			if dist <5 :
				flag = 1
				i = i+1

			if dist >=5:
				i = 0

			if i == 1:
				server = smtplib.SMTP('smtp.gmail.com', 587)
				server.starttls()
				server.login("yourmail@gmail.com", "password")
				msg = "Dustbin Alert.... Dustbin Full"
				server.sendmail("yourmail@gmail.com", "mailofreceiver@gmail.com", msg)
				server.quit()


			print ("Measured Distance = %.1f cm" % dist)
			time.sleep(1)
 
        # Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()
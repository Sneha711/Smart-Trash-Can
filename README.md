# Smart-Trash-Can
Touchless Automatic Motion Sensor Trash Can with fullness detection. This Smart Trash Can is integrated
with mail system which notifies the user when it’s full by sending a mail.

### Components used:
* Raspberry Pi 3
* 2 Ultrasonic Sensors HC-SR04
* TowerPro MG995 Servo Motor
* A Mini Trash Can.

### System Setup
 
 System Setup 1:
![](https://github.com/Sneha711/Smart-Trash-Can/blob/master/dustbin1.jpeg | width=50)

System Setup 2:
![alt text](https://github.com/Sneha711/Smart-Trash-Can/blob/master/dustbin2.jpeg "System Setup 2" =250x250)

There are two python files:
* `mail_ultrasonic_distance.py`: Code for detecting user proximity(using ultrasonic sensor) and accordingly opening and closing the Trash Can(using Servo motor).

* `servo_ultrasonic_distance.py`: Code for detecting the fullness of the Trash Can(using ultrasonic sensor) and accordingly notifying the user by sending mail(using smtp).


To make the Smart Trash Can work run both the files on raspberry pi. For that follow the steps:
1] Open terminal and access the raspberry pi from it.
2] Run both the files.


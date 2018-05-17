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
<p align="center">
<img src="https://github.com/Sneha711/Smart-Trash-Can/blob/master/dustbin1.jpeg" width=40%>
</p>

System Setup 2:
<p align="center">
<img src="https://github.com/Sneha711/Smart-Trash-Can/blob/master/dustbin2.jpeg" width=40%>
</p>


### Flow Diagram

<p align="center">
<img src="https://github.com/Sneha711/Smart-Trash-Can/blob/master/IOT.jpeg" width=40%>
</p>


### How it works
There are two python files:
* `mail_ultrasonic_distance.py`: Code for detecting user proximity(using ultrasonic sensor) and accordingly opening and closing the Trash Can(using Servo motor).

* `servo_ultrasonic_distance.py`: Code for detecting the fullness of the Trash Can(using ultrasonic sensor) and accordingly notifying the user by sending mail(using smtp).


### Running
To make the Smart Trash Can work run follow the steps: <br>
1] Make the required connections <br>
2] Fork this project to your GitHub account <br>
3] After forking, clone the repository using the following command: `git clone https://github.com/Sneha711/Smart-Trash-Can.git` <br>
4] Enable SSH on the Raspberry Pi <br>
5] Login to Raspberry Pi. For example with `ssh pi@your_raspberry_pi_ip` <br>
6] Move both the files on Raspberry Pi <br>
7] Run both the files at the same time using the command: `python servo_ultrasonic_distance.py;python mail_ultrasonic_distance.py`


### Working

<p align="center">
<img src="https://github.com/Sneha711/Smart-Trash-Can/blob/master/working.gif" width=40%>
</p>



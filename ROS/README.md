👋 A Python program that, using ALL the methods from the robot_control_class.py Python script, helps the Turtlebot robot to get out of the maze

✨get_laser (direction): As the name itself says, this method will allow you to get data from the laser of the robot. You will need to pass one parameter to this method:
           >>direction: Here you will specify a number between 0 and 719, which will indicate the direction of the laser reading.
           
✨get_laser_full(): As the name itself says, this method will allow you to get all the data from ALL the laser beams of the robot. As I've said before, this is a total of 719 different readings. So, when called, this method will return a LIST containing all the 719 different readings from the laser beams.

✨move_straight(): As the name says, this method will allow you to start moving the robot in a straight line.

✨stop_robot(): As the name says, this method will allow you to stop the robot from moving.

✨move_straight_time(motion, speed, time): As the name itself says, this method will allow you to move the robot in a straight line. You will need to pass three parameters to it.
           >>motion: Specify here if you want your robot to move forward ("forward") or backward ("backward").
           >>speed: Specify here the speed at which you want your robot to move (in m/s).
           >>time: Specify here how long you want your robot to keep moving (in seconds).

✨turn (clockwise, speed, time): As the name itself says, this method will allow you to turn the robot. You will need to pass three parameters to it.
           >>clockwise: Specify here whether you want your robot to turn clockwise ("clockwise") or counter-clockwise ("counter-clockwise").
           >>speed: Specify here the speed at which you want your robot to turn (in rad/s).
           >>time: Specify here how long you want your robot to keep turning (in seconds).

✨rotate (degrees): This method will allow your robot to rotate for the specified number of degrees.
           >>degrees: The number of degreees you want your robot to rotate.!
           
👀[image](https://user-images.githubusercontent.com/108583279/202231128-6654df3e-0618-4c87-b554-b561f8f97039.png)
👀![image](https://user-images.githubusercontent.com/108583279/202231350-4552b8bb-34ea-4bd4-9866-a7af502475f3.png)


import time
from robot_control_class import RobotControl
import math
import sys

robotcontrol = RobotControl()


class Robo:

    def __init__(self):
        print("Start...")
        self.frontlaser = robotcontrol.get_laser(360)
        self.botmove_speed = 2
        self.botmove_time = 1
        self.botturn_clockwise = "clockwise"
        self.botturn_speed = 1
        self.botturn_time = 1

    def botmove(self):
        while self.frontlaser > 1:
            robotcontrol.move_straight()
            self.frontlaser = robotcontrol.get_laser(360)
            print("distance: ", self.frontlaser)

        robotcontrol.stop_robot()
        print("Wall !!!... ")

    def botturn(self):
        distance_right = robotcontrol.get_laser(0)
        distance_left = robotcontrol.get_laser(719)
        print("right", distance_right, "left", distance_left)
        if distance_right > distance_left:
            print("Turn right")
            while self.frontlaser < 1:
                robotcontrol.turn("anticlockwise", self.botturn_speed, self.botturn_time)
                self.frontlaser = robotcontrol.get_laser(360)
                print("right: distance: ", self.frontlaser)
        else:
            print("Turn left")
            while self.frontlaser < 1:
                robotcontrol.turn(self.botturn_clockwise, self.botturn_speed, self.botturn_time)
                self.frontlaser = robotcontrol.get_laser(360)
                print("left: distance: ", self.frontlaser)

        robotcontrol.stop_robot()
        print("Let's Go!!!.. ")

    def stopbot(self):
        distance_right = robotcontrol.get_laser(0)
        distance_left = robotcontrol.get_laser(719)
        if self.frontlaser == math.inf:
            distance_right = robotcontrol.get_laser(0)
            distance_left = robotcontrol.get_laser(719)
            if distance_right == math.inf and distance_left == math.inf:
                print("Solved!!!...")


if __name__ == '__main__':

    robo = Robo()

    while not robotcontrol.ctrl_c:
        robo.botmove()
        robo.botturn()
        robo.stopbot()
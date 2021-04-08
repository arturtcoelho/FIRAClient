#!/usr/bin/env python3

from bridge import Actuator, Replacer, Vision, Referee, NUM_BOTS, convert_angle

from math import pi, fmod, atan2, fabs

def main_strategy(field):
    """Sets all objetives to ball coordinates."""
    ball = field["ball"]
    objectives = [{"index": i} for i in range(NUM_BOTS)]
    for obj in objectives:
        obj["x"] = ball["x"]
        obj["y"] = ball["y"]

    return objectives

def smallestAngleDiff(target, source):
    """Gets the smallest angle between two points in a arch"""
    a = fmod(target + 2*pi, 2*pi) - fmod(source + 2 * pi, 2 * pi)

    if (a > pi):
        a -= 2 * pi
    else:
        if (a < -pi):
            a += 2 * pi

    return a


def controller(field, objectives, mray):
    """Basic PID that sets the speed of each motor to send bot to coordinate"""
    speeds = [{"index": i} for i in range(NUM_BOTS)]

    for i, s in enumerate(speeds):
        Kp = 20
        Kd = 2.5

        try:
            controller.lastError
        except AttributeError:
            controller.lastError = 0

        rightMotorSpeed = 0
        leftMotorSpeed = 0

        reversed = False

        our_bots = field["yellow"] if mray else field["blue"] 

        angle_rob = our_bots[i]["angle"]

        angle_obj = atan2( objectives[i]["y"] - our_bots[i]["y"], 
                            objectives[i]["x"] - our_bots[i]["x"] )

        error = smallestAngleDiff(angle_rob, angle_obj)

        if (fabs(error) > pi / 2.0 + pi / 20.0):
            reversed = True
            angle_rob = convert_angle(angle_rob + pi)
            error = smallestAngleDiff(angle_rob, angle_obj)

        motorSpeed = (Kp * error) + (Kd * (error - controller.lastError))
        
        controller.lastError = error

        baseSpeed = 30

        motorSpeed = motorSpeed if motorSpeed < baseSpeed else baseSpeed
        motorSpeed = motorSpeed if motorSpeed > -baseSpeed else -baseSpeed

        if (motorSpeed > 0):
            leftMotorSpeed = baseSpeed
            rightMotorSpeed = baseSpeed - motorSpeed
        else:
            leftMotorSpeed = baseSpeed + motorSpeed
            rightMotorSpeed = baseSpeed

        if (reversed):
            if (motorSpeed > 0):
                leftMotorSpeed = -baseSpeed + motorSpeed
                rightMotorSpeed = -baseSpeed
            else:
                leftMotorSpeed = -baseSpeed
                rightMotorSpeed = -baseSpeed - motorSpeed

        s["left"] = leftMotorSpeed
        s["right"] = rightMotorSpeed
    return speeds

if __name__ == "__main__":

    # Choose team (my robots are yellow)
    mray = False

    # Initialize all clients
    actuator = Actuator(mray, "127.0.0.1", 20011)
    replacement = Replacer(mray, "224.5.23.2", 10004)
    vision = Vision(mray, "224.0.0.1", 10002)
    referee = Referee(mray, "224.5.23.2", 10003)

    # Main infinite loop
    while True:
        referee.update()
        ref_data = referee.get_data()

        vision.update()
        field = vision.get_field_data()

        if ref_data["game_on"]:

            objectives = main_strategy(field)

            speeds = controller(field, objectives, mray)

            actuator.send_all(speeds)

        elif ref_data["foul"] != 7:
            # foul behaviour
            actuator.stop()

        else:
            # halt behavior
            actuator.stop()
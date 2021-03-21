#!/usr/bin/env python3

from bridge import Actuator, Replacer, Vision, Referee, \
                    Object, Objective, Speed, Field, Ref_data, \
                    interrupt_type as it, convert_angle, NUM_BOTS

from math import pi, fmod, atan2, fabs

from time import sleep

def main_strategy(field):
    """Sets all objetives to ball coordinates."""
    ball = field.ball
    objectives = [Objective() for _ in range(NUM_BOTS)]
    for obj in objectives:
        obj.x = ball.x
        obj.y = ball.y

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


def controler(field, objectives):
    """Basic PID that sets the speed of each motor to send bot to coordinate"""
    speeds = [Speed() for _ in range(NUM_BOTS)]

    for i, s in enumerate(speeds):
        Kp = 20
        Kd = 2.5
        lastError = 0

        rightMotorSpeed = 0
        leftMotorSpeed = 0

        reversed = False

        angle_rob = field.our_bots[i].angle

        angle_obj = atan2( objectives[i].y - field.our_bots[i].y, 
                            objectives[i].x - field.our_bots[i].x )

        error = smallestAngleDiff(angle_rob, angle_obj)

        if (fabs(error) > pi / 2.0 + pi / 20.0):
            reversed = True
            angle_rob = convert_angle(angle_rob + pi)
            error = smallestAngleDiff(angle_rob, angle_obj)

        motorSpeed = (Kp * error) + (Kd * (error - lastError))
        
        lastError = error

        baseSpeed = 30

        motorSpeed = motorSpeed if motorSpeed < 30 else 30
        motorSpeed = motorSpeed if motorSpeed > -30 else -30

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

        s.left = leftMotorSpeed
        s.right = rightMotorSpeed
    return speeds

if __name__ == "__main__":

    # Choose team (my robots are yellow)
    mray = False

    # Initialize all clients
    actuator = Actuator(mray, "127.0.0.1", 20011)
    replacement = Replacer(mray, "224.5.23.2", 10004)
    vision = Vision("224.0.0.1", 10002)
    referee = Referee("224.5.23.2", 10003)

    # Initialize our data
    ref_data = Ref_data()
    field = Field(mray)
    objectives = []
    speeds = []
    positions = []

    # Main infinite loop
    while True:
        referee.update()
        referee.get_data(ref_data)

        if ref_data.game_on:
            vision.update()
            vision.fill_field(field)

            objectives = main_strategy(field)

            speeds = controler(field, objectives)

            actuator.send_all(speeds)

        elif ref_data.foul != it.HALT:

            # positions = position_strategy(ref_data) # TODO

            replacement.place_all(positions)

        else:
            print("Game Halted")
            sleep(0.1)
            # halt behavior
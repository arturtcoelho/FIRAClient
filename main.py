#!/usr/bin/env python3

from bridge import (Actuator, Replacer, Vision, Referee, 
                        NUM_BOTS, convert_angle, Entity)

from math import pi, fmod, atan2, fabs, sqrt

def main_strategy(field):
    """Sets all objetives to ball coordinates."""
    ball = field["ball"]
    objectives = [Entity(index=i) for i in range(NUM_BOTS)]

    mray = field['mray']
    if mray:
        if ball.vx > 0:
            ball_front = True
        else:         
            ball_front = False
    else:
        if ball.vx < 0:
            ball_front = True
        else:         
            ball_front = False

    BALL_STOPED = 1

    GK_POINT = Entity(x=160, y=65) if mray else Entity(x=11, y=65)
    DEF_POINT = Entity(x=125, y=45) if mray else Entity(x=45, y=45)
    ATK_POINT = Entity(x=45, y=45) if mray else Entity(x=125, y=45)
    ATK_SECONDARY = Entity(x=45, y=85) if mray else Entity(x=125, y=85)

    if (abs(ball.vx) <= BALL_STOPED): # ball isnt moving
        goalkeeper = GK_POINT
        defenser = ball
        atacker = ATK_POINT
    elif (ball_front): # ball is going back
        goalkeeper = GK_POINT
        defenser = ball
        atacker = DEF_POINT
    else: # ball is going fowards
        goalkeeper = ATK_POINT
        defenser = ATK_SECONDARY
        atacker = ball

    closer = field['our_bots'].copy()
    closer.sort(key=lambda k: sqrt((k.x-ball.x)**2 + (k.y-ball.y)**2)) # order in proximity to ball

    back = field['our_bots'].copy()
    back.sort(key=lambda k: k.x if mray else -k.x) # order in field x location

    objectives = [None for _ in range(NUM_BOTS)]
    # TODO add gk, def and atk to objecives

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


def controller(field, objectives):
    """
        Basic PID controller that sets the speed of each motor 
        sends robot to objective coordinate
        Courtesy of RoboCin
    """

    speeds = [{"index": i} for i in range(NUM_BOTS)]
    our_bots = field["our_bots"]

    # for each bot
    for i, s in enumerate(speeds):
        Kp = 20
        Kd = 2.5

        try:
            controller.lastError
        except AttributeError:
            controller.lastError = 0

        right_motor_speed = 0
        left_motor_speed = 0

        reversed = False
        
        objective = objectives[i]
        our_bot = our_bots[i]

        angle_rob = our_bot.a

        angle_obj = atan2( objective.y - our_bot.y, 
                            objective.x - our_bot.x )

        error = smallestAngleDiff(angle_rob, angle_obj)

        if (fabs(error) > pi / 2.0 + pi / 20.0):
            reversed = True
            angle_rob = convert_angle(angle_rob + pi)
            error = smallestAngleDiff(angle_rob, angle_obj)

        # set motor speed based on error and K constants
        error_speed = (Kp * error) + (Kd * (error - controller.lastError))
        
        controller.lastError = error

        baseSpeed = 30

        # normalize
        error_speed = error_speed if error_speed < baseSpeed else baseSpeed
        error_speed = error_speed if error_speed > -baseSpeed else -baseSpeed

        if (error_speed > 0):
            left_motor_speed = baseSpeed
            right_motor_speed = baseSpeed - error_speed
        else:
            left_motor_speed = baseSpeed + error_speed
            right_motor_speed = baseSpeed

        if (reversed):
            if (error_speed > 0):
                left_motor_speed = -baseSpeed + error_speed
                right_motor_speed = -baseSpeed
            else:
                left_motor_speed = -baseSpeed
                right_motor_speed = -baseSpeed - error_speed

        s["left"] = left_motor_speed
        s["right"] = right_motor_speed
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

        if ref_data["game_on"] or True:

            objectives = main_strategy(field)

            speeds = controller(field, objectives)

            actuator.send_all(speeds)

        elif ref_data["foul"] != 7:
            # foul behaviour
            actuator.stop()

        else:
            # halt behavior
            actuator.stop()
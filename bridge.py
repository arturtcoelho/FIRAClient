
"""
This module was created to interact with the FIRAClient 
located on https://github.com/yapiraUFPR/FIRAClient

This interaction is made with the file libfira.cpp,
witch generates the shared object libfira.so used here.

The classes located here use the lib subspace to store
their respective client data.
"""

__author__ = "Artur Coelho - github.com/arturtcoelho"

# The main import for this bridge, 
import ctypes
# imports used types 
from ctypes import c_double, \
                    c_char_p, \
                    c_uint16, \
                    c_int32, \
                    c_bool

from math import fmod, pi

from enum import Enum

# Loads the compiled shared library based on libfira.cpp
# See README.md to compile and usage

# The lib object will contain the C++ local clients 
# witch save their respective data
try:
    lib = ctypes.cdll.LoadLibrary('./libfira.so')
except Exception as e:
    try: 
        lib = ctypes.cdll.LoadLibrary('./FIRAClient/libfira.so')
    except:
        print("Error opening lib! Aborting", e)
        exit()

# Default bot number
NUM_BOTS = 3

LENGTH = 1.7 / 2.0
WIDTH = 1.3 / 2.0

def convert_width(w) -> float:
    """
    Converts width from the simulator data to centimetres
    with origin point on bottom left corner of field
    """
    try:
        return (WIDTH + w) * 100 
    except TypeError:
        return 0

def convert_length(d) -> float:
    """
    Converts width from the simulator data to centimetres
    with origin point on bottom left corner of field
    """
    try:
        return (LENGTH + d) * 100
    except TypeError:
        return 0

def convert_angle(a) -> float:
    """
    Converts the angle from full radians to 
    -Pi/2 to Pi/2 radians range
    """
    try:
        angle = fmod(a, 2*pi)
        if (angle < -pi):
            return angle + 2*pi
        if (angle > pi):
            return angle - 2*pi
        return angle
    except TypeError:
        return 0

class Object():
    """
    Class to generic object position and orientation.
    """
    x = 0.0
    y = 0.0
    angle = 0.0
    vx = 0.0
    vy = 0.0
    vangle = 0.0

class Objective():
    """Generic objective""" 
    x = 0.0
    y = 0.0
    angle = 0.0

class Speed():
    """Generic objective""" 
    left = 0.0
    right = 0.0

class Field():
    """
    Contains the data fetched from the vision client
    The team color, and ball and bots locations.
    """

    def __init__(self, my_robots_are_yellow):
        """
        Constructor for the class,
        initialize atributes to default values.
        """
        self.my_robots_are_yellow = my_robots_are_yellow
        self.ball = None
        self.our_bots = [[] for _ in range(NUM_BOTS)]
        self.their_bots = [[] for _ in range(NUM_BOTS)]

    def clean(self):
        """
        Clean to default values.
        """
        self.ball = None
        self.our_bots = [[] for _ in range(NUM_BOTS)]
        self.their_bots = [[] for _ in range(NUM_BOTS)]
        
class Ref_data():
    """
    Contains the data fetched from the referee client.
    """

    def __init__(self):
        """
        Constructor for the class,
        initialized to default values.
        """
        self.clear()    

    def clear(self):
        """
        Set atributes to default values.
        """
        self.foul = 7
        self.game_on = False
        self.yellow = False
        self.quad = 0
        self.is_game_halt = True

class interrupt_type(Enum):
    """Enumerate a list of foul types"""
    FREE_KICK = 0
    PENALTY_KICK = 1
    GOAL_KICK = 2
    FREE_BALL = 3
    KICKOFF = 4
    STOP = 5
    GAME_ON = 6
    HALT = 7

# Client classes

class Vision():
    """
    Class for the vision client, 
    Use one instance at a time to minimize network errors.
    """

    def __init__(self, addr = "224.0.0.1", port = 10002):
        """
        Constructor initialized with adress and port

        default address: "224.0.0.1"
        default port: 10002
        Fetches the first field.
        """

        # we need to convert the string type
        c_string = addr.encode('utf-8')
        lib.actuator_init.argtypes = [c_char_p, c_uint16, c_bool]

        lib.vision_init(c_string, c_uint16(port))
        # already update once
        self.update()

    def update(self):
        """Fetches client data."""
        return lib.vision_update_field()
        
    def fill_field(self, field):
        """
        Fills the field with client data

        Stores our_bots, their bots and ball
        Use after the update method.
        """

        # Checks parameter type 
        if (type(field) != Field):
            raise TypeError(field)
        try:
            # fills respective bots
            for i in range(NUM_BOTS):
                if field.my_robots_are_yellow:
                    field.our_bots[i] = self.get_robot(i, True)
                    field.their_bots[i] = self.get_robot(i, False)
                else:
                    field.our_bots[i] = self.get_robot(i, False)
                    field.their_bots[i] = self.get_robot(i, True)
            field.ball = self.get_ball()
            return field
        except Exception as e:
            print(e)
            return None

    def get_ball(self):
        """
        Returns a Object with the ball data
        Use after the update method.
        """

        try:
            # set return type for double
            # speeds typeset
            lib.vision_get_ball_x.restype = c_double
            lib.vision_get_ball_y.restype = c_double
            # positions typeset
            lib.vision_get_ball_vx.restype = c_double
            lib.vision_get_ball_vy.restype = c_double

            # fills and return the new object
            ball = Object()
            # positions
            ball.x = convert_length(lib.vision_get_ball_x())
            ball.y = convert_width(lib.vision_get_ball_y())
            # speeds
            ball.vx = lib.vision_get_ball_vx()
            ball.vy = lib.vision_get_ball_vy()
            ball.angle = 0

            return ball
        except TypeError:
            return None

    def get_robot(self, index, yellow):
        """
        Returns a Object with the bot data
        bot is given by index and get_yellow parametres
        Use after the update method.
        """

        try:
            # set the return type to double
            # position typeset
            lib.vision_robot_x.restype = c_double
            lib.vision_robot_y.restype = c_double
            lib.vision_robot_angle.restype = c_double
            # speeds typeset
            lib.vision_robot_vx.restype = c_double
            lib.vision_robot_vy.restype = c_double
            lib.vision_robot_vangle.restype = c_double

            # fills and return bot object
            # get position
            bot = Object()
            bot.x = convert_length(
                lib.vision_robot_x(c_int32(index), c_bool(yellow)))
            bot.y = convert_width(
                lib.vision_robot_y(c_int32(index), c_bool(yellow)))
            bot.angle = convert_angle(
                lib.vision_robot_angle(c_int32(index), c_bool(yellow)))
            # get speeds
            bot.vx = lib.vision_robot_vx(c_int32(index), c_bool(yellow))
            bot.vy = lib.vision_robot_vy(c_int32(index), c_bool(yellow))
            bot.vangle = lib.vision_robot_vangle(c_int32(index), c_bool(yellow))

            return bot
        except TypeError:
            return None

    def __del__(self):
        """Closes network conection"""
        lib.vision_term()

class Referee():
    """
    Referee client class, 
    Use one instance at a time to minimize network errors.
    """

    def __init__(self, addr = "224.5.23.2", port = 10003):
        """
        Initialize client on addr and port

        default adress: "224.5.23.2"
        default port: 10003
        Fetches the first data.
        """

        # we need to convert the string type
        c_string = addr.encode('utf-8')
        lib.actuator_init.argtypes = [c_char_p, c_uint16, c_bool]

        lib.referee_init(c_string, c_uint16(port))
        self.update()

    def update(self):
        """Fetches new referee data."""
        lib.referee_update()

    def get_data(self, data):
        """
        Fills the data structure with the new data from referee
        or default values (game stoped).
        """
        if (type(data) != Ref_data):
            raise TypeError(data)
        data.clear()
        data.foul = self.interrupt_type()
        data.game_on = self.is_game_on()
        data.yellow = self.is_yellow()
        data.quad = self.get_quadrant()
        data.is_game_halt = self.interrupt_type() == 7

    def interrupt_type(self):
        """
        returns the type of interrupt
        being it a foul, game_on or halt
        From libfira.cpp:
            FREE_KICK = 0
            PENALTY_KICK = 1
            GOAL_KICK = 2
            FREE_BALL = 3
            KICKOFF = 4
            STOP = 5
            GAME_ON = 6
            HALT = 7
        """
        return lib.referee_get_interrupt_type()

    def is_game_on(self):
        """returns (bool) GAME_ON == True."""
        return lib.referee_is_game_on()


    def color(self):
        """
        Returns interrupt color data from libira:
            BLUE = 0,
            YELLOW = 1,
            NONE = 2,
        """
        return lib.referee_interrupt_color()

    def is_yellow(self):
        """returns foul color == yellow."""
        return self.color() == 1

    def get_quadrant(self):
        """returns quadrant on witch foul happened."""
        return lib.referee_get_interrupt_quadrant()

    def __del__(self):
        """Closes network conection."""
        lib.referee_term()

class Actuator():
    """
    Actuator client class, 
    Use one instance at a time to minimize network errors.
    """

    def __init__(self, my_robots_are_yellow, addr = "224.0.0.1", port = 10002):
        """
        Initialize client on addr and port

        default adress: "224.0.0.1", 
        default port: 10002
        requires bool team_color to indicate later comands.
        """

        # we need to convert the string type
        c_string = addr.encode('utf-8')
        lib.actuator_init.argtypes = [c_char_p, c_uint16, c_bool]

        lib.actuator_init(c_string, 
                            c_uint16(port), 
                            c_bool(my_robots_are_yellow))

    def send(self, index, left, right):
        """
        sends motor speeds for one robot indicated by
        index on team initialized.
        """
        lib.actuator_send_command(c_int32(index), 
                                    c_double(left), 
                                    c_double(right))

    def send_all(self, speeds):
        """sends a list of speed commands"""
        for i, s in enumerate(speeds):
            try:
                self.send(i, s.left, s.right)
            except Exception as e:
                print("speed exception:", e)

    def __del__(self):
        """Closes network conection."""
        lib.actuator_term()

class Replacer():
    """
    Actuator client class, 
    Use one instance at a time to minimize network errors.
    """

    def __init__(self, my_robots_are_yellow, addr = "224.5.23.2", port = 10004):
        """
        Initialize client on addr and port

        default adress: "224.5.23.2"
        default port: 10004
        requires bool team_color to later comands.
        """
        c_string = addr.encode('utf-8')
        lib.actuator_init.argtypes = [c_char_p, c_uint16, c_bool]

        lib.replacer_init(c_string, 
                            c_uint16(port), 
                            c_bool(my_robots_are_yellow))

    def place(self, index, x, y, angle):
        """Sends a index indicated bot to x, y and angle."""
        lib.replacer_place_robot(c_int32(index), 
                                    c_double(x), 
                                    c_double(y), 
                                    c_double(angle))

    def place_all(self, placement):
        """Sends a list of positions to location"""
        for p in placement:
            try:
                self.place(p.index, p.x, p.y, p.angle)
            except Exception as e:
                print("placement exception:", e)

        lib.replacer_send_frame()

    def __del__(self):
        """Closes network conection."""
        lib.replacer_term()

# Base test run
if __name__ == "__main__":
    try:
        my_robots_are_yellow = False

        # initializes all classes with default ports
        vision = Vision()
        referee = Referee()
        actuator = Actuator(my_robots_are_yellow)
        replacer = Replacer(my_robots_are_yellow)
    except Exception as e:
        print("An error occured during execution:", e)
        exit()
    print()
    print("Test completed!")
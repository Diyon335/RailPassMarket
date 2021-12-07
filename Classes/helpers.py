"""
This file contains helper functions and enums
"""


from enum import Enum
import re

"""
Enumerations for the classes of rail passes
"""


# rail pass level enum
class RailPassLevel(Enum):
    VIP = 1
    ECONOMIC = 2


"""
Returns an enum, based on user input
"""


def from_user_input_level(input_value):
    if input_value == 1:
        return RailPassLevel.VIP
    elif input_value == 2:
        return RailPassLevel.ECONOMIC
    else:
        raise NotImplementedError

def enum_to_level(input_value):
    if input_value == "RailPassLevel.VIP":
        return 1
    elif input_value == "RailPassLevel.ECONOMIC":
        return 2
    else:
        raise NotImplementedError


"""
Returns a boolean indicating the the string contains any non-alphabet characters
"""


def invalid_string(string):
    return re.search(r"[\d\W]+", string)


"""
Returns a boolean indicating whether the entered string is of a valid email format
"""


def valid_email(string):
    return re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", string)


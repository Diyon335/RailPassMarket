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
Returns a boolean indicating the the string contains any non-alphabet characters
"""


def is_valid_string(string):
    return re.search(r"[\d\W]+", string)


"""
Returns a boolean indicating whether the entered string is of a valid email format
"""


def is_valid_email(string):
    return re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", string)


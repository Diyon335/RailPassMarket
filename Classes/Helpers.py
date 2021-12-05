from enum import Enum
# these are the enumeration types needed
# rail pass type enum can be extended as needed
class RailPassType(Enum):
    SINGLE = 1
    MULTI = 2


# rail pass level enum
class RailPassLevel(Enum):
    VIP = 1
    ECONOMIC = 2


# methods to help the conversions from user inputs to enums and vice versa
def from_user_input_type(input_value):
    if input_value == 1:
        return RailPassType.SINGLE
    elif input_value == 2:
        return RailPassType.MULTI
    else:
        raise NotImplementedError


def from_user_input_level(input_value):
    if input_value == 1:
        return RailPassLevel.VIP
    elif input_value == 2:
        return RailPassLevel.ECONOMIC
    else:
        raise NotImplementedError

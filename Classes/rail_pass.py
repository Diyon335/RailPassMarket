"""
Class for the Rail Pass
"""

from Classes.helpers import from_user_input_level
from datetime import datetime

class RailPass:

    """
    Constructor for the RailPass class
    """

    def __init__(self, price, rail_pass_level, rides_left, rail_pass_id, owner_id, issue_date):

        try:
            self._owner_id = int(owner_id)
            self._rail_pass_id = int(rail_pass_id)

            if int(rides_left) > 10 or int(rides_left) < 1:
                raise ValueError
            else:
                self._rides_left = int(rides_left)  # restriction here it must be less than 10 rides

            self._rail_pass_level = from_user_input_level(int(rail_pass_level))  # vip or economic using enums
            self._price = int(price)  # to be decided later how to implement that
            self._issue_date = datetime.strptime(issue_date, '%d/%m/%Y')  # the date the ticket was bough on

        except ValueError as e:
            print("Incorrect value entered")
            print(e)
        except TypeError as e:
            print("Incorrect type entered")
            print(e)

    """
    Returns the ID of the rail pass
    """
    def get_id(self):
        return self._rail_pass_id

    """
    Returns the cost of the rail pass
    """

    def get_cost(self):
        return self._price

    """
    Returns the issue date of the rail pass
    """

    def get_issue_date(self):
        return self._issue_date

    """
    Returns the number of rides left on the rail pass
    """

    def get_rides_left(self):
        return self._rides_left

    """
    Default toString method of the class
    """

    def __str__(self):
        return f"€{self._price}:{self._rail_pass_level}:{self._rides_left}:{self._rail_pass_id}:{self._owner_id}:{self._issue_date}"

    __repr__ = __str__


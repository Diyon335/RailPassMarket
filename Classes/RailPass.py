from abc import ABC, abstractmethod
from Classes.Helpers import from_user_input_level
from Classes.Helpers import from_user_input_type


# abstract base class
class Component(ABC):
    # Constructor
    def __init__(self, name, description):
        self._name = name
        self._description = description


# inherit abstract class component
class RailPass(Component):
    def __init__(self, name, description, price, railpass_type, railpass_level, number_rides_left, ticket_id, owner_id, sold, issue_date,
                 sold_date , want_to_sell):
        Component.__init__(self, name, description)
        self._owner_id = owner_id
        self._ticket_id = ticket_id
        self._number_rides_left = number_rides_left  # restriction here it must be less than 1o rides
        self._level = from_user_input_level(railpass_level)  # vip or economic using enums
        self._type = from_user_input_type(railpass_type)  # single or multi using enums
        self._price = price  # to be decided later how to implement that
        self._sold = sold  # this ticket is sold or not  false or true
        self._issue_date = issue_date  # the date the ticket was bough on 
        self._sold_date = sold_date  # the date of selling and null if not sold
        self._want_to_sell = want_to_sell #the user want to sell or not true or false flag

    def __str__(self):
        return 'Ticket is is = '+ str(self._ticket_id) +' , Number of rides is = '+ str(self._number_rides_left)\
               + ', The ticket is sold or not = '+ str(self._sold) + ' , The price of the ticket = '+ str(self._price)\
               +' , The owner want to sell or not = '+ str( self._want_to_sell)

    def get_ticket_id(self):
        return self._ticket_id

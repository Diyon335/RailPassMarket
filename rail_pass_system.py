from Files import file_parser
from uuid import uuid4
from datetime import datetime,timedelta

"""
Class for the rail pass trader system
"""


class RailPassSystem:

    """
    Constructor of the class
    """

    def __init__(self):
        self._clients = file_parser.parse_clients()
        self._rail_passes = file_parser.parse_rail_passes()

    """
    Adds a client to the list of clients
    """

    def add_client(self, person):
        self._clients.append(person)

    """
    Adds a rail pass to the list of rail passes
    """

    def add_rail_pass(self, rail_pass):
        self._rail_passes.append(rail_pass)

    """
    Returns a list of clients in the system
    """

    def get_clients(self):
        return self._clients

    """
    Returns a list of rail passes in the system
    """

    def get_rail_passes(self):
        return self._rail_passes

    """
    Returns all rail passes that have the required number of rides and are valid for the date of travel
    """

    def filter_rail_passes(self, travel_date, number_of_passengers):
        return list(filter(lambda rail_pass: rail_pass.get_issue_date() < travel_date < rail_pass.get_issue_date() + timedelta(days=365)
                                             and number_of_passengers < rail_pass.get_rides_left(), self._rail_passes))


    """
    Closes the system and writes all data to the database
    """

    def close(self):
        file_parser.write_clients(self._clients)
        file_parser.write_rail_passes(self._rail_passes)

    """
    Runs the system. While running, the user is prompted with buying/selling options until they want
    """

    def run(self):
        # Once called, the user has various options while this loop is running - such as uploading a ticket for sale, etc
        # TODO Implement various prompts (sell tickets, search and buy for tickets)
        while True:
            # Temporary break - just for testing
            break

        self.close()

    """
    Generates a random UUID
    """

    def generate_id(self):
        return uuid4()

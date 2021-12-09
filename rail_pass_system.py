from Files import file_parser
from uuid import uuid4
from datetime import datetime, timedelta

"""
Class for the rail pass trader system
"""


class RailPassSystem:
    """
    Constructor of the class
    """

    def __init__(self):
        self._clients = file_parser.parse_clients_and_passes()[0]
        self._rail_passes = file_parser.parse_clients_and_passes()[1]
        # property that holds current client
        self._client = None

    """
    Sets the current user of the system
    """

    def set_current_user(self, client):
        self._client = client

    """
    Gets the current user of the system
    """

    def get_current_user(self):
        return self._client

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
        return list(filter(
            lambda rail_pass: rail_pass.get_issue_date() < travel_date < rail_pass.get_issue_date() + timedelta( days=365) and number_of_passengers < rail_pass.get_rides_left() and self.get_current_user().get_person_id() != rail_pass.get_owner_id(), self._rail_passes))

    """
    Returns a boolean, indicating if the client exists in the database
    """

    def client_exists(self, email, password=None):

        for client in self._clients:

            if password is None:
                if client.get_email().lower() == email.lower():
                    return True

            else:
                if client.get_email().lower() == email.lower() and client.get_password() == password:
                    return True

        return False

    """
    Gets the client object based on email and password
    """

    def get_client(self, email, password):
        # Assumes client exists. Returns the first element (desired client) of a one-element list
        return list(
            filter(lambda client: client.get_email().lower() == email.lower() and password == client.get_password(),
                   self._clients))[0]

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
            prompt = input("Would you like to buy or sell a rail pass?")

            if "sell" in prompt:
                pass  # Not implemented yet
            elif "buy" in prompt:

                case = 0
                travel_date = ""
                number_of_passengers = ""

                while True:

                    try:
                        if case == 0:

                            travel_date = input("Please enter your desired date of travel (dd/mm/yyyy):")
                            travel_date = datetime.strptime(travel_date, '%d/%m/%Y')
                            if travel_date < datetime.today():
                                print("Date cannot be in the past")
                                continue

                            case = 1

                        if case == 1:
                            number_of_passengers = int(input("Please enter the number of passengers:"))
                            if len(self._rail_passes) < 1:
                                print("No Rail Passes left!")

                            else:
                                print(*self.filter_rail_passes(travel_date, number_of_passengers), sep="\n")

                            case = 2  # now next step is to buy a certain ticket from the displayed ones
                            continue

                        if case == 2:  # this case to ask the user to buy a ticket
                            rail_pass_id = int(input("Please enter the rail pass id you want to buy:"))
                            # check if that ticket already belongs to the user who is currently logged in
                            new_rail_passes = list([rp for rp in self.get_current_user().get_rail_passes() if
                                                    rp.get_id() == rail_pass_id])
                            if len(new_rail_passes) != 0:  # he has already this ticket in his list
                                print("You can not buy this ticket as you have it already.")
                                continue
                            else:
                                # this means this rail pass can be added now find the details from the list
                                # of tickets # tickets now are loaded with its db file
                                rail_pass_to_add = list([rp for rp in self.get_rail_passes() if
                                                         rp.get_id() == rail_pass_id])
                                if len(rail_pass_to_add) != 0:  # we found the ticket
                                    # check its price and if the user has enough balance
                                    rp_to_check = rail_pass_to_add[0]
                                    if self.get_current_user().can_buy(rp_to_check):
                                        # ticket is appended and money deducted
                                        self.get_current_user().buy_rail_pass( rp_to_check)
                                        # ticket need to be popped from the seller
                                        # get the owner object and pop the ticket out
                                        owner = list(
                                            filter(lambda owner_obj: owner_obj.get_person_id() == rp_to_check.get_owner_id(),
                                                   self.get_clients()))[0]
                                        owner.sell_rail_pass(rp_to_check)
                                        print("The ticket is added to your account successfully.")
                                        break
                                    else:
                                        print("You don't have enough balance in your account.")
                                        break
                                else:
                                    print("This ticket is not found in our database.")
                                    break

                    except (ValueError, TypeError):
                        print("Please check your entered data and try again!")
                        continue
                break

        self.close()

    """
    Generates a random UUID
    """

    def generate_id(self):
        return uuid4()

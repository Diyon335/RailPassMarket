from Files import file_parser
from uuid import uuid4
from datetime import datetime, timedelta
from Classes.rail_pass import RailPass
from Classes.person import Person
from Classes.helpers import RailPassLevel


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
            lambda rail_pass: rail_pass.get_issue_date() < travel_date < rail_pass.get_issue_date() + timedelta(
                days=365) and number_of_passengers <= rail_pass.get_rides_left() and self.get_current_user().get_person_id() != rail_pass.get_owner_id(),
            self._rail_passes))

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
        while True:
            prompt = input(
                "\nSelect an option:\nBuy a railpass\nView my railpasses\nView balance\nRegister a railpass\nDelete a railpass\nLogout\n --> ")


            if "buy" in prompt.lower():

                case = 0
                travel_date = ""

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

                            number_of_passengers = int(input("Please enter the number of required rides:"))

                            if len(self._rail_passes) < 1:
                                print("No Rail Passes left!")

                            else:

                                rail_passes_found = self.filter_rail_passes(travel_date, number_of_passengers)

                                if len(rail_passes_found) >= 1:

                                    for t in rail_passes_found:
                                        print(t.get_display_string())

                                else:
                                    print("No Rail Passes found as per your conditions.")
                                    case = 0
                                    break

                            case = 2
                            continue

                        if case == 2:
                            rail_pass_id = input("Please enter the rail pass id you want to buy. Type quit to cancel:")

                            if "quit" in rail_pass_id.lower():
                                print("Cancelled buying")
                                break
                            else:
                                rail_pass_id = int(rail_pass_id)

                            # Check if that ticket already belongs to the user who is currently logged in
                            new_rail_passes = list([rp for rp in self.get_current_user().get_rail_passes() if
                                                    rp.get_id() == rail_pass_id])

                            if len(new_rail_passes) != 0:  # He has already this ticket in his list
                                print("You can not buy this ticket as you have it already.")
                                continue

                            else:

                                rail_pass_to_add = list([rp for rp in self.get_rail_passes() if
                                                         rp.get_id() == rail_pass_id])

                                if len(rail_pass_to_add) != 0:
                                    # Check its price and if the user has enough balance
                                    rp_to_check = rail_pass_to_add[0]

                                    if self.get_current_user().can_buy(rp_to_check):

                                        self.get_current_user().buy_rail_pass(rp_to_check)

                                        # Remove from owner's list of rail passes
                                        owner = list(
                                            filter(lambda owner_obj: owner_obj.get_person_id() == rp_to_check.get_owner_id(), self.get_clients()))[0]

                                        owner.sell_rail_pass(rp_to_check)
                                        rp_to_check.set_owner_id(self.get_current_user().get_person_id())
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
                continue

            elif "view" or "railpasses" in prompt.lower():
                print("Your rail passes:")
                for rail_pass in self._client.get_rail_passes():
                    print(rail_pass.get_display_string())

            elif "balance" in prompt.lower():
                print("Your balance:")
                print(self._client.get_bank_balance())

            elif "register" in prompt.lower():

                case = 0
                rail_pass_level = ""
                rides_left = ""
                rail_pass_id = ""
                issue_date = ""

                while True:

                    try:
                        if case == 0:

                            rail_pass_id = input("Please enter the ID of your railpass. (12 digit number; top right corner): ")
                            if len(rail_pass_id) != 12:
                                print("You did not enter a 12 digit number, try again.")
                                continue

                            case = 1

                        if case == 1:
                            rail_pass_level = int(input("What level is your railpass?\nVIP (enter 1)\nRegular (enter 2)\n --> "))
                            if rail_pass_level != 1 and rail_pass_level != 2:
                                print("You must enter 1 or 2")
                                continue

                            case = 2

                        if case == 2:
                            issue_date = input("What date (dd/mm/yyyy) was the railpass issued?\n --> ")
                            issue_date_to_check = datetime.strptime(issue_date, '%d/%m/%Y')
                            if issue_date_to_check > datetime.today():
                                print("The issue date you entered is in the future, please reconsider.")
                                continue
                            elif issue_date_to_check < datetime.today() + timedelta(days=-365):
                                print("Your railpass has expired and can not be registered.")
                                continue
                            elif  issue_date_to_check < datetime.today() + timedelta(days=-345):
                                print("Your railpass has less than 20 days remaining and can not be registered.")
                                continue

                            case = 3

                        if case == 3:
                            rides_left = int(input("How many valid rides are left on the railpass?\n --> "))
                            if rides_left < 1 or rides_left > 10:
                                print("The number of valid rides left can range from 1 till 10.")
                                continue

                            break

                    # When an error is caught, it continues the while statement until the last case
                    except (ValueError, TypeError):
                        print("Please check your entered data and try again!")
                        continue

                print(f"Your railpass with id {rail_pass_id} is registered!")
                user = self.get_current_user()
                owner_id = user.get_person_id()
                rp = RailPass(RailPassLevel(rail_pass_level).name, rides_left, rail_pass_id, owner_id, issue_date)
                self.add_rail_pass(rp)
                user.add_rail_pass(rp)
                continue

            elif "delete" in prompt.lower():

                print("Your rail passes:")

                for p in self._client.get_rail_passes():
                    print(p.get_display_string())

                while True:

                    try:

                        id_to_delete = input("Please enter the rail pass id you want to delete. Type quit to cancel:")

                        if "quit" in id_to_delete.lower():
                            print("Cancelled deleting any tickets")
                            break
                        else:
                            id_to_delete = int(id_to_delete)

                        ids = [rp.get_id() for rp in self._rail_passes]

                        if id_to_delete not in ids:
                            print("Invalid ID. Check and try again")
                            continue

                        self._client.delete_rail_pass(id_to_delete)

                        # Delete tickets from database
                        new_rail_passes = [rp for rp in self._rail_passes if rp.get_id() != id_to_delete]
                        self._rail_passes = list(new_rail_passes)
                        print(f"Rail pass with id {id_to_delete} has been deleted")

                    except (ValueError, TypeError):
                        print("Please check your entered data and try again!")
                    continue

            elif "logout" in prompt.lower():
                self.close()
                break

    """
    Generates a random UUID
    """

    def generate_id(self):
        return uuid4()

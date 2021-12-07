"""
RAIL PASS TRADER

authors: Dirk Peeters, Rasha Ali, George Paul, Diyon Wickrameratne

"""

from Classes.person import Person
from rail_pass_system import RailPassSystem
from Classes.helpers import invalid_string, valid_email
from datetime import datetime

"""
Main method that runs the program
"""


def main():
    testing = True

    if testing:

        s = RailPassSystem()

        prompt = input("Welcome! Would you like to login or sign up?")

        # TODO Implement log in. Check against the list of clients in the system. Check if they exist, and if pass is correct
        if "login" in prompt:

            # Assuming login successful

            prompt = input("Would you like to buy or sell?")

            if "sell" in prompt:
                pass # Not implemented yet
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
                            break

                    except (ValueError, TypeError):
                        print("Please check your entered data and try again!")
                        continue

                print(*s.filter_rail_passes(travel_date, number_of_passengers), sep="\n")


        # We can change these if statements
        elif "sign up" in prompt:

            # Continuous prompt to help the user sign up
            case = 0
            first_name, last_name, email, password = "", "", "", ""
            telephone, balance = 0, 0

            # My version of a python switch statement
            while True:

                try:
                    if case == 0:
                        first_name = str(input("Please enter your first name: "))

                        if invalid_string(first_name):
                            raise ValueError

                        case = 1
                        continue

                    if case == 1:
                        last_name = str(input("Please enter your last name: "))

                        if invalid_string(last_name):
                            raise ValueError

                        case = 2
                        continue

                    if case == 2:
                        email = str(input("Please enter your email: "))

                        if not valid_email(email):
                            raise ValueError

                        case = 3
                        continue

                    if case == 3:
                        password = str(input("Please enter a password. You cannot use \":\" in your password: "))

                        if ":" in password:
                            raise ValueError

                        case = 4
                        continue

                    if case == 4:
                        telephone = int(input("Please enter your telephone number: "))

                        if len(str(telephone)) != 10:
                            raise ValueError

                        case = 5
                        continue

                    if case == 5:
                        balance = int(input("Please enter your bank balance: "))

                        if balance < 0:
                            raise ValueError

                        break

                # When an error is caught, it continues the while statement until the last case
                except (ValueError, TypeError):
                    print("Please check your entered data and try again!")
                    continue

            print(f"Welcome {first_name}!")
            s.add_client(Person(first_name, last_name, email, password, telephone, balance, s.generate_id()))

            s.run()

        else:
            print("Goodbye")
            s.close()

    else:
        pass


if __name__ == '__main__':
    main()

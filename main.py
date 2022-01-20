"""
RAIL PASS TRADER

authors: Dirk Peeters, Rasha Ali, George Paul, Diyon Wickrameratne

"""
from Classes.person import Person
from rail_pass_system import RailPassSystem
from Classes.helpers import invalid_string, valid_email

"""
Main method that runs the program
"""


def main():

    while True:

        s = RailPassSystem()

        prompt = input("Welcome! Would you like to login or sign up? Type quit to exit\n --> ")

        if "login" in prompt:

            email = input("Please enter your email: ")
            password = input("Please enter your password: ")
            if not s.client_exists(email, password):
                print("Incorrect login details. Please check your entered details and try again!")
                s.close()
                continue

            user = s.get_client(email, password)
            print("Welcome "+user.get_first_name()+"!")
            s.set_current_user(user)

            s.run()
        elif "sign up" in prompt:

             # Continuous prompt to help the user sign up
            case = 0
            first_name, last_name, email, password = "", "", "", ""
            telephone, balance = 0, 0

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

                        if s.client_exists(email):
                            print("You already have an account. Please restart and login!")
                            quit()

                        case = 3
                        continue

                    if case == 3:
                        password = str(input("Please enter a password. You cannot use \":\" in your password: "))

                        if ":" in password:
                            raise ValueError

                        case = 4
                        continue

                    if case == 4:
                        telephone = int(input("Please enter your telephone number (must be 11 digits): "))

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
            p = Person(first_name, last_name, email, password, telephone, balance, s.generate_id())
            s.add_client(p)
            s.set_current_user(p)

            s.run()

        elif "quit" in prompt:
            break

        else:
            print("We didn't recognise that, would you like to login or sign up?")


if __name__ == '__main__':
    main()

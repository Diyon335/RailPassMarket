from Classes.rail_pass import RailPass
"""
Class for a Person
"""


class Person:

    """
    Constructor for the Person class
    """

    def __init__(self, first_name, last_name, email_address, password, telephone, bank_balance, person_id):
        try:
            self._last_name = last_name
            self._person_id = int(person_id)  # it should be incremented by 1
            self._first_name = first_name
            self._email_address = email_address
            self._password = password
            self._telephone = telephone
            self._bank_balance = int(bank_balance)
            self._rail_passes = []  # list of rail passes owned by person

        except TypeError as e:
            print("Incorrect type entered")
            print(e)


    """
    Gets person id 
    """
    def get_person_id(self):
        return self._person_id

    """
    Gets the email of the person
    """
    def get_email(self):
        return self._email_address

    """
    Gets the password of the person
    """
    def get_password(self):
        return self._password

    """
    Gets first name of client
    """
    def get_first_name(self):
        return self._first_name

    """
    Adds a single rail pass for the person
    """
    def add_rail_pass(self, rail_pass):
        self._rail_passes.append(rail_pass)

    """
    Returns a boolean indicating if the person can buy a rail pass or not
    """

    def can_buy(self, rail_pass):
        return self._bank_balance >= rail_pass.get_cost()

    """
    Adds money to a person's bank account after selling a rail pass
    """

    def deposit_money(self, amount):
        self._bank_balance += amount

    """
    Subtracts money from a person's account after buying a rail pass
    """

    def deduct_money(self, amount):
        self._bank_balance -= amount

    """
    Sells a person's rail pass
    """

    def sell_rail_pass(self, rail_pass):
        # we will return only items with ids that are not equal to the input ticket id
        new_rail_passes = [rp for rp in self._rail_passes if rp.get_id() != rail_pass.get_id()]
        self._rail_passes = list(new_rail_passes)  # deep copy of the list

    """
    Allows a person to buy a ticket if they have sufficient balance
    """

    def buy_rail_pass(self, rail_pass):
        # push this ticket to the array
        if self.can_buy(rail_pass):
            self.deduct_money(rail_pass.get_cost())
            self._rail_passes.append(rail_pass)
        else:
            print("You do not have enough money to buy this Rail Pass")

    """
    Gets the rail passes of the person
    """
    def get_rail_passes(self):
        return self._rail_passes

    """
    Loads all of the person's rail passes from the database
    """
    def load_rail_passes(self, rail_pass_list):
        for rp in rail_pass_list:
            string = rp.split(":")
            self._rail_passes.append(RailPass(string[0], string[1], string[2], string[3], string[4], string[5]))

    """
    The default toString method of the Person object
    """

    def __str__(self):
        return f"{self._first_name}:{self._last_name}:{self._email_address}:{self._password}:{self._telephone}:{self._bank_balance}:{self._person_id}"

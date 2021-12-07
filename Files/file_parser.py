from Classes.person import Person
from Classes.rail_pass import RailPass
from Classes.helpers import enum_to_level

clients = "Databases/client_database.txt"
rail_passes = "Databases/ticket_database.txt"

"""
Parses each line from the database of clients
"""


def parse_clients():
    people = []
    with open(clients, "r") as file:
        for line in file:
            string = line.strip().split(":")
            people.append(Person(string[0], string[1], string[2], string[3], string[4], string[5], string[6]))

    return people


"""
Parses each line from the database of rail passes
"""


def parse_rail_passes():
    passes = []
    with open(rail_passes, "r") as file:
        for line in file:
            string = line.strip().split(":")
            passes.append(RailPass(string[0], enum_to_level(string[1]), string[2], string[3], string[4], string[5]))

    return passes


"""
Writes clients from the system to the database
"""


def write_clients(people):
    data = ""
    for client in people:
        data += str(client)+"\n"

    with open(clients, "w") as file:
        file.write(data)


"""
Writes rail passes from the system to the database
"""


def write_rail_passes(passes):
    data = ""
    for rp in passes:
        data += str(rp) + "\n"

    with open(rail_passes, "w") as file:
        file.write(data)

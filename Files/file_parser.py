from Classes.person import Person
from Classes.rail_pass import RailPass
import json

clients = "Databases/client_database.txt"
rail_passes = "Databases/ticket_database.txt"

"""
Parses each line from the database of clients, and gets all rail passes
"""


def parse_clients_and_passes():

    people = []
    all_rail_passes = []

    try:
        with open(clients, "r") as file:
            # Load the dictionary
            people_dict = json.loads(file.read())

    # In the case of an empty file
    except json.JSONDecodeError:
        print("Returned this shit")
        return people, all_rail_passes

    for person in people_dict:
        # Split the key aka Person to create a person object
        string = person.strip().split(":")

        # Add person to system
        p = Person(string[0], string[1], string[2], string[3], string[4], string[5], string[6])
        people.append(p)

        # Add their list of rail passes to their object (the value of the dict.)
        p.load_rail_passes(people_dict[person])

        rps = []
        for rp in people_dict[person]:
            string = rp.split(":")
            rps.append(RailPass(string[0], string[1], string[2], string[3], string[4], string[5]))

        # Add their share of rail passes to all the tickets in the system
        all_rail_passes.extend(rps)

    return people, all_rail_passes


"""
Writes clients from the system to the database
"""


def write_clients(people):
    data = {}
    for client in people:

        rps = []
        for rp in client.get_rail_passes():
            rps.append(str(rp))

        data[str(client)] = rps

    with open(clients, "w") as file:
        file.write(json.dumps(data))


"""
Writes rail passes from the system to the database
"""


def write_rail_passes(passes):
    data = ""
    for rp in passes:
        data += str(rp) + "\n"

    with open(rail_passes, "w") as file:
        file.write(data)

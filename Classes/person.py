
from Classes.RailPass import Component, RailPass

#This class person can be a buyer or a seller in the system and methods related ..
class Person(Component):
    def __init__(self,name,description,person_id,last_name,first_name,email_address,password,telephone,bank_account):
        Component.__init__(self,name,description)
        self._last_name=last_name
        self._person_id=person_id  # it should be incremented by 1
        self._first_name=first_name
        self._email_address=email_address
        self._password=password
        self._telephone=telephone
        self._bank_account = bank_account
        self._tickets = [] #list of tickets owned by that personI had another though and for me no sense two maintain two lists

    def __str__(self):
        return 'Name of the user = ' + self._last_name + ', list of tickets ids this user has now : '+ str([t.get_ticket_id() for t in self._tickets ])
    
    def sell_ticket(self, ticket): # pop this ticket out of the array
        # we will return only items with ids that are not equal to the input ticket id 
        new_tickes_list = [t for t in self._tickets if t.get_ticket_id() != ticket.get_ticket_id()]
        if len(new_tickes_list) != 0:
            self._tickets = list(new_tickes_list) #deep copy of the list

    def buy_ticket(self,ticket) : #push this ticket to the array
        self._tickets.append(ticket)
    

# this is just was for testing to be removed later
person = Person('name','description',0,'Tom ','first_name','email_address@gmail.com','password',12345678,12345678)
rail1 = RailPass('name','description',10,1,2,5,1,0 ,False ,'2021-07-04 18:38:09.710949' , '2021-12-04 18:38:09.710949',False)
rail2 = RailPass('name','description',10,1,2,5,2,0 ,False ,'2021-07-04 18:38:09.710949' , '2021-12-04 18:38:09.710949', False)
rail3 = RailPass('name','description',10,1,2,5,3,0 ,False ,'2021-07-04 18:38:09.710949' , '2021-12-04 18:38:09.710949' , False)
person.buy_ticket(rail1)
print(rail1)
print(rail2)
print(rail3)
person.buy_ticket(rail2)
person.buy_ticket(rail3)
person.sell_ticket(rail1)
print(person)


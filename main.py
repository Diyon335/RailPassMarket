from Classes.RailPass import RailPass
from Classes.person import Person


def main():
    #testing
    person = Person('name','description',0,'lastName','first_name','email_address@gmail.com','password',12345678,12345678)
    rail = RailPass('name','description',10,1,2,5,1,0 ,False ,'2021-07-04 18:38:09.710949' , '2021-12-04 18:38:09.710949')

    person.buy_ticket(rail)
    print(person)

if __name__ == '__main__':
    main()
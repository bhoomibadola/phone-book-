class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"{self.name} {self.phone_number}"

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("No contact found")
        else:
            print("all contacts in directory")
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone_number
        return f"{search_name} not found"

    @staticmethod
    def validate_phone_number(number):
        return len(number) >= 8 and number.isdigit()


n_contact = int(input("how many contacts do you want to add?: "))
for i in range(n_contact):
    name = input("what is your name?: ")
    phone_number = input("what is your phone number?: ")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)
    else:
        print(f"{name} is not a valid phone number")

Contact.show_all_contact()
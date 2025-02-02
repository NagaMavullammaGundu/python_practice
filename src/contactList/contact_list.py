# add a contact

import argparse


class Contact:

    def __init__(self, name, number, email, address):
        """Constructor"""
        self.name = name
        self.number = number
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} and his number is {self.number} and he lives in {self.address}"


def write_file(contact_list):
    """Writing contacts to the file"""
    file = open(
        "contactlist.txt",
        "a",
    )
    for contact in contact_list:
        file.write(
            f"{contact.name},{contact.number},{contact.email},{contact.address}\n"
        )
    file.close()


def read_file():
    """Reading content in the file"""
    file = open("contactlist.txt", "r")
    contacts = file.readlines()
    contacts = [contact.strip() for contact in contacts]
    file.close()

    contact_list = []
    for contact in contacts:
        contact_name, contact_number, contact_email, contact_address = contact.split(
            ","
        )
        contact_object = Contact(
            contact_name, contact_number, contact_email, contact_address
        )
        contact_list.append(contact_object)
    return contact_list


def add(contact_name, contact_number, contact_email, contact_address):
    new_contact = Contact(contact_name, contact_number, contact_email, contact_address)
    write_file([new_contact])


def view():
    """Displaying the contacts in file"""
    list_of_contacts = read_file()
    for contact in list_of_contacts:
        print(contact)


def search():
    pass


def update():
    pass


def delete():
    pass


def main():
    parser = argparse.ArgumentParser(description="Contact List")

    parser.add_argument(
        "--contact_name", type=str, required=True, help="Name of the Person"
    )
    parser.add_argument(
        "--contact_number", type=int, required=True, help="Number of the Person"
    )
    parser.add_argument(
        "--contact_email", type=str, required=False, help="Email of the Person"
    )
    parser.add_argument(
        "--contact_address", type=str, required=False, help="Address of the Person"
    )

    args = parser.parse_args()

    add(
        args.contact_name, args.contact_number, args.contact_email, args.contact_address
    )
    view()
    read_file()


if __name__ == "__main__":
    main()

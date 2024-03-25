#niezbędne biblioteki
import os
import csv
import re
from collections import UserDict

#klasy
class AddressBook(UserDict):
    ab_id = 1
    contacts_book = {}

    def __init__(self):
        self.id=AddressBook.ab_id
        AddressBook.ab_id += 1

class Record():
    def __init__(self):
        super().__init__()
        self.personal_details = None
        self.contact_data = None
        self.favorite = False

class PersonalDetails(Record):
    def __init__(self, name="empty", lastname="empty"):
        super().__init__()
        self.name = name
        self.lastname = lastname

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Podanie imienia jest obowiązkowe")
        elif not isinstance(value, str) or len(value) < 3:
            raise ValueError("Imię składa się z liter. Minimalna liczba liter: 3.")
        self._name = value

    @property
    def lastname(self):
        return self._lastname
    @lastname.setter
    def lastname(self, value):
        if not value:
            raise ValueError("Podanie nazwiska jest obowiązkowe")
        elif not isinstance(value, str) or len(value) < 2:
            raise ValueError("Nazwisko składa się z liter. Minimalna liczba liter: 2.")
        self._lastname = value

class ContactData:
    def __init__(self,  phone=None, email=None):
        self.phone = phone
        self.email = email

    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, value):
        if not value:
            value = ""
        elif not isinstance(value, str) or not value.isdigit() or len(value) != 9:
            raise ValueError("Numer telefonu ma 9 cyfr.")
        self._phone = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if not value:
            value = ""
        elif not re.match(r"[\w.-]+@{1}[a-zA-Z0-9]+\.[a-zA-Z]{2,3}\b", value):
            raise ValueError('Adres mailowy składa się z identyﬁkatora użytkownika, znaku "@" i domeny (przykład: jan.nowak@domena.pl).')
        self._email = value

#funkcje
def load_file():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"my_addressbook.csv")
    if os.path.exists(file_path):
        with open(file_path, "r", newline = "") as tempfile:
            reader = csv.reader(tempfile)
            next(reader)
            max_id = 0
            for row in reader:
                id, name, lastname, phone, email, favorite = row
                max_id = max(max_id, int(id))
                personal_details = PersonalDetails(name, lastname)
                contact_data = ContactData(phone, email)
                new_contact = Record()
                new_contact.id = id
                new_contact.personal_details = personal_details
                new_contact.contact_data = contact_data
                new_contact.favorite = favorite.lower() == "true"
                AddressBook.contacts_book[int(id)] = new_contact
            AddressBook.ab_id = max_id + 1

def help_me():
    all_commands = ", ".join(available_commands.keys())
    print(f"Dostępne komendy wyglądają następująco: {all_commands}.")

def hello_there():
    print("Witaj, jak mogę Ci pomóc?")

def add_contact():
    print(f"Dodajesz nowy kontakt")
    personal_details = PersonalDetails()
    contact_data = ContactData()
    while True:
        try:
            nc_name = input(f"Wprowadź imię: ").lower()
            personal_details.name = nc_name
            break
        except ValueError as e:
            print("UWAGA: ", str(e))
            continue

    while True:
        try:
            nc_lastname = input(f"Wprowadź nazwisko: ").lower()
            personal_details.lastname = nc_lastname
            break
        except ValueError as e:
            print("UWAGA: ", str(e))
            continue
    
    while True:
        try:
            nc_phone = input(f"Wprowadź numer telefonu: ")
            contact_data.phone = nc_phone
            break
        except ValueError as e:
            print("UWAGA: ", str(e))
            continue

    while True:
        try:
            nc_email = input(f"Wprowadź adres mailowy: ").lower()
            contact_data.email = nc_email
            break
        except ValueError as e:
            print("UWAGA: ", str(e))
            continue

    nc_favorite = input(f"Chcesz dodać kontakt do ulubionych? (tak/nie): ")
    if nc_favorite.lower() == "tak":
        nc_favorite = True
    else:
        nc_favorite = False
    nc_id = AddressBook.ab_id
    personal_details = PersonalDetails(nc_name, nc_lastname)
    contact_data = ContactData(nc_phone, nc_email)

    new_contact = Record()
    new_contact.id = nc_id
    new_contact.personal_details = personal_details
    new_contact.contact_data = contact_data
    new_contact.favorite = nc_favorite

    AddressBook.contacts_book[nc_id] = new_contact
    AddressBook.ab_id += 1
    print(f"Dodanie kontaktu {nc_id} zakończone sukcesem")

def choice_change_contact():
    change_person = input("Podaj dane kontaktu, który chcesz zmienić: ").lower()
    persons_to_change = []
    
    for contact_id, contact in AddressBook.contacts_book.items():
        if change_person in contact.personal_details.name.lower() or change_person in contact.personal_details.lastname.lower() or change_person == contact.contact_data.phone or change_person == contact.contact_data.email:
            persons_to_change.append((contact_id, contact))
    
    if len(persons_to_change) == 0:
        print("Nie znaleziono kontaktu.")
        return
        
    if len(persons_to_change) == 1:
        contact_id, contact = persons_to_change[0]
        changed_contact = AddressBook.contacts_book.get(int(contact_id))
    
    else:
        print("Znalenziono kilka kontaktów:")
        for contact_id, contact in persons_to_change:
            print(contact_id, contact.personal_details.name.title(), contact.personal_details.lastname.title(), contact.contact_data.phone, contact.contact_data.email, contact.favorite)
        
        while True:
            change_person_id = input("Podaj ID kontaktu, który chcesz zmienić: ")
            changed_contact = AddressBook.contacts_book.get(int(change_person_id))
            if changed_contact:
                break
            else:
                print("Nie znaleziono kontaktu o podanym ID.")
       
    while True:    
        choice = input("Wskaż co chcesz zrobić: Dodać dane kontaktowe (1), Zmodyfikować zapisane dane (2): ").lower()
        if choice == "1" or choice == "d":
            add_new_contacts_data(changed_contact)
            break
        elif choice == "2" or choice == "z":
            change_contact(changed_contact)
            break
        else:
            print("Wybierz opcję 1 lub opcję 2")

def add_new_contacts_data(changed_contact):
    print("Dodajesz adres mailowy")
    while True:
        extra_mail = input("Podaj adres mailowy: ")
        try:
            contact_data = ContactData(email=extra_mail)
            changed_contact.contact_data.email += ", " + extra_mail
            break
        except ValueError as e:
            print(f"UWAGA: {str(e)}")

def change_contact(changed_contact):
    possibility = {
        "1": ("name", "Podaj nowe imię: "),
        "2": ("lastname", "Podaj nowe nazwisko: "),
        "3": ("phone", "Podaj nowy numer telefonu: "),
        "4": ("email", "Podaj nowy adres e-mail: "),
        "5": ("favorite", "Czy chcesz oznaczyć kontakt jako ulubiony? (tak/nie): ")
    }
    print("Wybierz daną którą chcesz zmienić:")
    for key, (possibility_choice, possibility_message) in possibility.items():
        print(f"{key}. {possibility_message}")
    
    while True:
        choice = input("Wybierz numer opcji: ")
        if choice in possibility:
            break
        else:
            print("Niepoprawna opcja. Wybierz numer od 1 do 5")
           
    if choice in possibility:
        possibility_choice, _ = possibility[choice]
        while True:
            try:
                new_value = input(possibility[choice][1])
                if possibility_choice == "name":
                    changed_contact.personal_details.name = new_value
                elif possibility_choice == "lastname":
                    changed_contact.personal_details.lastname = new_value
                elif possibility_choice == "phone":
                    changed_contact.contact_data.phone = new_value
                elif possibility_choice == "email":
                    changed_contact.contact_data.email = new_value
                elif possibility_choice == "favorite":
                    if new_value.lower() == "tak":
                        changed_contact.favorite = True
                    elif new_value.lower() == "nie":
                        changed_contact.favorite = False
                    else:
                        raise ValueError("Odpowiedz 'tak' lub 'nie'.")
                break
            except ValueError as e:
                print(f"UWAGA: {str(e)}")
                continue

    
    if possibility_choice != "favorite":
        setattr(changed_contact.personal_details, possibility_choice, new_value)
        setattr(changed_contact.contact_data, possibility_choice, new_value)

    for key, contact in AddressBook.contacts_book.items():
        if contact == changed_contact:
            if possibility_choice == "favorite":
                AddressBook.contacts_book[key].favorite = changed_contact.favorite
            else:
                setattr(AddressBook.contacts_book[key].personal_details, possibility_choice, new_value)
                setattr(AddressBook.contacts_book[key].contact_data, possibility_choice, new_value)
            print("Dane zmieniono pomyślnie.")
            break

def remove_contact():
    remove_person = input("Podaj dane kontaktu, który chcesz usunąć: ")
    persons_to_remove = []
    for contact_id, contact in AddressBook.contacts_book.items():
        if remove_person in contact.personal_details.name.lower() or remove_person in contact.personal_details.lastname.lower() or remove_person == contact.contact_data.phone or remove_person == contact.contact_data.email:
            persons_to_remove.append((contact_id, contact))
    
    if persons_to_remove:
        if len(persons_to_remove) == 1:
            contact_id, removed_contact = persons_to_remove[0]
            del AddressBook.contacts_book[contact_id]
            print(f"Usunięto kontakt {contact_id}: {removed_contact.personal_details.name.title()} {removed_contact.personal_details.lastname.title()}")

        else:
            print("Znaleziono kilka kontaków.")
            for contact_id, contact in persons_to_remove:
                print(contact_id, contact.personal_details.name.title(), contact.personal_details.lastname.title(), contact.contact_data.phone, contact.contact_data.email, contact.favorite)
            remove_person_ID = input("Podaj ID kontaktu, który chcesz usunąć: ")
            if remove_person_ID in AddressBook.contacts_book:
                removed_contact = AddressBook.contacts_book.pop(remove_person_ID)
                print(f"Usunięto kontakt {remove_person_ID}: {removed_contact.personal_details.name.title()} {removed_contact.personal_details.lastname.title()}")
            else:
                print("Podany kontakt nie istnieje.")

def find_contact():
    seek_person = input("Wpisz dane osoby, którą chcesz znaleźć: ")
    found_persons = []
    for contact_id, contact in AddressBook.contacts_book.items():
        if seek_person in contact.personal_details.name.lower() or seek_person in contact.personal_details.lastname.lower() or seek_person == contact.contact_data.phone or seek_person == contact.contact_data.email:
            found_persons.append((contact_id, contact))
    
    if found_persons:
        print("Znaleziono kontakty:")
        for contact_id, contact in found_persons:
            print(contact_id, contact.personal_details.name.title(), contact.personal_details.lastname.title(), contact.contact_data.phone, contact.contact_data.email, contact.favorite)
    else:
        print("Nie znaleniono żandego kontaktu.")

def show_all_contacts():
    print(f"ID NAME LASTNAME PHONE EMAIL FAV")
    for contact_id, contact in AddressBook.contacts_book.items():
        print(contact_id, contact.personal_details.name.title(), contact.personal_details.lastname.title(), contact.contact_data.phone, contact.contact_data.email, contact.favorite)
    
def quit_program():
    print("Zamykanie Asystenta bez zapisywania kontaktów.")
    return True

def exit_program():
    print("Zapisywanie książki adresowej...")
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"my_addressbook.csv")
    file_exists = os.path.exists(file_path)
    contacts_book = AddressBook.contacts_book
    
    with open(file_path, "w", newline = "") as tempfile:
        writer = csv.DictWriter(tempfile, fieldnames = ("id", "name", "lastname", "phone", "email", "favorite"))
        if not file_exists:
            writer.writeheader()
        if contacts_book:
            writer.writeheader()
            for contact_id, contact in contacts_book.items():
                rowdict = {
                    "id": contact.id, 
                    "name": contact.personal_details.name, 
                    "lastname": contact.personal_details.lastname, 
                    "phone": contact.contact_data.phone, 
                    "email": contact.contact_data.email, 
                    "favorite": contact.favorite
                }
                writer.writerow(rowdict)
            print("Zapisano nowe dane.")
        else:
            print("Brak nowych danych do zapisu.")
    print("Zamykanie Asystenta.")
    return True

available_commands = {
    "help": help_me,
    "hello": hello_there,
    "add": add_contact,
    "change": choice_change_contact,
    "remove": remove_contact,
    "show": show_all_contacts,
    "find": find_contact,
    "exit": exit_program,
    "quit": quit_program,
}

def main():
    while True:
        user_input = input(f"Podaj komendę: ").lower()
        user_command = user_input.split()
        if user_command[0] in available_commands:
            if available_commands[user_command[0]](*user_command[1:]):
                break
        else:
            print(f"Podana komenda nie istnieje. Spróbuj użyć 'help'.")

if __name__ == "__main__":
    load_file()
    main()
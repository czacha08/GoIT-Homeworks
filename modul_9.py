#
commands = ["help", "hello", "add", "delete", "show", "phone", "change", "exit",]
database = [{"martha": "100200300"}, {"bruce": "400500600"}, {"thomas": "700800900"}]

#dekorator obsługujący błędy:
def input_error(funkcja):
    def iner_function(*args, **kwargs):
        try:
            return funkcja(*args, **kwargs)
        except ValueError:
            print(f"Podaj imię lub imię i numer telefonu.")
        except KeyError:
            print(f"Podaj imię.")
        except IndexError:
            print(f"Nie znaleziono kontaktu.")
    return iner_function

#funkcje odpowadające za polecenia
def get_help():
    return f"Dostępne są następujące komendy: {', '.join(commands)}."

def hello():
    return "Witaj! Jestem Twoim asystenetem. Jak mogę Ci pomóc?"

def bye():
    return "Do zobaczenia"

@input_error
def add(full_command):
    command, name, phone= full_command.split(" ")
    person = {name: phone}
    database.append(person)
    return f"Asystent dodał kontakt: {name.capitalize()} z numerem telefonu {phone}."

def show():
    list = ""
    print(f"Oto lista kontaktów:")
    for person in database:
        for name, phone in person.items():
            list += (f"- {name.capitalize()}:\t {phone}\n")
    return list

@input_error
def change(full_command):
    command, name, new_phone = full_command.split(" ")
    for person in database:
        if name in person:
            person[name] = new_phone
            return f"Asystent zmienił numer kontaktu {name.capitalize()} na {new_phone}."
    return f"Asystent nie znalazł kontaktu {name.capitalize()} w bazie danych."

@input_error
def delete(full_command):
    command, name = full_command.split(" ")
    found = False
    for person in database[:]:
        if name in person:
            database.remove(person)
            found = True
            return f"Asystent usunął kontakt {name.capitalize()}."      
    if not found:
        return f"Asystent nie znalazł kontaktu {name.capitalize()}."

@input_error
def phone(full_command):
    command, seeking_name = full_command.split(" ")
    for person in database:
        for name, phone in person.items():
            if seeking_name in name:
                return f"Numer do {name.capitalize()} to {phone}."
    return f"Asysten nie znalazł kontaktu {seeking_name.capitalize()}"

def main():
    print(f"Witaj w Osobistym Asystencie. Wpisz help w celu uzyskania pomocy lub zacznij pracę.")
    while True:
        full_command  = input(f"Wpisz komendę: ").lower()
        command = full_command.split()[0]
        if command == "help":
            print(get_help())
        elif command == "hello":
            print(hello())
        elif command == "add":
            print(add(full_command))
        elif command == "show":
            print(show())
        elif command == "change":
            print(change(full_command))
        elif command == "delete":
            print(delete(full_command))
        elif command == "phone":
            print(phone(full_command))
        elif command == "exit":
            print(bye())
            break
        else:
            print("Nieznene polecenie")  


if __name__ == "__main__":
    main()
import datetime as dt
#zmienne
today = dt.datetime.now()
next_week = today + dt.timedelta(days=7)
current_year = today.year
birthday_people = []

#lista użytkowników
users = [
    {"Alayah": "1955-12-18"},
    {"Alysha": "1946-10-15"},
    {"Bert": "1954-08-16"},
    {"Blake": "1947-06-01"},
    {"Brenna": "1950-04-13"},
    {"Briana": "1982-02-06"},
    {"Briggs": "1998-11-14"},
    {"Bryant": "1945-09-11"},
    {"Claire": "1953-07-15"},
    {"Conor": "1958-05-25"},
    {"Dakota": "1992-03-18"},
    {"Dwight": "1998-01-30"},
    {"Earleen": "1945-12-09"},
    {"Fancy": "1956-10-22"},
    {"Felipe": "1959-08-12"},
    {"Fran": "2000-06-15"},
    {"Grace": "1968-04-22"},
    {"Graham": "1963-02-24"},
    {"Gyles": "1985-11-11"},
    {"Hamza": "1971-09-22"},
    {"Haylie": "1972-07-19"},
    {"Helen": "1974-05-18"},
    {"Hyram": "1999-03-02"},
    {"Ida": "1958-01-27"},
    {"Johnie": "1982-12-08"},
    {"Jolie": "1974-10-26"},
    {"Karrie": "1957-08-24"},
    {"Katherine": "1974-06-19"},
    {"Keira": "1974-04-02"},
    {"Kelsey": "1977-02-27"},
    {"Kendal": "1978-11-21"},
    {"Kimball": "1980-09-15"},
    {"Leandro": "1993-07-29"},
    {"Leila": "1970-05-03"},
    {"Lorainne": "1961-03-27"},
    {"Lucas": "1995-01-05"},
    {"Luvinia": "1958-12-12"},
    {"Marcus:": "1996-10-02"},
    {"Marnie": "1949-08-29"},
    {"Petunia": "1964-06-04"},
    {"Preston": "2006-04-15"},
    {"Rexanne": "1984-02-11"},
    {"Royce": "1990-11-08"},
    {"Stafford": "1961-09-30"},
    {"Summer": "2005-07-13"},
    {"Totty": "1974-05-01"},
    {"Tyla": "1948-03-24"},
    {"Tylor": "1952-01-18"},
    {"Vaughan": "1946-12-16"},
    {"Zelma": "1980-10-22"},
    {"Marcin": "1987-03-02"},
    {"Paweł": "1965-03-01"},
    {"Joanna": "1972-03-04"},
    {"Patrycja": "1995-02-28"},
]

days_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",]

#funkcje
def get_birthday_day(users):
    for user in users:
        for name, date in user.items():
            yr, mt, d = date.split("-")
            wishes = dt.datetime(year=int(current_year), month=int(mt), day=int(d))
            if today.date() <= wishes.date() <= next_week.date():
                weekday = wishes.weekday()
                birthday_dict = {name: weekday}
                birthday_people.append(birthday_dict)
                # print(f'jazdaa {name}, {wishes}, {birthday_dict}')
    # print(f"birthday_people = {birthday_people}")
    return (birthday_people)

def get_birthdays_per_week(birthday_people):
    result = {}
    # birthday_people = sorted(birthday_people, key=lambda item: item[name])
    for person in birthday_people:
        # print(birthday_people)
        for name, day in person.items():
            day_name = days_name[int(day)]
            result.setdefault(day_name, []).append(name)
    # print(result)
    for day, people in result.items():
        print(f"{day}: {', '.join(people)}")
                       

#wywołanie funkcji
get_birthday_day(users)
get_birthdays_per_week(birthday_people)
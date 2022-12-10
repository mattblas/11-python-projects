import datetime, re

def main():
    data = get_data()
    print_data(data[0], data[1], data[2], data[3])

 
def name_input():
    name = []
    while True:
        n = input("What is your name? ").lower()
        if n.strip().replace(" ", "").isalpha() and len(n.split()) > 1:
            break
        print ("invalid name")
    n = n.split()
    for i in n:
            temp_name = str(i).capitalize()
            name.append(temp_name)            
    return name


def date_input():
    while True:
        date = input("What is your date of birth? (YYYY-MM-DD) ")
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
    return date


def adress_input():
    adress = []
    while True:
        a = input("What is your adress? (no street, city) ")
        if use_regex(a):
            break
        print("Incorrect data format, should be (no street, city) ")
    a_split = a.split(" ")
    for i in a_split:
        try:
            i = str(i).capitalize()
            adress.append(i)
        except:
            adress.append(i)
    return adress


def use_regex(input_text):
    pattern = re.compile(r"[0-9]+\s[\w\s]+,\s[\w\s]+", re.IGNORECASE)
    return pattern.match(input_text)


def goals_input():
    return (input("What are your personal goals? "))


def get_data():
    name = name_input()
    date = date_input()
    adress = adress_input()
    goals = goals_input()
    return (name, date, adress, goals)


def print_data(name, date, adress, goals):
    print("")
    print(f"Name: ", end="")
    for i in name:
        print(f"{i}", end=" ")
    print("")
    print(f"Date of birth: {date}")
    print(f"Adress: ", end="")
    for i in adress:
        print(f"{i}", end=" ")
    print("")
    print(f"Personal goals: {goals}")   


if __name__ == "__main__":
    main()

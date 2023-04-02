from distributions import MyDataBase

db = MyDataBase()

user = input("Enter username ")
status = "start"
answer = ""


while True:

    if status == "start":

        if not db.user_exist(user):
            db.add_user(user)

        answer = input("You authorized. Enter your command ")
        status = "menu"

    elif status == "menu":

        if answer.lstrip()[:3] == 'add':

            if answer.strip()[3:]:
                db.add_element(user, answer.lstrip()[3:].strip())
                answer = input("Element added. Enter your command ")
            else:
                answer = input("Incorrect input. Enter command ")

        elif answer.lstrip()[:6] == 'remove':
            if answer.strip()[6:]:

                if db.find_element(user, answer.lstrip()[6:].strip()):
                    db.remove_element(user, answer.lstrip()[6:].strip())
                    answer = input("Element deleted. Enter your command ")
                else:
                    answer = input("Element doesnt exist. Enter your command ")
            else:
                answer = input("Incorrect input. Enter command ")

        elif answer.lstrip()[:4] == 'find':
            if answer.strip()[4:]:

                if db.find_element(user, answer.lstrip()[4:].strip()):
                    answer = input("Element was found. Enter your command ")
                else:
                    answer = input("Element doesnt find. Enter your command ")
            else:
                answer = input("Incorrect input. Enter command ")

        elif answer.lstrip()[:4] == 'grep':
            if answer.strip()[4:]:
                if db.grep_element(user, answer.lstrip()[4:].strip()):
                    i = 1

                    for element in db.grep_element(user, answer.lstrip()[4:].strip()):
                        print(f'{i}) {element}')
                        i += 1

                    answer = input("Enter your command ")

                else:
                    answer = input("No such elements. Enter your command ")
            else:
                answer = input("Incorrect input. Enter command ")

        elif answer.strip() == 'list':
            if db.list_element(user):
                i = 1

                for element in db.list_element(user):
                    print(f'{i}) {element}')
                    i += 1
                answer = input("Enter your command ")

            else:
                answer = input("List is empty. Enter command ")

        elif answer.strip() == 'save':

            if (db.list_element(user)):
                db.save_data()
                answer = input("Data was saved. Enter your command ")
            else:
                answer = input("Your storage is empty, nothing to save. Enter your command ")

        elif answer.strip() == 'load':
            with open("storage.json", "r") as file:
                if file.read():
                    if db.load_data(user):
                        answer = input("Data was loaded. Enter your command ")
                    else:
                        answer = input("Nothing to load. Enter your command ")
                else:
                    answer = input("Your file is empty, nothing to load. Enter your command ")

        elif answer.strip() == "switch":
            status = "switch"
            answer = input("Save in file?(Y/N) ")

        else:
            answer = input("Incorrect input. Enter command ")

    elif status == "switch":
        if answer.strip().lower() == "y" or answer.strip().lower() == "n":

            if answer.strip().lower() == "y":
                db.save_data()
                print("Data was saved")

            user = input("Enter new username ")
            status = "start"

        else:
            answer = input("Wrong imput. Save in file?(Y/N) ")
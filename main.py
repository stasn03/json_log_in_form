import json
def main():
    while True:
        print("1. Log in")
        print("2. Sign in")
        print("3. Display accounts")
        print("0. Exit")
        
        option= int(input("Introduce your option: "))

        match option:
            case 1:
                log_in()
            case 2:
                sign_in()
            case 3:
                display_acc()
            case 0:
                break


def import_acc():
    with open("accounts.json", "r") as json_file:
        acc_json= json.load(json_file)

    return acc_json


def check_acc(username):
    exist= False
    acc_json= import_acc()
    
    for acc in acc_json:
        if acc["username"] == username:
            exist= True

    if exist:
        return True
    else:
        return False


def log_in():

    username_input= input("Introduce your username: ")
    password_input= input("Introduce your password: ")

    acc_json= import_acc()
    for i in range(len(acc_json)):
        print(f"username: {acc_json[i]["username"]}")
        print(f"password: {acc_json[i]["password"]}")

def sign_in():
    acc_json= import_acc()
    account= {
        "username": input("Introduce your username: "),
        "password": input("Introduce your password: ")
    }

    acc_json.append(account)


    if not check_acc(account["username"]):
        with open("accounts.json", "w") as json_file:
            json.dump(acc_json, json_file)
    else:
        print("There is already an account with this username")
        acc_json.pop()


def display_acc():
    with open("accounts.json", "r") as json_file:
        accounts= json.load(json_file)

    print(accounts)


main()

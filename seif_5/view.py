from person import*
from model import*


class view():
    def get_user_input(self):

        name=input(" enter your full name ")
        addres=input("enter your adress ")
        phone=input("enter your phone number ")

        return name,addres,phone
    
    def show_people_list(self, people_list):
        print("\n--- Current People List ---")
        if not people_list:
            print("The list is empty.")
        else:
            for person in people_list:
                print(person)

    def display_menu(self):
        print("\n--- Menu ---")
        print("1. Add Person")
        print("2. Show All People")
        print("-1. Exit")
        return input("Choose an option: ")
    def display_message(self, message):
        print(f" >> {message}")




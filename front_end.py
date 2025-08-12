from models import session, Owners
from bp_appointments import create_appointment, view_appointments, reschedule_appointment, complete_appointment
from bp_auth import login, register_user
from bp_owner import view_profile, update_profile, delete_user
from bp_pets import view_pets, create_pet, update_pet, delete_pet


def welcome_menu():
    current_user = None
    while True:
        print("""
--------- Welcome to Pet Clinic --------
        1.) Login
        2.) Register
""")
        choice = input("select (1 or 2) or quit: ")
        if choice == '1':
            current_user = login()
            if current_user:
                return current_user

        elif choice == '2':

            current_user = register_user()
            if current_user:
                return current_user

        elif choice == 'quit':
            return
        else:
            print("Invalid response please try again.")

def owner_menu(current_user):
    while True:
        print("""
    1.) View Profile
    2.) Update Profile
    3.) Delete Profile
    4.) Back""")
        choice = input("choose 1-3: ")
        if choice == '1':
            view_profile(current_user)
        elif choice == '2':
            current_user = update_profile(current_user)
        elif choice == '3':
            is_deleted = delete_user(current_user)
            if is_deleted:
                current_user = None
                return current_user
        elif choice == '4':
            return
        else:
            print("Invalid Selection.")

def pets_menu(current_user):
    while True:
        print("""
1.) View my Pets
2.) Create Pet
3.) Update Pet
4.) Delete Pet
5.) Back""")
        choice = input("choose 1-5: ")
        if choice == '1':
            view_pets(current_user)
            
        elif choice == '2':
            create_pet(current_user)
            pass
        elif choice == '3':
            update_pet(current_user)
            pass
        elif choice == '4':
            delete_pet(current_user)
            pass
        elif choice == '5':
            return
        else:
            print("Invalid Selection.")

def appointments_menu(current_user):
    while True:
        print("""
1.) Schedule appointment
2.) View appointments
3.) Reschedule appointment
4.) Complete appointment
5.) Back
""")
        choice = input("choose 1-5: ")
        if choice == '1':
            create_appointment(current_user)
        elif choice == '2':
            view_appointments(current_user)
        elif choice == '3':
            reschedule_appointment(current_user)
        elif choice == '4':
            complete_appointment(current_user)
        elif choice =='5':
            return


def main():
    
    current_user = welcome_menu() 

    #After you test you login and register functions, it might be more efficient
    #to set current_user to a user in your db so you don't have to log in everytime
    #you want to test something.
    
    if current_user:
        while True and current_user:
            print("""
        --------- Pet Clinic --------
        1.) Manage Profile
        2.) My Pets
        3.) My Appointments
        """)
            choice = input("choose 1-3: ")
            if choice == '1':
                owner_menu(current_user)
            elif choice == '2':
                pets_menu(current_user)
            elif choice == '3':
                appointments_menu(current_user)
            else:
                print("Invalid Selection.")

        print("Thanks for stopping by!")
    

main()
    

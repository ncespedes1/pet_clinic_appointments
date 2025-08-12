from sqlalchemy.exc import IntegrityError
from models import Owners, session



def login():

#in class:

    print("----- Login -----")
    email = input("Email: ")
    password = input("Password: ")

    user = session.query(Owners).where(Owners.email==email).first()

    if user and user.password == password:
        print("Successfully logged in.")
        print(f"Welcome back {user.name}")
        return user
    else:
        print("Invalid username or password.")
        

#Login function
#get email and password from user
#check database for owner with the given email
#if you find an owner, check if the found owners password is the same as the given password
#if so return user



def register_user(**user_data):
    #in class: remove **user_data above
    print("----- Welcome! Please fill in the following to register. -----")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    phone = input("Phone: ")
    try:
        new_owner = Owners(name=name, email=email, password=password, phone=phone)
        session.add(new_owner)
        session.commit()
        print(f"Welcome {name}!")
        return new_owner
    except IntegrityError:
        print("This email is associated with another account.")
    except Exception as e:
        print("Issue creating this account")
        print(e)

    
#Register function
#get all info required to create an owner from the user
#try and create an Owner from the info (will fail if email is already in user)
#if you succeed return user
#except error and print message



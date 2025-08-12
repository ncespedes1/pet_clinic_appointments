from models import Owners, session

#View profile function
#displays the current users info

def view_profile(current_user):
    current_user.display()




#Update profile function
#displays current user info
#allows user to update any of the fields
#commits changes 
#shows changes and returns update current_user

def update_profile(current_user):

    view_profile(current_user)
    print("Please fill in any desired changes. Leave answers blank to keep current information.")
    name = input("Name: ")
    phone = input("Phone: ")
    password = input("Password: ")
    while True:
        email = input("Email: ")
        taken_user = session.query(Owners).where(Owners.email==email).first()
        if taken_user:
            print("This email is taken.")
            continue
        break

    if name:
        current_user.name = name
    if phone:
        current_user.phone = phone
    if password:
        current_user.password = password
    if email:
        current_user.email = email

    session.commit()
    print("Here are your new changes:")
    view_profile(current_user)
    return current_user



#Delete profile function
#Ask user to confirm they want to delete
#if so delete the current user from the session
#commits changes 

def delete_user(current_user):
    choice = input("Type 'delete' to confirm you wish to delete your account: ")
    if choice.lower() == 'delete':
        session.delete(current_user)
        session.commit()
        print("Successfully deleted account.")
        return True
    else:
        print("Opted out, back to menu.")
        return False
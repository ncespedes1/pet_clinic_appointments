from models import Pets, session

#view pets function
#Takes in current user
#Loops over all of the current users pets (use the .pets relationship attribute to get list of pets)
#prints the pets info

def view_pets(current_user):

    pet_list = current_user.pets

    print(f"--- {current_user.name}'s Pets ---")
    for pet in pet_list:
        print(f"\n --- Pet: {pet.id} ---")
        pet.display()


#Create pets function
#gets pets info from user
#create Pets() from the info
#print new pet


def create_pet(current_user):
   
    name = input("Pet Name: ")
    species = input("Species: ")
    breed = input("Breed: ")
    age = int(input("Age: "))


    new_pet = Pets(name=name, species=species, breed=breed, age=age, owner_id=current_user.id)
    session.add(new_pet)
    session.commit()
    print("Pet profile successfully created.")


#Update pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#get updated info from the user
#set that pets info to the new info
#commit changes
#print new pet info

def update_pet(current_user):
    view_pets(current_user)

    choice = int(input("Select a pet by Pet Id: "))
    pet = session.query(Pets).where(Pets.id == choice, Pets.owner_id==current_user.id.first())

    if pet:

        print("Please fill in any desired changes. Leave answers blank to keep current information.\n")
        name = input("Name: ")
        species = input("Species: ")
        breed = input("Breed: ")
        age = input("Age:")
   
        if name:
            pet.name = name
        if species:
            pet.species = species
        if breed:
            pet.breed = breed
        if age:
            pet.age = age

        session.commit()
        print("Pet successfully updated.")

    else:
        print("Invalid choice.")

        
def delete_pet(current_user):
    view_pets(current_user)

    choice = int(input("Select a pet by Pet Id: "))
    pet = session.query(Pets).where(Pets.id == choice, Pets.owner_id == current_user.id).first()

    if pet:
        confirm = input("Please type 'delete' to confirm deletion of pet profile. ")
        if confirm.lower() == 'delete':
            session.delete(pet)
            session.commit()
            print(f"Pet successfully deleted.")
    
    else:
        print("Invalid choice.")


#Delete pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#Ask user if they are sure they want to delete this pet
#delete pet from the session
#commit changes





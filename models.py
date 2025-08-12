from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean, Text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column
from datetime import date

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///pet_clinic.db')
Session = sessionmaker(bind=engine)
session = Session()


class Owners(Base):
    """Owner model representing pet owners"""
    __tablename__ = 'owners'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    
    # Relationship to pets (one-to-many)
    pets: Mapped[list["Pets"]] = relationship("Pets", back_populates="owner")
    
    def display(self):
        print("Name: ", self.name)
        print("Phone: ", self.phone)
        print("Email: ", self.email)
        print("Password: ", self.password)


class Pets(Base):
    """Pet model representing pets in the clinic"""
    __tablename__ = 'pets'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    species: Mapped[str] = mapped_column(String(50), nullable=False)  # e.g., "Dog", "Cat", "Bird"
    breed: Mapped[str] = mapped_column(String(100), nullable=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('owners.id'), nullable=False)
    
    # Relationships
    owner: Mapped["Owners"] = relationship("Owners", back_populates="pets")
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="pet")
    

    def display(self):
        print("\nName: ", self.name)
        print("Species: ", self.species)
        print("Breed: ", self.breed)
        print("Age: ", self.age)
    


class Vets(Base):
    """Veterinarian model representing clinic veterinarians"""
    __tablename__ = 'vets'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    specialization: Mapped[str] = mapped_column(String(100), nullable=True)  # e.g., "General", "Surgery", "Dermatology"
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    
    # Relationships
    appointments: Mapped[list["Appointments"]] = relationship("Appointments", back_populates="vet", )
    
    def display(self):
        print("Name: ", self.name)
        print("Specialization: ", self.specialization)
        print("Email: ", self.email)


class Appointments(Base):
    """Appointment model representing pet appointments with veterinarians"""
    __tablename__ = 'appointments'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'), nullable=False)
    veterinarian_id: Mapped[int] = mapped_column(Integer, ForeignKey('vets.id'), nullable=False)
    appointment_date: Mapped[date] = mapped_column(Date, nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="Scheduled", nullable=False)  # "Scheduled", "Completed", "Cancelled"
    
    # Relationships
    pet: Mapped["Pets"] = relationship("Pets", back_populates="appointments")
    vet: Mapped["Vets"] = relationship("Vets", back_populates="appointments")
    
def display(self):
    print("Appointment ID: ", self.id)
    print("Date: ", self.appointment_date)
    print("Vet: ", self.vet.name)
    print("Notes: ", self.notes)
    print("Status: ", self.status)



Base.metadata.create_all(engine)

# vet1 = Vets(name="Dr. Dizzy", specialization="Anesthesiologist", email="dylank@clinic.com")
# vet2 = Vets(name="Dr. James Brown", specialization="Surgery", email="james.brown@clinic.com")
# vet3 = Vets(name="Dr. Lisa Garcia", specialization="Dermatology", email="lisa.garcia@clinic.com")
# vet4 = Vets(name="Dr. Emily Wilson", specialization="General", email="emily.wilson@clinic.com")

# session.add_all([vet1,vet2,vet3,vet4])
# session.commit()
    


#============== Adding Data =================


# new_owners = [
#     Owners(name = "Shaggy Rogers", phone = "555-123-1969", email= "norvillerogers@mysteryinc.com", password="123"),
#     Owners(name = "Charlie Brown", phone = "555-111-1950", email= "peanuts@email.com", password="1234"),
#     Owners(name = "Madame Adelaide Bonfamille", phone = "555-444-1910", email= "arisocats@email.com", password="12345"),
#     Owners(name = "Harry Potter", phone = "555-777-1997", email= "yerawizard@email.com", password="123456"),
#     Owners(name = "John Arbuckle", phone = "555-222-1978", email= "lasagna@email.com", password="1234567")
# ]
# session.add_all(new_owners)
# session.commit()


# new_pets = [
#     Pets(name = "Snoopy", species = "Dog", breed= "Beagle", age=5, owner_id=2),
#     Pets(name = "Scooby-Doo", species = "Dog", breed= "Great Dane", age=9, owner_id=1),
#     Pets(name = "Hedwig", species = "Owl", breed= "Snowy Owl", age=7, owner_id=4),
#     Pets(name = "Garfield", species = "Cat", breed= "Domestic Shorthair", age=10, owner_id=5),
#     Pets(name = "Odie", species = "Dog", breed= "Mixed", age=4, owner_id=5),
#     Pets(name = "Duchess", species = "Cat", breed= "Turkish Angora", age=9, owner_id=3),
#     Pets(name = "Marie", species = "Cat", breed= "Turkish Angora", age=0, owner_id=3),
#     Pets(name = "Berlioz", species = "Cat", breed= "Turkish Angora", age=0, owner_id=3),
#     Pets(name = "Toulouse", species = "Cat", breed= "Turkish Angora", age=0, owner_id=3),
#     Pets(name = "Thomas O'Malley", species = "Cat", breed= "Domestic Shorthair", age=7, owner_id=3)
# ]
# session.add_all(new_pets)
# session.commit()



# new_appts = [
#     Appointments(pet_id = 6, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 10, 30, 0), notes = "Well behaved, model cat. No previous problems.", status = "Scheduled"),
#     Appointments(pet_id = 7, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 10, 45, 0), notes = "Checkup, no known problems. Warning: Do not mess up her bow.", status = "Scheduled"),
#     Appointments(pet_id = 8, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 11, 15, 0), notes = "To avoid distractions, keep away from his brother. Likes to bite", status = "Scheduled"),
#     Appointments(pet_id = 9, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 11, 30, 0), notes = "To avoid distractions, keep away from his brother. Likes to bite", status = "Scheduled"),
#     Appointments(pet_id = 10, veterinarian_id = 1, appointment_date = datetime(2025, 8, 15, 11, 45, 0), notes = "Adopted alleyway cat. Needs thorough checkup. Seems to be unfamiliar with vets.", status = "Scheduled"),
#     Appointments(pet_id = 1, veterinarian_id = 1, appointment_date = datetime(2025, 9, 15, 10, 45, 0), notes = "Address the dog directly, not the owner", status = "Scheduled"),
#     Appointments(pet_id = 2, veterinarian_id = 2, appointment_date = datetime(2025, 9, 25, 11, 30, 0), notes = "Clear the office, he will eat everything", status = "Cancelled"),
#     Appointments(pet_id = 4, veterinarian_id = 2, appointment_date = datetime(2025, 7, 30, 10, 30, 0), notes = "Low motivation to exercise. Has history of eating too much lasagna. Check blood report.", status = "Completed"),
#     Appointments(pet_id = 5, veterinarian_id = 2, appointment_date = datetime(2025, 7, 30, 11, 30, 0), notes = "Struggles to keep tongue in mouth. Check for dryness. Very sweet dog.", status = "Completed"),
#     Appointments(pet_id = 3, veterinarian_id = 1, appointment_date = datetime(2025, 7, 15, 10, 30, 0), notes = "Well behaved. Has shown wing fatigue before.", status = "Completed")
# ]
# session.add_all(new_appts)
# session.commit()

# print("hello testing")


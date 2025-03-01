#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Sets up my database and session creating all tables for good interaction
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# function to enable us to add data to the database
def add_sample_data():
    # this clears the data that is already there in the tables
    session.query(Company).delete()
    session.query(Dev).delete()
    session.query(Freebie).delete()
    session.commit()

    # creating example of companies ,developers and freebies i'll use to see if my code 
    company1= Company(name="ZayreGadgets",founding_year=2000)
    company2 = Company(name ="CoderBytes",founding_year=1995)

    developer1=Dev(name="Jojoh")
    developer2=Dev(name="Gabs")

    
    freebie1= Freebie(item_name="T-shirt", value=20, dev=developer1, company=company1)
    freebie2= Freebie(item_name="Laptop", value=5, dev=developer2, company=company2)

    #adds all the data together to session and saves it.
    session.add_all([company1, company2, developer1, developer2, freebie1, freebie2])#adding data to our sessions
    session.commit()

# function to test the relatrionship and methods
def run_tests():
    print("Companies:")
    companies = session.query(Company).all()
    for company in companies:
        print(company)

    #queries to check our data by printing all devlpers,freebies and companies
    print("\nDevelopers:")
    devs = session.query(Dev).all()
    for dev in devs:
        print(dev)

    print("\nFreebies:")
    freebies = session.query(Freebie).all()
    for freebie in freebies:
        print(freebie)

    # Testing  the  relationship btwn companies and developers.
    print("\nTesting Relationships:")
    company = session.query(Company).first()
    print(f"Company: {company.name}")
    print("Developers working here:")
    for dev in company.devs:
        print(f"- {dev.name}")

    dev = session.query(Dev).first()
    print(f"\nDeveloper: {dev.name}")
    print("Companies they work with:")
    for company in dev.companies:
        print(f"- {company.name}")

  #testiing the methods in the models
    print("\nTesting Methods:")
    new_freebie = company.give_freebie(dev, "cup", 10)
    session.add(new_freebie)
    session.commit()
    print(f"New Freebie: {new_freebie.item_name} (Value: {new_freebie.value})")
#does the developer have a cup?
    print(f"\nDoes {dev.name} have a cup? {dev.received_one('cup')}")

    dev2 = session.query(Dev).filter(Dev.name == "Gabs").first()
    dev.give_away(dev2,new_freebie)
    session.commit()
    
    print(f"{dev.name} gave {new_freebie.item_name} to {dev2.name}")
    print(f"{dev.name} still has a cup? {dev.received_one('cup')}")

    print("\nPrinting details of all freebies:")
    for freebie in session.query(Freebie).all():
        print(freebie.print_details())

# Main function to run the script
def main():
    add_sample_data()
    run_tests()

if __name__ == "__main__":
    main()
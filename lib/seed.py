#!/usr/bin/env python3
from models import Base, Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker

#lets create a  Sqldatabase
engine= create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

session=sessionmaker(bind=engine)
session=session()

print("Clearing data that exists")
session.query(Company).delete()
session.query(Dev).delete()
session.query(Freebie).delete()
session.commit()
print("cleared successfully")

#creating some sample data
print("creating example companies")
company1 = Company(name="ZayreGadgets", founding_year=2000)
company2 = Company(name="CoderBytes", founding_year=1995)

print("making example developers")
developer1 = Dev(name="Jojoh")
developer2 = Dev(name="Gabs")

print("creating example freebies")
freebie1 = Freebie(item_name="T-shirt", value=20, dev=developer1, company=company1)
freebie2 = Freebie(item_name="Laptop", value=5, dev=developer2, company=company2)

print("adding data to  the database")
session.add_all([company1, company2, developer1, developer2, freebie1, freebie2])
session.commit()
print("Database created successfully")


session.close()
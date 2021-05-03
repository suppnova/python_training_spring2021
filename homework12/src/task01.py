"""
Using ORM framework of your choice, create models classes created in Homework 6 (Teachers, Students, Homework and others).
- Target database should be sqlite (filename main.db localted in current directory)
- ORM framework should support migrations.

Utilizing that framework capabilities, create
 - a migration file, creating all necessary database structures.
 - a migration file (separate) creating at least one record in each created database table
 - (*) optional task: write standalone script (get_report.py) that retrieves and stores the following information into CSV file report.csv
     for all done (completed) homeworks:
         Student name (who completed homework)
         Creation date
         Teacher name who created homework


Utilize ORM capabilities as much as possible, avoiding executing raw SQL queries.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homework12.src.models import *


def create_session():
    engine = create_engine("sqlite:///main.db", echo=True)
    session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    return session()

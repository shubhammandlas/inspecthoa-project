# from flask_sqlalchemy import SQLAlchemy
# # from models.user import User

# db = SQLAlchemy()

# def init_db(app):
#     db.init_app(app)
#     print('Databse connection')

#     # Define your models here
#     # Example:
#     # from models.item import Item

#     # Create the database tables

#     with app.app_context():
#         db.create_all()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your database URL. Replace 'your_database_url' with your actual database URL.
database_url = 'postgresql://shugupta:@localhost/inspecthoa'

# Create a SQLAlchemy engine
engine = create_engine(database_url)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

def init_db(app):
    # You can perform any additional configuration here if needed.
    print('Database connection')
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

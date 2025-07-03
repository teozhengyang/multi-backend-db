from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL
# DATABASE_URL = "postgresql://user:password@localhost:5433/mydatabase"

# MySQL
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/mydatabase"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()

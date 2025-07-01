from sqlalchemy import Column, Integer, String
from database import Base

# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
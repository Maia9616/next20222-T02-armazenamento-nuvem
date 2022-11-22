from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"User(id_user={self.id_user!r}, name={self.name!r}, password={self.password!r})"


class Plan(Base):
    __tablename__ = "plan"

    id_plan = Column(Integer, primary_key=True)
    name = Column(String(45))
    limit_files = Column(Integer)
    limit_data = Column(Integer)

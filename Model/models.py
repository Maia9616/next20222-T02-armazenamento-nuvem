import json

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base


def convert_json(**kwargs):
    return json.dumps(kwargs)



Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(45))
    password = Column(String(255))

    def __repr__(self):
        return f"User(id_user={self.id_user!r}, name={self.name!r}, email={self.email!r}, password={self.password!r})"


class Plan(Base):
    __tablename__ = "plan"

    id_plan = Column(Integer, primary_key=True)
    name = Column(String(45))
    limit_files = Column(Integer)
    limit_data = Column(Integer)


    def __repr__(self):
        return convert_json(id_plan=self.id_plan, name=str(self.name),
                            limit_files=self.limit_files, limit_data=self.limit_data)

class Files(Base):
    __tablename__ = "files"

    id_file = Column(Integer, primary_key=True)
    name = Column(String(255))
    size = Column(Integer)
    user = Column (Integer)

    #representação do objeto da classe
    def __repr__(self):
        return f"Files(id_file={self.id_file!r}, name={self.name!r}, size={self.size!r}, user={self.user!r}"

class Session(Base):
    __tablename__ = "session"

    id_session = Column(Integer, primary_key=True)
    user_iduser = Column(Integer)
    token = Column(String(45))
    creation_date = Column(String(45))

    def __repr__(self):
        return f"Session(id_session={self.id_session!r}, token={self.token!r}, creation_date={self.creation_date!r}"





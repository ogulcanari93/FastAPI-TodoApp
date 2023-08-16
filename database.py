from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


engine = create_engine("sqlite:///todo.db")
Base = declarative_base()

class ToDo(Base):   
    __tablename__ = 'todos'
    id = Column(Integer, primary_key = True)
    task = Column(String(50))




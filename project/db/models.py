from sqlalchemy import Column, \
    Integer, String, Text, DateTime, Boolean, \
    Enum as SQLAEnum, \
    ForeignKey
from sqlalchemy.orm import relationship

from project.db import Base

class Poem(Base):
    __tablename__ = 'poems'
    id = Column(Integer, primary_key=True)

    author = Column(String(200))
    lines = relationship('PoemLine', back_populates='poem')
    
    def __init__(self, author):
        self.author = author


class PoemLine(Base):
    __tablename__ = 'poem_lines'
    id = Column(Integer, primary_key=True)
    
    text = Column(String(200))

    poem_id = Column(Integer, ForeignKey('poems.id'))
    poem = relationship('Poem', back_populates='lines')
    
    def __init__(self, text):
        self.text = text
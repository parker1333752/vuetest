'''
Description: Definitions of all tables storaged on Database;
Note: All tables defined as python old style class (without any parent classs).
        and table class name should end with 'Model'.

Author: Sijun Li.
'''
from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy import Text
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship, backref


class UserModel:
    id = Column(Integer, primary_key=True)
    email = Column(String(20), unique=True, nullable=False)
    name = Column(String(20))
    password = Column(String(41), nullable=False)

    items = relationship()

    def __init__(self, email=None, name=None, password=None):
        self.email = email
        self.name = name
        self.password = password

    def __repr__(self):
        return 'User<email %r>' % (self.email)


class ItemModel:
    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.id'), nullable=False)
    folder = Column(String(20))
    createtime = Column(BigInteger, nullable=False)
    alerttime = Column(BigInteger)
    finishtime = Column(BigInteger)
    text = Column(Text)

    user = relationship('User',
                        backref=backref('posts', lazy='dynamic'))

    tags = relationship

    def __init__(self, userid, folder, createtime, alerttime, finishtime, text):
        self.userid = userid
        self.folder = folder
        self.createtime = createtime
        self.alerttime = alerttime
        self.finishtime = finishtime

    def __repr__(self):
        return "Item<id: %r, text: %r>" % (self.id, self.text)


class TagModel:
    id = Column(Integer, primary_key=True)
    tag = Column(String(20), unique=True, nullable=False)

    items = relationship

    def __init__(self, tag):
        self.tag = tag

    def __repr__(self):
        return 'Tag<id: %r, tag: %r>' % (self.id, self.tag)


class Item2TagModel:
    '''
    Relationship between items and tag.
    It's a many-to-many relationship.
    '''
    itemid = Column(Integer, ForeignKey('item.id'), primary_key=True)
    tagid = Column(Integer, ForeignKey('tag.id'), primary_key=True)

    item = relationship('Item',
                        backref=backref('posts', lazy='dynamic'))
    tag = relationship('Tag',
                       backref=backref('posts', lazy='dynamic'))

from sqlalchemy import Column, Integer, String

from app import db


class Visitor(db.Model):
    '''Table for storing site visitors.'''

    __tablename__ = 'Visitors'

    id = Column(Integer, primary_key=True)
    ip = Column(String, nullable=False, index=True)
    user_agent = Column(String, nullable=False)

    @classmethod
    def get_by_ip(cls, ip):
        return db.session.query(cls).filter(cls.ip==ip).first()

    def __repr__(self):
        return f'Visitor(id={self.id} ip={self.ip})'

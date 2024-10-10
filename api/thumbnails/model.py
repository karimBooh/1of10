from operator import index

from sqlalchemy import Column, Integer, Text, BLOB, DateTime, func

from api.db.database import Base


class Thumbnail(Base):
    __tablename__ = 'thumbnails'
    id = Column(Integer, primary_key=True, index=True)
    feedback = Column(Text)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    update_date= Column(DateTime(timezone=True), onupdate=func.now())
    image = Column(BLOB)

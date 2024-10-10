from sqlalchemy.orm import Session
from . import model, schema

def get_thumbnail(db: Session, thumbnail_id: int):
    return db.query(model.Thumbnail).filter(model.Thumbnail.id == thumbnail_id).first()


def get_thumbnails(db: Session, skip:int=0, limit:int=100):
    return db.query(model.Thumbnail).offset(skip).limit(limit).all()


def create_thumbnails(db: Session, thumbnail:schema.ThumbnailCreate):
    db_thumbnail = model.Thumbnail(feedback=thumbnail.feedback,
                          image=thumbnail.image)
    db.add(db_thumbnail)
    db.commit()
    db.refresh(db_thumbnail)
    return db_thumbnail
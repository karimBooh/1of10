
from .thumbnails import model as model_thumbnail
from .db.database import SessionLocal, engine

from api.thumbnails.route import router as router_thumbnail


def models():
    model_thumbnail.Base.metadata.create_all(bind=engine)

def routes(app):
    app.include_router(router_thumbnail)
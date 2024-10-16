from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .modules import routes, models

models()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routes(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}

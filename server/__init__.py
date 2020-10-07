from fastapi import FastAPI

from server.config.database import SessionLocal
from server.config.routes import routes

db_session = SessionLocal()

app = FastAPI()
routes()

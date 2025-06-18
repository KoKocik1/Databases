import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import Session

from .Models.models import Base

load_dotenv()


def get_database_url():
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRESS_ADDRESS = os.getenv("POSTGRESS_ADDRESS")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    if not all([POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRESS_ADDRESS, POSTGRES_PORT]):
        raise EnvironmentError(
            "Database environment variables are not fully set.")
    return (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRESS_ADDRESS}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )


engine = create_engine(get_database_url())


def init_db():
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    # If you modified something into the database then remove docker container
    # with command: `docker compose down -v`
    if not existing_tables:
        with engine.connect() as conn:
            conn.execute(text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'))
            conn.commit()
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully")
    else:
        print("Database tables already exist")


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

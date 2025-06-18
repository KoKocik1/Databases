from sqlalchemy import BigInteger, Column, Float, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(
        PostgresUUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )
    telegram_id = Column(BigInteger, unique=True)
    name = Column(String(255))

from sqlalchemy.orm import Session

from ..Models.models import User


def create_user(db: Session, user_id: str) -> User:
    user = User(id=user_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: str) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

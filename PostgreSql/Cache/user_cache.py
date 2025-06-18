from typing import Dict, Optional

from ..Models.models import User


class UserCache:
    _instance = None
    _cache: Dict[str, User] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_user(self, user_id: str) -> Optional[User]:
        return self._cache.get(user_id)

    def get_user_id(self, user_id: str) -> str:
        user = self.get_user(user_id)
        if user is None:
            raise ValueError(
                f"User with id {user_id} not found in cache")
        return str(user.id)

    def add_user(self, user_id: str, user: User) -> None:
        self._cache[user_id] = user

    def has_user(self, user_id: str) -> bool:
        return user_id in self._cache

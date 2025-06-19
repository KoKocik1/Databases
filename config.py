import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    allowed_user_ids: list[int]

    @classmethod
    def from_env(cls) -> "Config":
        load_dotenv()

        allowed_user_ids_str = os.getenv("ALLOWED_USER_IDS", "")
        allowed_user_ids = [
            int(uid.strip()) for uid in allowed_user_ids_str.split(",") if uid.strip()
        ]

        return cls(
            allowed_user_ids=allowed_user_ids,
        )

    def validate(self) -> None:
        missing_vars = []

        if not self.allowed_user_ids:
            missing_vars.append("ALLOWED_USER_IDS")

        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )

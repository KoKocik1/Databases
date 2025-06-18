from functools import wraps

from ..SqlDB.database import get_db
from ..Cache.user_cache import UserCache
from ..Service.user_service import create_user, get_user_by_id


def ensure_user_in_db(user_id_extractor):
    """
    Example ussage (Telegram):

    from telegram import Update
    from telegram.ext import ContextTypes

    def telegram_user_id_extractor(update, context, *args, **kwargs):
        if hasattr(update, "effective_user") and update.effective_user:
            return update.effective_user.id
        return None

    Create decorator:
    update_db_user = ensure_user_in_db(telegram_user_id_extractor)

    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            user_id = user_id_extractor(*args, **kwargs)
            if not user_id:
                return await func(*args, **kwargs)
            cache = UserCache()
            if cache.has_user(user_id):
                return await func(*args, **kwargs)
            db = next(get_db())
            try:
                user = get_user_by_id(db, user_id)
                if not user:
                    user = create_user(db, user_id)
                cache.add_user(user_id, user)
                return await func(*args, **kwargs)
            finally:
                db.close()
        return wrapper
    return decorator

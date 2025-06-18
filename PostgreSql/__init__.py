"""
PostgresTemplate - A PostgreSQL database template module for Python projects.

This module provides a complete PostgreSQL database setup with SQLAlchemy ORM,
caching, middleware, and service layers for building scalable applications.

Example usage:
    from PostgresTemplate import initialize_database, UserService, UserCache
    
    # Initialize the database
    initialize_database()
    
    # Use services
    user = UserService.create_user(db_session, user_id)
    
    # Use cache
    cache = UserCache()
    cached_user = cache.get_user(user_id)
"""

# Database and core functionality
from .SqlDB.database import init_db, get_db, engine, get_database_url

# Models
from .Models.models import Base, User

# Services
from .Service import user_service as UserService
from .Service.user_service import create_user, get_user_by_id

# Cache
from .Cache.user_cache import UserCache

# Middleware
from .Middleware.middleware import update_db_user

# Public API - what users should import
__all__ = [
    # Database functions
    "init_db",
    "get_db",
    "engine",
    "get_database_url",

    # Models
    "Base",
    "User",

    # Services
    "UserService",
    "create_user",
    "get_user_by_id",

    # Cache
    "UserCache",

    # Middleware
    "update_db_user",

    # Utility functions
    "initialize_database",
]


def initialize_database():
    """Initialize the PostgreSQL database with all required tables and extensions."""
    init_db()

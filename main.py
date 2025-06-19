from PostgreSql import initialize_database
from config import Config

config = Config.from_env()
config.validate()

if __name__ == "__main__":
    print("Initializing database...")
    initialize_database()

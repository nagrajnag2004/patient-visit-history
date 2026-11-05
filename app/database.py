import os
from dotenv import load_dotenv
import certifi
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from .env file
load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "mysql").lower()

if DB_TYPE == "sqlite":
    # SQLite: Zero installation, local file
    DATABASE_URL = "sqlite:///./patient_visit.db"
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
    print("-> Using SQLite database: ./patient_visit.db")
else:
    # MySQL / TiDB Cloud
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "test")

    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    connect_args = {}
    # TiDB Cloud requires secure TLS encryption with CA certificate
    if "tidbcloud.com" in DB_HOST or str(DB_PORT) == "4000":
        connect_args = {
            "ssl": {
                "ca": certifi.where()
            }
        }

    engine = create_engine(
        DATABASE_URL,
        connect_args=connect_args,
        pool_pre_ping=True,
        pool_recycle=3600
    )
    print(f"-> Using MySQL database: '{DB_NAME}' on {DB_HOST}")

# SessionLocal is a factory for new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all SQLAlchemy database models
Base = declarative_base()


# Dependency to get DB session per request, and safely close it afterwards
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from src.config import get_settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{get_settings().DB_USER}:{get_settings().DB_PASS}"f"@" \
                          f"{get_settings().DB_HOST}:{get_settings().DB_PORT}/{get_settings().DB_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

host = 'localhost'
user = 'postgres'
password = 'root'
database = "employee"
port = 5432
url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(url,echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
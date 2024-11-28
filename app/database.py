from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:admin@localhost/SistemaClinico"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("Conexión a la base de datos exitosa")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

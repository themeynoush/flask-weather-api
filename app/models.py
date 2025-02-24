from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import Config


Base = declarative_base()


class WeatherData(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)
    temperature_c = Column(Float)
    temperature_f = Column(Float)
    condition = Column(String)


engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    """Create tables if they don't exist."""
    Base.metadata.create_all(engine)

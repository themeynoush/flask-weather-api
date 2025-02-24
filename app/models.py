from datetime import datetime
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


class WeatherRequestLog(Base):
    __tablename__ = "weather_requests"
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)
    timestamp = Column(String, default=datetime.utcnow)


class UserFavorites(Base):
    __tablename__ = "user_favorites"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    city = Column(String, nullable=False)


engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    """Create tables if they don't exist."""
    Base.metadata.create_all(engine)

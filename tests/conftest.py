import pytest
from app.models import Base, engine, SessionLocal


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Create and clean the database for testing."""
    Base.metadata.drop_all(bind=engine)  # Remove existing tables
    Base.metadata.create_all(bind=engine)  # Create tables
    yield
    Base.metadata.drop_all(bind=engine)  # Clean up after tests

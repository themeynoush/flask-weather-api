import pytest
from app.models import SessionLocal, UserFavorites
from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_add_favorite(client):
    """Ensure a user can add a favorite city."""
    response = client.post("/weather/favorite", json={"user_id": 1, "city": "Paris"})

    assert response.status_code == 200
    assert response.json["message"] == "Favorite city added!"

    session = SessionLocal()
    favorite = session.query(UserFavorites).filter_by(user_id=1, city="Paris").first()

    assert favorite is not None
    assert favorite.city == "Paris"

    session.close()


def test_get_favorites(client):
    """Ensure user can retrieve saved favorite cities."""
    session = SessionLocal()
    session.add(UserFavorites(user_id=1, city="London"))
    session.commit()

    response = client.get("/weather/favorites/1")

    assert response.status_code == 200
    assert "London" in response.json["favorites"]

    session.close()

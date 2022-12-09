from unittest.mock import Mock, patch


def test_signup_user_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True

        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }

        response = client.post(
            "/users/signup",
            json=user,
        )

    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == user["email"]
    assert data["username"] == user["username"]
    assert data["surname"] == user["surname"]


def test_signup_user_without_email(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True

        user = {
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }

        response = client.post(
            "/users/signup",
            json=user,
        )

    assert response.status_code == 422, response.text


def test_signup_same_user_twice(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        # mock_get.return_value.json.return_value = {}

        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }

        response1 = client.post(
            "/users/signup",
            json=user,
        )

        response2 = client.post(
            "/users/signup",
            json=user,
        )

    assert response1.status_code == 201
    assert response2.status_code == 409
    assert response2.json()["detail"] == "The user already exists"

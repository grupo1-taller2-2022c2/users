from unittest.mock import Mock, patch


def test_user_address_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        address = {
            "email": "test_email@gmail.com",
            "street_name": "paseo colon",
            "street_number": 850
        }

        response = client.post(
            "/passengers/address",
            json=address
        )

    assert response.status_code == 404
    assert response.json()["detail"] == "The user doesn't exist"


def test_user_address_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=user,
        )

        address = {
            "email": "test_email@gmail.com",
            "street_name": "paseo colon",
            "street_number": 850
        }
        response = client.post(
            "/passengers/address",
            json=address
        )

    assert response.status_code == 201


def test_user_profile_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True

        response = client.get(
            "/passengers/test_email@gmail.com"
        )

    assert response.status_code == 404
    assert response.json()["detail"] == "The user doesn't exist"


def test_user_profile_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=user,
        )

        response = client.get(
            "/passengers/test_email@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()["username"] == "test_username"
    assert response.json()["surname"] == "test_surname"


def test_self_profile_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True

        response = client.get(
            "/passengers/me/test_email@gmail.com"
        )

    assert response.status_code == 404
    assert response.json()["detail"] == "The user doesn't exist"


def test_self_profile_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=user,
        )

        response = client.get(
            "/passengers/me/test_email@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()["email"] == "test_email@gmail.com"
    assert response.json()["username"] == "test_username"
    assert response.json()["surname"] == "test_surname"


def test_modify_profile_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        new_profile = {
            "username": "test_username_1",
            "surname": "test_surname_1",
            "ratings": 0,
            "photo": "new_url"
        }
        response = client.patch(
            "/passengers/test_email@gmail.com",
            json=new_profile
        )

    assert response.status_code == 404
    assert response.json()["detail"] == "The user doesn't exist"


def test_modify_profile_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=user,
        )
        new_profile = {
            "username": "test_username_1",
            "surname": "test_surname_1",
            "ratings": 0,
            "photo": "new_url"
        }
        client.patch(
            "/passengers/test_email@gmail.com",
            json=new_profile
        )
        response = client.get(
            "/passengers/test_email@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()["username"] == "test_username_1"
    assert response.json()["surname"] == "test_surname_1"


def test_add_rating_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        rating = {
            "passenger_email": "test_email@gmail.com",
            "trip_id": 1,
            "ratings": 4,
            "message": "Ok"
        }
        response = client.post(
            "/passengers/ratings",
            json=rating
        )

    assert response.status_code == 404
    assert response.json()["detail"] == "The user doesn't exist"


def test_add_rating_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=user,
        )
        rating = {
            "passenger_email": "test_email@gmail.com",
            "trip_id": 1,
            "ratings": 4,
            "message": "Ok"
        }
        response = client.post(
            "/passengers/ratings",
            json=rating
        )

    assert response.status_code == 201


def test_get_none_rating_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        response = client.get(
            "/passengers/ratings/all/test_email@gmail.com"
        )

    assert response.status_code == 404


def test_get_none_rating_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=user,
        )
        response = client.get(
            "/passengers/ratings/all/test_email@gmail.com"
        )

    assert response.status_code == 200
    assert response.json() == []


def test_get_all_rating_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=user,
        )
        rating = {
            "passenger_email": "test_email@gmail.com",
            "trip_id": 1,
            "ratings": 4,
            "message": "Ok"
        }
        client.post(
            "/passengers/ratings",
            json=rating
        )
        response = client.get(
            "/passengers/ratings/all/test_email@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()[0]["email"] == rating["passenger_email"]
    assert response.json()[0]["trip_id"] == rating["trip_id"]
    assert response.json()[0]["ratings"] == rating["ratings"]
    assert response.json()[0]["message"] == rating["message"]


def test_get_one_rating_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        user = {
            "email": "test_email@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=user,
        )
        rating = {
            "passenger_email": "test_email@gmail.com",
            "trip_id": 1,
            "ratings": 4,
            "message": "Ok"
        }
        client.post(
            "/passengers/ratings",
            json=rating
        )
        response = client.get(
            "/passengers/ratings/1"
        )

    assert response.status_code == 200
    assert response.json()["ratings"] == rating["ratings"]

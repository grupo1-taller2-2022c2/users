
from unittest.mock import Mock, patch


def test_add_driver_vehicle_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }

        response = client.post(
            "/drivers/vehicle",
            json=vehicle
        )

    assert response.status_code == 404
    assert response.json()["detail"] == "The user doesn't exist"


def test_add_driver_vehicle_ok(client):
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
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        response = client.post(
            "/drivers/vehicle",
            json=vehicle
        )

    assert response.status_code == 201


def test_get_empty_available_drivers_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True

        response = client.get(
            "/drivers/all_available"
        )

    assert response.status_code == 200
    assert response.json() == []


def test_get_all_available_drivers_ok(client):
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
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )

        response = client.get(
            "/drivers/all_available"
        )

    assert response.status_code == 200
    assert response.json()[0]["email"] == vehicle["email"]
    assert response.json()[0]["licence_plate"] == vehicle["licence_plate"]
    assert response.json()[0]["model"] == vehicle["model"]
    assert response.json()[0]["username"] == user["username"]
    assert response.json()[0]["surname"] == user["surname"]


def test_driver_profile_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True

        response = client.get(
            "/drivers/test_email@gmail.com"
        )

    assert response.status_code == 404
    assert response.json()["detail"] == "The user doesn't exist"


def test_driver_profile_ok(client):
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
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )

        response = client.get(
            "/drivers/test_email@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()["username"] == "test_username"
    assert response.json()["surname"] == "test_surname"


def test_driver_self_profile_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True

        response = client.get(
            "/drivers/me/test_email@gmail.com"
        )

    assert response.status_code == 404
    assert response.json()["detail"] == "The user doesn't exist"


def test_driver_self_profile_ok(client):
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
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )

        response = client.get(
            "/drivers/me/test_email@gmail.com"
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
            "licence_plate": "test_licence_plate_1",
            "model": "test_model_1",
            "ratings": 0,
            "photo": "new_url"
        }
        response = client.patch(
            "/drivers/test_email@gmail.com",
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
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )
        new_profile = {
            "username": "test_username_1",
            "surname": "test_surname_1",
            "licence_plate": "test_licence_plate_1",
            "model": "test_model_1",
            "ratings": 0,
            "photo": "new_url"
        }
        client.patch(
            "/drivers/test_email@gmail.com",
            json=new_profile
        )
        response = client.get(
            "/drivers/test_email@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()["username"] == "test_username_1"
    assert response.json()["surname"] == "test_surname_1"
    assert response.json()["licence_plate"] == "test_licence_plate_1"
    assert response.json()["model"] == "test_model_1"


def test_add_rating_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        rating = {
            "driver_email": "test_email@gmail.com",
            "trip_id": 1,
            "ratings": 4,
            "message": "Ok"
        }
        response = client.post(
            "/drivers/ratings",
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
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )
        rating = {
            "driver_email": "test_email@gmail.com",
            "trip_id": 1,
            "ratings": 4,
            "message": "Ok"
        }
        response = client.post(
            "/drivers/ratings",
            json=rating
        )

    assert response.status_code == 201


def test_get_none_rating_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        response = client.get(
            "/drivers/ratings/all/test_email@gmail.com"
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
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )
        response = client.get(
            "/drivers/ratings/all/test_email@gmail.com"
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
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )
        rating = {
            "driver_email": "test_email@gmail.com",
            "trip_id": 1,
            "ratings": 4,
            "message": "Ok"
        }
        client.post(
            "/drivers/ratings",
            json=rating
        )
        response = client.get(
            "/drivers/ratings/all/test_email@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()[0]["email"] == rating["driver_email"]
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
        vehicle = {
            "email": "test_email@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )
        rating = {
            "driver_email": "test_email@gmail.com",
            "trip_id": 1,
            "ratings": 4,
            "message": "Ok"
        }
        client.post(
            "/drivers/ratings",
            json=rating
        )
        response = client.get(
            "/drivers/ratings/1"
        )

    assert response.status_code == 200
    assert response.json()["ratings"] == rating["ratings"]


def test_driver_report_without_passenger_not_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        driver = {
            "email": "test_driver@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=driver,
        )
        vehicle = {
            "email": "test_driver@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )
        report = {
            "driver_email": "test_driver@gmail.com",
            "passenger_email": "test_passenger@gmail.com",
            "trip_id": 1,
            "reason": "test_reason"
        }
        response = client.post(
            "/drivers/reports",
            json=report
        )
    assert response.status_code == 404
    assert response.json()["detail"] == "The passenger doesn't exist"


def test_driver_report_ok(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        driver = {
            "email": "test_driver@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=driver,
        )
        passenger = {
            "email": "test_passenger@gmail.com",
            "username": "test_username",
            "password": "test_pass",
            "surname": "test_surname",
        }
        client.post(
            "/users/signup",
            json=passenger,
        )
        vehicle = {
            "email": "test_driver@gmail.com",
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }
        client.post(
            "/drivers/vehicle",
            json=vehicle
        )
        report = {
            "driver_email": "test_driver@gmail.com",
            "passenger_email": "test_passenger@gmail.com",
            "trip_id": 1,
            "reason": "test_reason"
        }
        response = client.post(
            "/drivers/reports",
            json=report
        )
    assert response.status_code == 201

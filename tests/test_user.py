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


def test_signin_user_that_doesnt_exist(client):

    user = {
        "email": "test_username@gmail.com",
        "password": "test_pass"
    }

    response = client.post(
        "/users/grantaccess",
        json=user,
    )

    assert response.status_code == 403, response.text
    assert response.json()["detail"] == "Incorrect username or password"


def test_signin_user_ok(client):
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

        user = {
            "email": "test_email@gmail.com",
            "password": "test_pass"
        }
        response = client.post(
            "/users/grantaccess",
            json=user,
        )

    assert response.status_code == 200, response.text
    assert response.json()["username"] == "test_username"
    assert response.json()["surname"] == "test_surname"


def test_empty_list_of_users(client):
    response = client.get(
        "/users/"
    )

    assert response.status_code == 200, response.text
    assert response.json() == []


def test_list_of_users(client):
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
            "/users/"
        )

    assert response.status_code == 200, response.text
    assert response.json()[0]["email"] == "test_email@gmail.com"


def test_none_blocked_users(client):
    response = client.get(
        "/users/blocked"
    )
    assert response.status_code == 200
    assert response.text == "0"


def test_block_invalid_user(client):
    response = client.post(
        "users/blocked/test_email@gmail.com"
    )
    assert response.status_code == 403


def test_block_user(client):
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
        response = client.post(
            "users/blocked/test_email@gmail.com"
        )
    assert response.status_code == 200
    assert response.json()["message"] == 'User blocked'


def test_blocked_users(client):
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
        client.post(
            "users/blocked/test_email@gmail.com"
        )
        response = client.get(
            "/users/blocked"
        )
    assert response.status_code == 200
    assert response.text == "1"


def test_user_is_not_blocked(client):
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
            "users/blocked/test_email@gmail.com"
        )
    assert response.status_code == 200
    assert not response.json()["is_blocked"]


def test_user_is_blocked(client):
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
        client.post(
            "users/blocked/test_email@gmail.com"
        )
        response = client.get(
            "users/blocked/test_email@gmail.com"
        )
    assert response.status_code == 200
    assert response.json()["is_blocked"]


def test_invalid_unblock_user(client):
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
        response = client.post(
            "users/unblocked/test_email@gmail.com"
        )
    assert response.status_code == 403
    assert response.json()["detail"] == "The user is already unblocked"


def test_unblock_user(client):
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
        client.post(
            "users/blocked/test_email@gmail.com"
        )
        response = client.post(
            "users/unblocked/test_email@gmail.com"
        )
    assert response.status_code == 200


def cannot_get_wallet_info(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        response = client.get(
            "users/test_email@gmail.com/wallet"
        )
    assert response.status_code == 403


def get_wallet_info(client):
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
            "users/test_email@gmail.com/wallet"
        )
    assert response.status_code == 200


def get_user_id(client):
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
        "users/test_email@gmail.com/id"
    )
    assert response.status_code == 200
    assert response.text == '1'


def make_wallet_withdrawal(client):
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
        withdrawal = {
            "user_external_wallet_address": "address",
            "amount_in_ethers": "0.006"
        }
        response = client.post(
            "/users/test_email@gmail.com/wallet/withdrawals",
            json=withdrawal
        )
    assert response.status_code == 200
    assert response.status_code == 400


def invalid_wallet_withdrawal(client):
    with patch("app.helpers.user_helpers.requests.post") as mock_post:
        # Mockeo la llamada a wallets para crear la wallet
        mock_post.return_value.ok = True
        withdrawal = {
            "user_external_wallet_address": "address",
            "amount_in_ethers": "0.006"
        }
        response = client.post(
            "/users/test_email@gmail.com/wallet/withdrawals",
            json=withdrawal
        )
    assert response.status_code == 403

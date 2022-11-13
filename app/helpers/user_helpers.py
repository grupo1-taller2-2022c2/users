import hashlib
import json
import os
import requests
from fastapi import HTTPException

backoffice_base_url = os.getenv('BACKOFFICE_BASE_URL')
wallets_base_url = os.getenv('WALLETS_BASE_URL')


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def send_reg_notification_to_backoffice(reg_method):
    url = backoffice_base_url + "/metrics/registrations?method=" + reg_method
    response = requests.post(url=url)

    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


def send_login_notification_to_backoffice(reg_method):
    url = backoffice_base_url + "/metrics/logins?method=" + reg_method
    response = requests.post(url=url)

    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


def create_wallet_for_new_user(user_id):
    url = wallets_base_url + "/wallets"
    body = {'user_id': user_id}
    response = requests.post(url=url, json=body)
    print("Wallet created for new user: \n" + response.content)

    if response.ok:
        return 0
    raise HTTPException(status_code=response.status_code,
                        detail=response.json())


def get_wallet_info(user_id):
    url = wallets_base_url + "/wallets/" + str(user_id)
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json())


def withdraw_funds_from_user_wallet(user_id, withdrawal_info):
    url = wallets_base_url + "/wallets/" + str(user_id) + "/withdrawals"
    body = {'user_external_wallet_address': withdrawal_info.user_external_wallet_address,
            'amount_in_ethers': withdrawal_info.amount_in_ethers}
    response = requests.post(url=url, json=body)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json())

import hashlib
import os
import requests
from fastapi import HTTPException

url_base = os.getenv('BACKOFFICE_BASE_URL')


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def send_reg_notification_to_backoffice(reg_method):
    url = url_base + "/metrics/registrations?method=" + reg_method
    response = requests.post(url=url)

    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


def send_login_notification_to_backoffice(reg_method):
    url = url_base + "/metrics/logins?method=" + reg_method
    response = requests.post(url=url)

    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])

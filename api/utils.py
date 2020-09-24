from flask import current_app
from authlib.jose import jwt
import requests


def get_payload(token: str) -> dict:
    """Decode data form jwt"""
    return dict(jwt.decode(token, current_app.config.get('SECRET_KEY')))


def get_apod_info(url: str, date: str, hd: bool) -> dict:
    """
    Return link to picture of the day and picture's description.

    url: NASA "APOD"-api's endpoint;
    date: date for day's picture;
    hd: True - high definition, False - lowe definition;

    return - dict, where
    explanation: picture's description
    link: link for downloading.
    """
    res = requests.get(url, params={'date': date}).json()
    link = res['hdurl'] if hd else res['url']
    return {
        'explanation': res['explanation'],
        'link': link
    }

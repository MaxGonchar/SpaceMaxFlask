import requests


def get_apod_data(url: str, date: str, hd: bool) -> dict:
    """
    Return link to picture of the day and picture's description.

    params:
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


def upload_image(link: str, pas: str):
    """"""


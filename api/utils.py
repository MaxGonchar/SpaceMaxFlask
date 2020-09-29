import requests


def get_apod(url: str, date: str, hd: bool) -> dict:
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
    response = requests.get(url, params={'date': date})
    response.raise_for_status()
    res = response.json()

    explanation = res['explanation']
    link = res['hdurl'] if hd == 'True' else res['url']

    return {
        'explanation': explanation,
        'link': link
    }


def download_image(link: str, path: str):
    pass


def get_jwt():
    pass


def get_json() -> dict:
    pass


# def jsonify_data():
#     pass


# def jsonify_error():
#     pass

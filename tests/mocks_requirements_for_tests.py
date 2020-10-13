VALID_APOD_RESPONSE_DATA = {
    "explanation": "Some explanation",
    "url": "https://domen/adres/image.jpg",
    "hdurl": "https://domen/adres/imagehd.jpg"
}
INVALID_APOD_RESPONSE_DATA = {"explanation": "Something is going wrong"}

VALID_CME_RESPONSE_DATA = [
    {
        "startTime": "2020-09-30T12:09Z",
        "link": "https://kauai.ccmc.gsfc.nasa.gov/DONKI/view/CME/15902/-1",
        "note": "The source is unclear, no candidate eruptions could be "
                "identified. It is possible that an eruption occurring on "
                "the western limb of STA EUVI during a data gap in STA EUVI "
                "imagery is the culprit.",
    }
]

REQUIRED_RESPONSE_WRONG_JWT = {
            "message": "Wrong JWT structure",
            "status_code": 401
}

REQUIRED_DAYIMAGE_RESPONSE_OK = {
    'explanation': 'Some explanation',
    'message': 'Image successfully downloaded, link:'
               ' /Users/mhonc/Projects/SpaceMaxFlask/media/'
               '2020-09-20_hd.jpg'
}
DREQUIRED_AYIMAGE_RESPONSE_INVALID_APOD_DATA = {
            "message": "'url'",
            "status_code": 500
}

REQUIRED_CME_RESPONSE_OK = [
    {
        "coronalMassEjectionQuantity": 1
    },
    [
        {
            "explanation": "The source is unclear, no candidate eruptions "
                           "could be identified. It is possible that an "
                           "eruption occurring on the western limb of STA "
                           "EUVI during a data gap in STA EUVI imagery is "
                           "the culprit.",
            "link to DONKI": "https://kauai.ccmc.gsfc.nasa.gov/DONKI/"
                             "view/CME/15902/-1",
            "startTime": "2020-09-30T12:09Z"
        }
    ]
]

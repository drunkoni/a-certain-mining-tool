import pprint
from googleapiclient.discovery import build
from secret import API_KEY,SEARCHENGINE_ID

def search(keyword):
    """Custom search"""
    service = build(                    # Initialize google Api
        "customsearch",
        "v1",
        developerKey = API_KEY
    )

    data = service.cse().list(
        q = keyword,
        cx = SEARCHENGINE_ID
    ).execute()

    pprint.pprint(data)

search('linux')
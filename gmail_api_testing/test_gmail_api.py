from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ["https://mail.google.com/"]


# this function is used  to establish connection between gmail api
def get_mail_info():
    creds = None
    if os.path.exists('../token.json'):
        creds = Credentials.from_authorized_user_file('../token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('../token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service


# this function is used  to check list api is working or not and id used in assert is from mail
# to check whether list api retrieving proper id's or not
def test_list_api():
    service = get_mail_info()
    results = service.users().messages().list(userId='me').execute()
    results = results.get('messages', [])
    # list of emails id's stored in list
    lst = [messages['id'] for messages in results]
    assert '179cfb54742b3d8a'  in lst


# this function to check trash api and id is passed and message with particular id will be moved
# to trash then once i will be getting the list of id's and check it is not in the list
def test_trash_api():
    service = get_mail_info()
    # below line send the message to trash
    results = service.users().messages().trash(userId='me', id='179cfa532d5b9f1e').execute()
    # then i am getting the list of message id's to check it has been send to trash
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    results = results.get('messages', [])
    lst = [messages['id'] for messages in results]
    # assert checks whether the message has been moved or not
    assert '179cfa532d5b9f1e' not in lst

# function to check untrash api is working or not
# same id passed in trash is passed into untrash api and message with respective id is moved back from trash
def test_untrash():
    service = get_mail_info()
    # below line remove the message from trash and sends back
    results = service.users().messages().untrash(userId='me', id='179cfa532d5b9f1e').execute()
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    results = results.get('messages', [])
    lst = [messages['id'] for messages in results]
    # the below assert checks the message is moved back into respective place
    assert '179cfa532d5b9f1e' in lst

# function to check modify api
def test_modify():
    service = get_mail_info()
    # the below line code modify message labels from unread to important and it is verified using assert
    post_data = {
        "addLabelIds": [
            'CATEGORY_PERSONAL',
            "IMPORTANT"

        ],
        "removeLabelIds": [
            "CATEGORY_PROMOTIONS",
            "UNREAD"
        ]
    }
    # the below line modify the message labels
    results = service.users().messages().modify(userId='me', id="179ad1f548974f92", body=post_data).execute()
    results = service.users().messages().get(userId='me', id="179ad1f548974f92").execute()
    labels = results.get("labelIds", [])
    # the below assert verifies it
    assert ['IMPORTANT', 'CATEGORY_PERSONAL'] == labels

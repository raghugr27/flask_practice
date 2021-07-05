# Importing all the models
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pytest
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("creating and setting the value to logger")
logging.basicConfig(
    filename="logfile1.log", format="%(asctime)s %(message)s", filemode="w"
)

# If modifying these scopes, delete the file token.json.
logger.info("Entered into the scope")
# SCOPES = ['https://www.googleapis.com/auth/classroom.courses']
SCOPES = ['https://www.googleapis.com/auth/classroom.rosters']


# This function is used  to establish connection between google classroom api
@pytest.fixture()
def service():
    logger.info("Calling the main service function using pytest fixture ")
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('classroom', 'v1', credentials=creds)
    return service


# this function is used  to create a course api
def course_create(service):
    logger.info("Function to create a course")
    course = {
        'name': 'python',
        'section': 'class 4',
        'descriptionHeading': 'Welcome to python',
        'description': """We'll be learning about about the
                     structure of code""",
        'room': '303',
        'ownerId': 'me',
        'courseState': 'PROVISIONED'
    }
    course = service.courses().create(body=course).execute()
    print('Course created: %s %s' % (course.get('name'), course.get('id')))


# this function is used  to check list api is working or not and testing using assert statements
def test_get_list(service):
    logger.info("Function to get the list and to test the data using assert statements")
    results = service.courses().students().list(courseId="360068019757", pageSize=10).execute()
    assert '102827317029388411088' != results['students'][1]['profile']['id']
    assert '1028273170293884110008' not in results['students'][1]['profile']['id']
    assert type(results) == dict
    assert results
    assert len(results) != 0
    return results


# this function is used  to add student api by using invitations and testing using assert statements
def test_add_student(service):
    logger.info("Function to add the student and to test the data using assert statements")
    info = {
        "userId": "kkmkkklaku2998@gmail.com",
        "courseId": "360068019757",
        "role": "STUDENT"
    }
    service.invitations().create(body=info).execute()
    student_list = test_get_list(service)
    assert len(student_list) != 0
    assert 'manu' not in student_list['students'][1]['profile']['name']
    assert 'biradar' in student_list['students'][1]['profile']['name']['familyName']
    assert student_list


# this function is used  to get the specified user details and testing using assert statements
def test_get_method(service):
    logger.info("Function to get the specified student and to test the data using assert statements")
    results = service.courses().students().get(courseId='360068019757', userId='114205514281092595614').execute()
    student_list = test_get_list(service)
    assert len(results) == 0, "it is not equal to zero"
    assert results['userId'] == student_list['students'][0]['userId']
    assert results['courseId'] not in student_list['students']
    assert results['profile']['id'] != '3245767788'
    assert student_list
    assert type(results) == dict
    assert type(student_list['students']) == list


'''
# this function is used  to delete the specified student api is working or not and testing using assert statements
def test_delete_student(service):
    logger.info("Function to delete the student and to check whether the data deleted or not using assert statements")
    service.courses().students().delete(courseId='360068019757', userId= '102827317029388411088').execute()
    student_list = test_get_list(service)
    assert student_list
    assert '360068019757' not in student_list
    assert '102827317029388411088' not in student_list
'''
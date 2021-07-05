from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient import errors
import pytest
# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/classroom.courses']
SCOPES = ['https://www.googleapis.com/auth/classroom.rosters']


def get_info():
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

@pytest.fixture()
def service():
    service = get_info()
    return service

def course_create(service):
    #service = get_info()
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


def createstudent(service):
    enrollment_code = 'fdheb2e'
    course_id = '360068019757'
    student = {
        'userId': 'inder'
    }
    try:
        student = service.courses().students().create(
            courseId=course_id,
            enrollmentCode=enrollment_code,
            body=student).execute()
        print(
            '''User {%s} was enrolled as a student in
            the course with ID "{%s}"'''
            % (student.get('profile').get('name').get('fullName'),
            course_id))
    except errors.HttpError as error:
        print('You are already a member of this course.')


def accept_invitation():
    service = get_info()
    result = add_student(service)
    id = result['id']
    print(id)
    student = service.invitations().accept(id)
    print(student)


def add_student(service):
    info = {
        "userId": "aurnm98@gmail.com",
        "courseId": "360068019757",
        "role": "STUDENT"
    }
    student = service.invitations().create(body=info).execute()
    print(student)
    return student

def test_get_list(service):
    results = service.courses().students().list(courseId="360068019757", pageSize=10).execute()
    lst = results.get('profile').get('name').get('fullName')
    print(lst)
    assert '102827317029388411088' == results['students'][1]['profile']['id']
    assert '1028273170293884110008' != results['students'][1]['profile']['id']
    return results


def test_get_method(service):
    results = service.courses().students().get(courseId='360068019757', userId='114205514281092595614').execute()
    student_list = test_get_list(service)
    assert results['userId']==student_list['students'][0]['userId']
    assert results['courseId'] != student_list['students']


def delete_student(service):
    service.courses().students().delete(courseId='360068019757',userId= '102827317029388411088').execute()

accept_invitation()
#add_student()
#get_list()
#delete_student()
#get_method()
#get_list()
#course_create()
#get_list()
#delete_student()
#get_list()
#createstudent()
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GS:
    __SCOPES = None
    __creds = None
    __service = any

    def __init__(self, scopes) -> None:
        if not scopes:
            raise Exception("Scope List can´t be null !!")
        self.__SCOPES = scopes.copy()

    def auth(self) -> None:
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.__SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.__SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.__creds = creds

    def buildService(self) -> None:
        try:
            self.__service = build('sheets', 'v4', credentials = self.__creds).spreadsheets()
        except HttpError as err:
            raise Exception(err)
        

    def getSheet(self, spreadSheetId, sheetName, range) -> list:
        try:
            result = self.__service.values().get(
                spreadsheetId = spreadSheetId,
                range = f"{sheetName}!{range}",
                majorDimension = "COLUMNS"
                ).execute().get('values', [])
            return result
        except HttpError as err:
            raise Exception(err)

    def updateSheet(self, spreadSheetId, sheetName, range, data) -> None:
        try:
            result = self.__service.values().update(
                spreadsheetId = spreadSheetId, 
                range = f"{sheetName}!{range}", 
                valueInputOption = 'USER_ENTERED', 
                body=data
            ).execute()
        except HttpError as err:
            raise Exception(err)
                                    
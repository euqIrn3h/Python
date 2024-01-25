Python 3.10.4

On GS_Api auth flow it is requested a credentials.json. This file cam be imported on OAuth dashboard of your 
google app.

    So your directory should be like this:
        /google_sheets
            .GS_Api.py
            .GS.py
            .credentials.json      <<<------ Note this

It is necessary have a google app and have a user access ( even as a tester). 
The google docs may be useful to you :
    https://cloud.google.com/apis/docs/getting-started?hl=pt-br
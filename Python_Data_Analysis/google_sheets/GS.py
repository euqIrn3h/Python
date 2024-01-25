from GS_Api import GS


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = 'SPREADSHEET_ID'
SHEET_NAME = 'SHEET_NAME'
RANGE = 'A0:Z1000'
DATA = {
    "majorDimension": "COLUMNS",
    "values": [
        ["Example",0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
        ["Example",0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    ]
}

def main():
    gs = GS(SCOPES)
    gs.auth()
    

    gs.buildService()

    values = gs.getSheet(SAMPLE_SPREADSHEET_ID, SHEET_NAME, RANGE)

    if not values:
        print('No data found.')
    else:
        print(values)

    gs.updateSheet(SAMPLE_SPREADSHEET_ID, SHEET_NAME, RANGE, DATA)



if __name__ == '__main__':
    main()
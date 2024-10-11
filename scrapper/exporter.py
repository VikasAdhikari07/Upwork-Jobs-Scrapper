import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

def google_sheet_transfer(jobs_worksheet):
    try:
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name(r"scrapper\\cred.json",scope)

        client = gspread.authorize(creds)

        sheet = client.open("Upwork Sheet").sheet1

        set_with_dataframe(worksheet=sheet, dataframe=jobs_worksheet, include_index=False,
        include_column_header=True, resize=True)
    except Exception as e:
        print(f"Error occur : {e}")
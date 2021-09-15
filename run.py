import gspread
from time import sleep
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("pet_experiment_data")

answers = SHEET.worksheet("Answers")

data = answers.get_all_values()

keys = [key for key in data[0]]
data.pop(0)
x = {key: [] for key in keys}
for answer_list in data:
    index = 0
    for answer in answer_list:
        x[keys[index]].append(answer)
        index += 1


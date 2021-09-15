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

user_answers = {}


def question_user(question):
    """
    Asks the user all the questions from the form
    """
    while True:
        if question == "Do your parents live together?":
            if user_answers["Do you have two parents?"] == "No":
                user_answers[question] = ""
                break
        elif question == "Are your sibling(s) older than you?":
            if user_answers["Do you have sibling(s)?"] == "No":
                user_answers[question] = ""
                break
        user_answer = input(f"{question} (Yes/No)\n")
        if validate_questions(user_answer):
            user_answers[question] = user_answer
            break


def validate_questions(value):
    """
    Validates the questions from question_user()
    """
    try:
        if value != "Yes" and value != "No":
            raise ValueError(
                f"You must answer with either Yes or No, you answered {value}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


print("Welcome to the Question Analyser!\n")
sleep(1)
print("You will be asked a few questions.")
print("After answering the questions,")
print("your answers will be compared to other peoples answers.")
sleep(2)
print("--------------------------------------------\n")
if input("Would you like to begin? (Yes/No)\n") != "Yes":
    exit()


for question in x:
    value = x[question]
    if question != "Tidstämpel":
        question_user(question)


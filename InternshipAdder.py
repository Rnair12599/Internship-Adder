import datetime
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

def printMen():
    print("If you want to add a new input, enter '1'")
    print("To output all internshps applied, enter '2'")
    val = int(input("Else '0': "))
    return val

def getDate():
    x = datetime.datetime.now()
    return x.strftime("%x")

def toGSheet(df):
    scope = ["https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("../APIcreds/InternshipAdder-DriveAPI-Cred.json", scope)
    #getting credentials from json credential file for google drive and google sheets

    client = gspread.authorize(creds)

    sheet = client.open("Summer2019_Internships").sheet1  # Open the spreadsheet

    fp = open("InternshipList.csv", "r")
    line = fp.readline()
    cnt = 0
    while line:
        currArr = line.split(",")
        cnt += 1
        for i in range(len(currArr)):
            sheet.update_cell(cnt,i+1, currArr[i])
        line = fp.readline()

    fp.close()

    """data = sheet.get_all_records()  # Get a list of all records

    row = sheet.row_values(3)  # Get a specific row
    col = sheet.col_values(3)  # Get a specific column
    cell = sheet.cell(1,2).value  # Get the value of a specific cell

    insertRow = ["hello", 5, "red", "blue"]
    sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4

    sheet.update_cell(2,2, "CHANGED")  # Update one cell

    numRows = sheet.row_count  # Get the number of rows in the sheet"""

#--------Start of MAIN PROGRAM-------------

df = pd.read_csv("InternshipList.csv")
print(df)


val = -1
Additions = []

while(val != 0):
    val = printMen()
    if(val == 1):
        temp = []
        temp.append(str(input("Enter Company Name: ")).capitalize())
        temp.append(str(input("Enter what type of internship: ")))
        sDate = str(input("Enter date applied or 't' for today: "))
        if(sDate == 't'):
            sDate = str(getDate())
        temp.append(sDate)
        temp.append(str(input("Enter the status of application: ")))
        temp.append(str(input("Enter stage currently at for application: ")))
        Additions.append(temp)

df2 = pd.DataFrame(Additions, columns = ['Company','Position','Date','Status','Stage'])
df = df.append(df2)
df.sort_values("Company", inplace = True)
df.to_csv("InternshipList.csv", index = False)

toGSheet(df)

import datetime

class InterApp:
    def __init__(self, company, type, date, status):
        self.company = company
        self.type = type
        self.date = date
        self.status = status

def printMen():
    print("If you want to add a new input, enter '1'")
    print("To output all internshps applied, enter '2'")
    val = int(input("Else '0': "))
    return val

def getDate():
    x = datetime.datetime.now()
    return x.strftime("%x")

#--------Start of MAIN PROGRAM-------------
f = open("InternshipList.txt", "r")

line = f.readline()


AllApp = []

while line:
    tempL = line.split(", ")
    sCom = str(tempL[0])
    sType = str(tempL[1])
    sDate = str(tempL[2])
    sStatus = str(tempL[len(tempL) - 1])
    apps = InterApp(sCom,sType,sDate,sStatus)
    AllApp.append(apps)
    line = f.readline()
f.close()

val = -1
while(val != 0):
    val = printMen()
    if(val == 1):
        sCom = str(input("Enter Company Name: "))
        sType = str(input("Enter what type of internship: "))
        sDate = str(input("Enter date applied or 't' for today: "))
        sStatus = str(input("Enter the status of application"))
        sStatus += "\n"
        if(sDate == 't'):
            sDate = str(getDate())
        Rec = InterApp(sCom,sType,sDate,sStatus)
        AllApp.append(Rec)


AllApp.sort(key = lambda x: x.company)

f = open("InternshipList.txt", "w")

for i in AllApp:
    f.write(i.company + ", ")
    f.write(i.type + ", ")
    f.write(i.date + ", ")
    f.write(i.status)

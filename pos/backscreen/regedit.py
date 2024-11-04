import os
def regedit():
    print("WalterOS POS Registry Editor")
    print("For syntax problems, please type 'help;'.")
    while True:
        x = input("POS/REGEDIT$ ")
        if x.endswith(';'):
            z = x.split(' ')
            if z[0].lower() == "write":
                with open(f"frontend/config/{z[1]}.config", 'w') as w:
                    y = z[2]
                    w.write(y[:-1])
                    print(y[:-1])
            elif z[0].lower() == "read":
                y = z[1]
                with open(f"frontend/config/{y[:-1]}.config", 'r') as r:
                    print(r.readline())
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
    with open(f"frontend/config/{key}.config", 'r') as r:
        return r.readline()
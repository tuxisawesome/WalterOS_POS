print("WalterOS POS Bootstrap")
with open("firstrun.txt","r") as frn:
    if frn.read() == "serv":
        print("[0] Server, [1] Frontscreen, [2] Backscreen?")
        x = input("[0->2] >>> ")
        if x == "0":
            import os
            print("python or python3? [0/1]")
            x = input("[0/1] >>> ")
            if x == "0":
                try:
                    os.system("cd server && python server.py")
                except:
                    pass
            elif x == "1":
                try:
                    os.system("cd server && python3 server.py")
                except:
                    pass
            else:
                print("!!! Unrecognised command, Halting....")
        elif x == "1":
            import os
            print("python or python3? [0/1]")
            x = input("[0/1] >>> ")
            if x == "0":
                try:
                    os.system("cd pos/backscreen/frontend && python main.py")
                except:
                    pass
            elif x == "1":
                try:
                    os.system("cd pos/backscreen/frontend && python3 main.py")
                except:
                    pass
            else:
                print("!!! Unrecognised command, Halting....")
        elif x == "2":
            import os
            print("python or python3? [0/1]")
            x = input("[0/1] >>> ")
            if x == "0":
                try:
                    os.system("cd pos/backscreen/ && python main.py")
                except:
                    pass
            elif x == "1":
                try:
                    os.system("cd pos/backscreen/ && python3 main.py")
                except:
                    pass
            else:
                print("!!! Unrecognised command, Halting....")
        else:
            print("!!! Unrecognised command, Halting....")
    else:
        print("[1] Frontscreen, [2] Backscreen?")
        x = input("[1/2] >>> ")
        if x == "1":
            import os
            print("python or python3? [0/1]")
            x = input("[0/1] >>> ")
            if x == "0":
                try:
                    os.system("cd pos/backscreen/frontend && python main.py")
                except:
                    pass
            elif x == "1":
                try:
                    os.system("cd pos/backscreen/frontend && python3 main.py")
                except:
                    pass
            else:
                print("!!! Unrecognised command, Halting....")
        elif x == "2":
            import os
            print("python or python3? [0/1]")
            x = input("[0/1] >>> ")
            if x == "0":
                try:
                    os.system("cd pos/backscreen/ && python main.py")
                except:
                    pass
            elif x == "1":
                try:
                    os.system("cd pos/backscreen/ && python3 main.py")
                except:
                    pass
            else:
                print("!!! Unrecognised command, Halting....")
        else:
            print("!!! Unrecognised command, Halting....")
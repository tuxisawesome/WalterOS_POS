import os

def clientsetup():
    print("")
    print("What is the IP of the server? [Leave blank for 127.0.0.1]")
    x = input(">>> ")
    with open(f"pos/backscreen/frontend/config/payproc.ip.config", 'w') as w:
        if x == "":
            w.write("127.0.0.1")
            print("127.0.0.1")
        else:
            w.write(x)
            print(x)
        w.close()
    print("")
    print("What is the port of the server? [Leave blank for 6543]")
    x = input(">>> ")
    with open(f"pos/backscreen/frontend/config/payproc.port.config", 'w') as w:
        if x == "":
            w.write("6543")
            print("6543")
        else:
            w.write(x)
            print(x)
        w.close()
    print("")
    print("Do you want to enable autologin? (Y/N) [Default is N]")
    x = input(">>> ")
    with open(f"pos/backscreen/frontend/config/users.autologin.config", 'w') as w:
        if x == "":
            w.write("false")
            print("false")
        elif x == "Y" or x == "y":
            w.write("true")
            print("true")
        else:
            w.write("false")
            print("false")

        w.close()
    if x == "y" or x == "Y":
        print("")
        print("Do you want an admin user? (Y/N) [Default is Y]")
        x = input(">>> ")
        if x == "n" or x == "N":
            print("")
            print("*   User creation skipped.")
            print("")
        else:
            print("")
            print("What is the admin username? [Leave blank for 'admin']")
            x = input(">>> ")
            with open(f"pos/backscreen/frontend/config/users.admin.uid.config", 'w') as w:
                if x == "":
                    w.write("admin")
                    print("admin")
                else:
                    w.write(x)
                    print(x)
                w.close()
            print("")
            print("What is the admin password? [Leave blank for 1234]")
            x = input(">>> ")
            with open(f"pos/backscreen/frontend/config/users.admin.pwd.config", 'w') as w:
                if x == "":
                    w.write("1234")
                    print("1234")
                else:
                    w.write(x)
                    print(x)
                w.close()
    else:
        print("")
        print("What is the admin username? [Leave blank for 'admin']")
        x = input(">>> ")
        with open(f"pos/backscreen/frontend/config/users.admin.uid.config", 'w') as w:
            if x == "":
                w.write("admin")
                print("admin")
            else:
                w.write(x)
                print(x)
            w.close()
        print("")
        print("What is the admin password? [Leave blank for 1234]")
        x = input(">>> ")
        with open(f"pos/backscreen/frontend/config/users.admin.pwd.config", 'w') as w:
            if x == "":
                w.write("1234")
                print("1234")
            else:
                w.write(x)
                print(x)
            w.close()
        
    print("")
    print("")
    print("Thank you for using WalterOS POS.")
    print("This setup has been completed.")
def serversetup():
    print("")
    print("Are you planing to also set up as a client?")
    x = input("[y/n] >>> ")
    if x == "y":
        clientsetup()
    with open(f"firstrun.txt", 'w') as fr:
        fr.write("serv")
    print("This part of setup is complete.")

def firstrun():
    print("")
    os.system("pip install flask")
    print("WalterOS POS Setup")
    print("Are you setting this computer up as a server or a client?")
    print("If both, select 'server'.")
    print("Type [S/s/Server] for server or [C/c/Client] for client.")
    x = input(">>> ")


    # Check if server or client
    if x == "server" or x == "s":
        serversetup()
    elif x == "client" or x == "c":
        os.rmdir("server")
        clientsetup()
    else:
        firstrun()

firstrun()
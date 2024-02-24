import os

def clientsetup():
    print("")
    print("What is the IP of the server? [Leave blank for 127.0.0.1]")
    x = input(">>> ")
    with open(f"frontend/config/payproc.ip.config", 'w') as w:
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
    with open(f"frontend/config/payproc.port.config", 'w') as w:
        if x == "":
            w.write("6543")
            print("6543")
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
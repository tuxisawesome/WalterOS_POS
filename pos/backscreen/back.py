

more = True
while more:
    cmd = input("POS$ ")
    if cmd == "payment":
        whatfor = input("What for? ")
        howmuch = input("How much? ")
        total = f"pay`{howmuch}`{whatfor}"
        with open('frontend/cmd_list.txt','a') as cmlist:
            cmlist.write(total)
            cmlist.close()
    elif cmd == "":
        continue
    elif cmd == "quit":
        exit()
    else:
        print("Commands: 'payment','quit'")
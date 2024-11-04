import os
from time import sleep
import regedit
def brand(clear=True):
    if clear:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        print("")
        print("╔═══════════════════════════════════════════╗")
        print("║__        __    _ _             ___  ____  ║")
        print("║\ \      / /_ _| | |_ ___ _ __ / _ \/ ___| ║")
        print("║ \ \ /\ / / _` | | __/ _ \ '__| | | \___ \ ║")
        print("║  \ V  V / (_| | | ||  __/ |  | |_| |___) |║")
        print("║   \_/\_/ \__,_|_|\__\___|_|   \___/|____/ ║")
        print("║ ____   ___  ____                          ║")
        print("║|  _ \ / _ \/ ___|                         ║")
        print("║| |_) | | | \___ \                         ║")
        print("║|  __/| |_| |___) |                        ║")
        print("║|_|    \___/|____/                         ║")
        print("╚═══════════════════════════════════════════╝")
        print("")
    else:
        print("")
        print("╔═══════════════════════════════════════════╗")
        print("║__        __    _ _             ___  ____  ║")
        print("║\ \      / /_ _| | |_ ___ _ __ / _ \/ ___| ║")
        print("║ \ \ /\ / / _` | | __/ _ \ '__| | | \___ \ ║")
        print("║  \ V  V / (_| | | ||  __/ |  | |_| |___) |║")
        print("║   \_/\_/ \__,_|_|\__\___|_|   \___/|____/ ║")
        print("║ ____   ___  ____                          ║")
        print("║|  _ \ / _ \/ ___|                         ║")
        print("║| |_) | | | \___ \                         ║")
        print("║|  __/| |_| |___) |                        ║")
        print("║|_|    \___/|____/                         ║")
        print("╚═══════════════════════════════════════════╝")
        print("")

def other_options():
    os.system("clear")
    brand()
    print("Other options menu:")
    print("1     - Exit menu")
    print("2/ANY - Quit guided mode")
    print("3     - Registry Editor")
    cmd = input("? ")
    if cmd == "1":
        return True
    elif cmd == "2":
        return False
    elif cmd == "3":
        regedit.regedit()
        return True



def guided_mode():
    global mores
    mores = True
    while mores:

        brand()
        uname = input("Swipe userid card: ")
        pwd = input("Pass 2 (press enter after): ")

        if uname == regedit.readkey("users.admin.uid"):
            if pwd == regedit.readkey("users.admin.pwd"):
                pass
            else:
                print("Card read error")
                input("Press enter to try again")
                continue
        else:
            print("Card read error")
            input("Press enter to try again")
            continue
        print("Please select: 0 [Other options] or anything else for new order")
        cmd = input("? ")
        if cmd == "O" or cmd == "0" or cmd == "o":
            x = other_options()
            if not x:
                break
            else:
                continue
        else:
            items = []
            prices = []
            total = 0.00
            cont = True
            while cont:
                try:
                    brand()
                    print("What do you want to do?")
                    print("1     - Add item")
                    print("2     - Delete item")
                    print("3/ANY - List items")
                    print("4     - List Customer Balance")
                    print("5     - Quit order")
                    print("6     - Checkout")
                    cmd2 = input("? ")
                    if cmd2 == "1":
                        brand()
                        print("Item name?")
                        cmd3 = input("? ")
                        brand()
                        print("Price?")
                        cmd4 = input("$ ")
                        brand()
                        print("")
                        print("----------------------------")
                        print("Item:")
                        print(f"{cmd3}     ${cmd4}")
                        print("----------------------------")
                        print("Are you sure you want to add? [Y/N] or nothing for [N]")
                        cmd5 = input("[Y/N]? ")
                        if cmd5 == "Y" or cmd5 == "y":
                            os.system("clear")
                            print("Added item.")
                            message = f"{cmd3}    +${cmd4}"
                            totalsx = f"debug`{message}\n"
                            with open('frontend/cmd_list.txt','a') as cmlist:
                                cmlist.write(totalsx)
                                cmlist.close()
                            items.append(cmd3)
                            prices.append(float(cmd4))
                            total = total + float(cmd4)
                            continue
                        else:
                            continue

                    elif cmd2 == "2":
                        brand()
                        print("Find the item you want to remove:")
                        for item in items:
                            print(f"#{items.index(item)}   {item}")
                        print("Enter the number of the item you want to remove:")
                        try:
                            x = input("? ")
                            os.system("clear")
                            message = f"{item}    -${prices[int(x)]}"
                            totalsx = f"debug`{message}\n"
                            with open('frontend/cmd_list.txt','a') as cmlist:
                                cmlist.write(totalsx)
                                cmlist.close()
                            total = total - prices[int(x)]
                            items.pop(int(x))
                            prices.pop(int(x))
                            print("Item removed.")
                        except:
                            brand()
                            print("Numbers Error")
                            sleep(2)
                        
                    elif cmd2 == "3" or cmd2 == "":
                        brand()
                        print("Items:")
                        print("-----------------------------------")
                        for item in items:
                            print(f"#{items.index(item)}   {item}")
                        print("-----------------------------------")
                        print(f"Total Price: {total}")
                        print("")
                        x = input("Press enter to continue... ")
                    elif cmd2 == "5":
                        os.system("clear")
                        break
                    elif cmd2 == "4":
                        brand()
                        totalsx = f"getbal`.\n"
                        with open('frontend/cmd_list.txt','a') as cmlist:
                            cmlist.write(totalsx)
                            cmlist.close()
                        print("Waiting 3 seconds to make sure execution is flushed...")
                        sleep(3)
                    elif cmd2 == "6":
                        brand()
                        print("Items:")
                        print("-----------------------------------")
                        for item in items:
                            print(f"#{items.index(item)}   {item}")
                        print("-----------------------------------")
                        print("Type Y or y to accept, or anything else to deny")
                        y = input("? ")
                        if y == "y" or y == "Y":
                            brand()
                            whatfor = "Listed Items"
                            howmuch = total
                            totals = f"pay`{howmuch}`{whatfor}\n"
                            with open('frontend/cmd_list.txt','a') as cmlist:
                                cmlist.write(totals)
                                cmlist.close()

                            with open('frontend/paymount','w') as pmount:
                                pmount.write(howmuch)
                                pmount.close()
                            print("Was checkout successful? Type N or n for no or anything for yes.")
                            z = input("? ")
                            if z == "N" or z == "n":
                                os.system("clear")
                                continue
                            else:
                                total = 0.00
                                items = []
                                prices = []
                                os.system("clear")
                                break
                except:
                    print("Error!")
                        
                        

                



def textmode():
    global more
    more = True
    print("WalterOS POS")
    print("Manual mode")
    print("Type 'guided' or '0' to enter automatic mode.")
    while more:
        cmd = input("POS$ ")
        if cmd == "guided" or cmd == "0":
            guided_mode()
        elif cmd == "payment":
            whatfor = input("What for? ")
            howmuch = input("How much? ")
            total = f"pay`{howmuch}`{whatfor}\n"
            with open('frontend/cmd_list.txt','a') as cmlist:
                cmlist.write(total)
                cmlist.close()
        elif cmd == "print":
            message = input("Message: ")
            total = f"debug`{message}\n"
            with open('frontend/cmd_list.txt','a') as cmlist:
                cmlist.write(total)
                cmlist.close()
        elif cmd == "regedit":
            regedit.regedit()
        elif cmd == "clear" or cmd == "cls":
            os.system("clear")
        elif cmd == "":
            continue
        elif cmd == "quit":
            exit()
        else:
            print("Commands: 'payment','quit','clear','print','regedit',guided/0'")



if __name__ == "__main__":
    textmode()
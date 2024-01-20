


def other_options():
    print("")
    print("Other options menu:")
    print("1 - Exit menu")
    print("2 - Quit guided mode")
    cmd = input("? ")
    if cmd == "1":
        return True
    elif cmd == "2":
        return False



def guided_mode():
    global mores
    mores = True
    while mores:
        print("Please select: O [Other options] or anything else for new order")
        cmd = input("? ")
        if cmd == "O" or cmd == "o":
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
                    #New order
                    print("What do you want to do?")
                    print("1     - Add item")
                    print("2     - Delete item")
                    print("3/ANY - List items")
                    print("4     - Quit order")
                    print("5     - Checkout")
                    cmd2 = input("? ")
                    if cmd2 == "1":
                        print("Item name?")
                        cmd3 = input("? ")
                        print("Price?")
                        cmd4 = input("$ ")
                        print("")
                        print("----------------------------")
                        print("Item:")
                        print(f"{cmd3}     ${cmd4}")
                        print("----------------------------")
                        print("Are you sure you want to add? [Y/N] or nothing for [N]")
                        cmd5 = input("[Y/N]? ")
                        if cmd5 == "Y" or cmd5 == "y":
                            print("Added item.")
                            message = f"{cmd3}    +${cmd4}"
                            totalsx = f"debug`{message}"
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
                        print("Find the item you want to remove:")
                        for item in items:
                            print(f"#{items.index(item)}   {item}")
                        print("Enter the number of the item you want to remove:")
                        try:
                            x = input("? ")
                            message = f"{item}    -${prices[int(x)]}"
                            totalsx = f"debug`{message}"
                            with open('frontend/cmd_list.txt','a') as cmlist:
                                cmlist.write(totalsx)
                                cmlist.close()
                            total = total - prices[int(x)]
                            items.pop(int(x))
                            prices.pop(int(x))
                            print("Item removed.")
                        except:
                            print("Numbers Error")
                        
                    elif cmd2 == "3" or cmd2 == "":
                        print("")
                        print("Items:")
                        print("-----------------------------------")
                        for item in items:
                            print(f"#{items.index(item)}   {item}")
                        print("-----------------------------------")
                        print(f"Total Price: {total}")
                    elif cmd2 == "4":
                        break
                    elif cmd2 == "5":
                        print("")
                        print("Items:")
                        print("-----------------------------------")
                        for item in items:
                            print(f"#{items.index(item)}   {item}")
                        print("-----------------------------------")
                        print("Type Y or y to accept, or anything else to deny")
                        y = input("? ")
                        if y == "y" or y == "Y":
                            whatfor = "Listed Items"
                            howmuch = total
                            totals = f"pay`{howmuch}`{whatfor}"
                            with open('frontend/cmd_list.txt','a') as cmlist:
                                cmlist.write(totals)
                                cmlist.close()
                            print("Was checkout successful? Type N or n for no or anything for yes.")
                            z = input("? ")
                            if z == "N" or z == "n":
                                continue
                            else:
                                total = 0.00
                                items = []
                                prices = []
                                break
                except:
                    print("Error!")
                        
                        

                




more = True
print("WalterOS POS Control")
print("Manual mode")
print("Type 'guided' to enter automatic mode.")
while more:
    cmd = input("POS$ ")
    if cmd == "guided":
        guided_mode()
    elif cmd == "payment":
        whatfor = input("What for? ")
        howmuch = input("How much? ")
        total = f"pay`{howmuch}`{whatfor}"
        with open('frontend/cmd_list.txt','a') as cmlist:
            cmlist.write(total)
            cmlist.close()
    if cmd == "print":
        message = input("Message: ")
        total = f"debug`{message}"
        with open('frontend/cmd_list.txt','a') as cmlist:
            cmlist.write(total)
            cmlist.close()
    elif cmd == "":
        continue
    elif cmd == "quit":
        exit()
    else:
        print("Commands: 'payment','quit'")
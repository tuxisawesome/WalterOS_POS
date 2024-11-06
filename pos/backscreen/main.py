import back
import regedit
import sys

print("WalterOS POS")
print("*   Running registry verification")
x = regedit.regverify()
if x != "ok":
    print(x)
    y = input("Would you like to open regedit [Y/N]? ")
    if y == "Y" or y == "y":
        regedit.regedit()
    print("!!! Exiting...")
    sys.exit(1)


if regedit.readkey("system.defaultmode") == "text" :
    back.textmode()
else:
    back.guided_mode()


import back
import regedit

if regedit.readkey("system.defaultmode") == "text" :
    back.textmode()
else:
    back.guided_mode()


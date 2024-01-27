import requests
from dbg import p

def getremoteip():
    ppip = ""
    ppp = ""
    with open("config/payproc.ip.config", "r") as ppipc:
        ppip = ppipc.readlines()[0]
        ppipc.close()
    with open("config/payproc.port.config", "r") as pppc:
        ppp = pppc.readlines()[0]
        pppc.close()
    return [ppip,ppp]

def processpay(pwd,amount):
    pp = getremoteip()
    ppp = pp[1]
    ppip = pp[0]
    p(f"[{ppip},{ppp}]")
    subt = requests.get(f"http://{ppip}:{ppp}/api/sub/{pwd}/{amount}").text
    p(subt)
    p(f'{requests.get(f"http://{ppip}:{ppp}/api/bal/{pwd}").text}')
    return subt



def getbal(pwd):
    pp = getremoteip()
    ppp = pp[1]
    ppip = pp[0]
    p(f"[{ppip},{ppp}]")
    # Get bal
    return requests.get(f"http://{ppip}:{ppp}/api/bal/{pwd}").text

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, send_file
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# pay`30`potatos
def getbal(key):
    keys = []
    bals = []
    with open("keys.config", 'r') as keyx:
        keys = keyx.readlines()
        keyx.close()
    with open("bals.config", 'r') as balx:
        bals = balx.readlines()
    try:
        keydex = keys.index(key)
    except:
        return str("null")
    final = bals[keydex]
    return str(final)


def getname(key):
    keys = []
    bals = []
    with open("keys.config", 'r') as keyx:
        keys = keyx.readlines()
        keyx.close()
    with open("name.config", 'r') as balx:
        bals = balx.readlines()
    try:
        keydex = keys.index(key)
    except:
        return str("null")
    final = bals[keydex]
    return "Welcome, " + str(final)
# pay`30`potatos
def subbal(key,amnt):
    keys = []
    bals = []
    with open("keys.config", 'r') as keyx:
        keys = keyx.readlines()
        keyx.close()
    with open("bals.config", 'r') as balx:
        bals = balx.readlines()
    keydex = keys.index(key)
    newbal = float(bals[keydex]) - float(amnt)
    if newbal < 0:
        return str("True")
    bals[keydex] = newbal
    with open("bals.config", 'w') as baly:
        for line in bals:
            baly.write(f"{line}\n")
        baly.close()
    
    return str("True")

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def main():
    return render_template("main.html")

@app.route('/acct')
def acct():
    return render_template("acct.html")

@app.route('/acct-bal')
def acct_bal():
    return render_template("acct-bal.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/logout')
def logout():
    return render_template("logout.html")


@app.route('/api/bal/<key>')

def bal(key):
    x = getbal(key)
    return x

@app.route('/api/name/<key>')

def name(key):
    x = getname(key)
    return x

@app.route('/api/sub/<key>/')
def brokensub2(key):
    return "True"


@app.route('/api/sub/<key>/<amnt>')

def sub(key,amnt):
    if amnt == "":
        return "True"
    try:
        x = subbal(key,amnt)
    except:
        return "True"
    return x

@app.route('/api/sub/<key>')
def brokensub(key):
    return "True"

@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')
# main driver function
if __name__ == '__main__':
	# run() method of Flask class runs the application 
	# on the local development server.
    app.run(host='0.0.0.0',port=6543,debug=False)
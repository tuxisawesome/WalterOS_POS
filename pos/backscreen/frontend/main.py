# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request




#       SETTINGS






# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/api/payment', methods=['POST']) 
def read_form(): 
  
    # Get the form data as Python ImmutableDict datatype  
    data = request.form 
  
    ## Return the extracted information  
    if data['userPassword'] == "123123":
        #purchasesuccess
        with open('cmd_list.txt','w') as eee:
            eee.write("")
            eee.close()
        return render_template('purchasecomplete.html')
    else:
        return render_template('purchasefailed.html')







# pay`30`potatos

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():

    shopname = "WalterOS POS"
    shopdesc = "Most advanced POS Ever!"















    with open('cmd_list.txt','r') as cmdfile:
         global cmd_list
         cmd_list = cmdfile.readlines()
         cmdfile.close()
    if cmd_list == []:
          return render_template('home.html',shopname=shopname,shopdesc=shopdesc)
    else:
          for cmd in cmd_list:
            if cmd.split('`')[0] == "debug":
                with open('cmd_list.txt', 'r') as fin:
                    data = fin.read().splitlines(True)
                with open('cmd_list.txt', 'w') as fout:
                    fout.writelines(data[1:])
                return render_template('debug.html',message=cmd.split('`')[1])
            elif cmd.split('`')[0] == "pay":
                with open('cmd_list.txt', 'r') as fin:
                    data = fin.read().splitlines(True)
                with open('cmd_list.txt', 'w') as fout:
                    fout.writelines(data[1:])
                return render_template('pay.html',cost=cmd.split('`')[1],whatfor=cmd.split('`')[2])
            else:
                return render_template('error.html',cmd_list=cmd_list)
	

# main driver function
if __name__ == '__main__':
	# run() method of Flask class runs the application 
	# on the local development server.
    app.run(host='0.0.0.0',port=5432,debug=False)
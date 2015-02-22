import smtplib
from flask import render_template
from flask import Flask
from app import app


@app.route("/sendemail", methods=['GET', 'POST'])
def sendemail():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    return "<html> <head><title> Sam</title> </head> <body> <p> %s,  %s</p> </body </html> " % (name, message)
  return "Hi"
  
  
app.run(debug=True,host="0.0.0.0",port=8080)

"""fromaddr = 'samorae101@gmail.com'

toaddr = 'samorae101@gmail.com'

#message = {"fromname": fromname, "fromaddr": fromaddr}

fromname= "Sam"
toname = "Sasha"
subject = "Hi"
msg = 'Just checking,  just finished this part of the code'
msg2 = "Hi"



message = """#From:  %r  <%r>

#To: %r <%r> 

#Subject: %r


#%r
 

""" % (fromname, fromaddr, toname, toaddr, subject, msg)

messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = 'samorae101@gmail.com'

password = 'sunshinemkc'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

print "done!"

server.quit()   """
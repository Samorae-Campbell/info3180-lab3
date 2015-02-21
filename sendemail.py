import smtplib

fromaddr = 'samorae101@gmail.com'

toaddr = 'samorae101@gmail.com'

#message = {"fromname": fromname, "fromaddr": fromaddr}

fromname= "Sam"
toname = "Sasha"
subject = "Hi"
msg = 'Just checking,  just finished this part of the code'
msg2 = "Hi"



message = """From:  %r  <%r>

To: %r <%r> 

Subject: %r


%r
 

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

server.quit()
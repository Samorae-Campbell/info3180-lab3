"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import smtplib
from app import app
from flask import render_template, request, redirect, url_for


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route("/sendemail", methods=['GET', 'POST'])
def sendemail():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    subject = str(request.form['subject'])
    user_message = request.form['message']
    fromaddr = email
    toaddr = 'samorae101@gmail.com'

    #message = {"fromname": fromname, "fromaddr": fromaddr}

    fromname= str(name)
    toname = "Samorae"
    #subject = 
    msg = str(user_message)
     #msg2 = "Hi"



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

    print "Message sent - %s, %s, %s, %s" % (name, email, subject, user_message)

    server.quit()
    return "<div> <h1> Your email has been sent <i>%s</i>, Thank you </h1></div>" % name
  return "Hi"

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")

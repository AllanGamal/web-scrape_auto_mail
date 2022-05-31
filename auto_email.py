# function that accepts gmail username and password and send a mail to an email adress
def send_mail(username, password, to_email, subject, body):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # create message object instance
    msg = MIMEMultipart()
    # setup the parameters of the message
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject
    # add in the message body
    msg.attach(MIMEText(body, 'plain'))
    # create server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(username, password)
    # send the message via the server
    server.sendmail(username, to_email, msg.as_string())
    server.close()
#send_mail('username', 'password', 'to_email', 'subject', 'This is a test')

# function that checks a website for a specific class of html tag
def check_html_tag(url, element, tag, tag_value):
    import requests
    from bs4 import BeautifulSoup
    # get the html
    html = requests.get(url)
    # parse the html
    soup = BeautifulSoup(html.text, 'html.parser')
    # find the tag
    tag = soup.find(element, {tag: tag_value})
    # return the tag
    return tag
tag_string = check_html_tag('url', 'element', 'tag', 'value')

# function that check if a string include a specific word
def check_string(string, word):
    x = bool(0)
    if word in str(string):
        x = bool(1)
    return x
bool_qty = check_string(tag_string, '"Qty":1')

# function that sends a mail if the quantity is 1
def send_mail_if_bool(booly):
    if booly == 1:
        send_mail('username@gmail.com', 'password', 'send_to@gmail.com', 'subject', 'body')


# function that repeats to check the html tag every x hours
def repeat_every(hours):
    import time
    while True:
        send_mail_if_bool(bool_qty) # check the html tag and send a mail if the quantity is 1
        if bool_qty == 1: # if the quantity is 1, add 0.5 hours to the time
            hours += 0.5
        time.sleep(3600 * hours) # repeat every x hours
repeat_every(0.5)

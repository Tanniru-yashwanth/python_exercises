from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_contacts(filename):
    names = []
    mails = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for a in file:
            names.append(a.split(" ")[0])
            mails.append(a.split(" ")[1])
    return names, mails


def read_template(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        template_file_content = file.read()
    return template_file_content


s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login('tanniruyashwanth07@gmail.com', 'Tanniru@8535')

names, mails = get_contacts('contacts.txt')
message = read_template('message.txt')


for name, mail in zip(names, mails):
    msg = MIMEMultipart()
    msg['From'] = 'tanniruyashwanth07@gmail.com'
    msg['To'] = mail
    msg['subject'] = "This is the test"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)

    del msg

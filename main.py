import time
import os
import random
import smtplib
from email.message import EmailMessage

def email_alert(content, to):
  msg = EmailMessage()
  msg.set_content(content)
  msg['to'] = to

  user = "Email@gmail.com"
  msg['from'] = user
  password = "AppPassword"

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(user, password)

  with open('img.jpg', 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='application', subtype='jpg', filename='img.jpg')

  server.send_message(msg)

  server.quit()

users = ["Email"]

while True:
  time.sleep(0.25)
  print("sent to: ", random.choice(users))
  email_alert("Message", random.choice(users))

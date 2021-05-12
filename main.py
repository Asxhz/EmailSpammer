import time
import os
import random
import smtplib
from email.message import EmailMessage

amount = input('How many messages to send (enter loop to send infinite): ')
addimage = input('Would you like to add an image? (yes/no) If you choose to add an image, You need to have a file in this directory named img.jpg: ')
emails = input('Please enter the email you would like to spam: ')
message = input('Please enter the message content: ')

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
  
  if addimage=='yes'|'y':
    with open('img.jpg', 'rb') as content_file:
      content = content_file.read()
      msg.add_attachment(content, maintype='application', subtype='jpg', filename='img.jpg')

  server.send_message(msg)

  server.quit()

users = ["Email"]

if amount=='loop'|null|'':
  print('you either typed loop or left the message count number blank, or typed an invalid answer. Sending infinite messages.')
  while True:
    time.sleep(0.25)
    print("sent to: ", emails)
    email_alert(message, emails)
else:
  while i > amount:
    time.sleep(0.25)
    print("sent to: ", emails)
    email_alert(message, emails)


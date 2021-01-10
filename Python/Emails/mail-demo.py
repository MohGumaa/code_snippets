
import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'YourAddress@gmail.com'

# Here to send to multiple person
# msg['To'] = contacts
# msg['To'] = ', '.join(contacts)

# files = ['img1.png', 'img2.png', 'img12.png']

# msg.set_content('image attachment')
# for file in files:
#     with open(file, 'rb') as f:
#         file_date = f.read()

#         # Here will determine type of img only for image for other type no need
#         file_type = imghdr.what(f.name)
#         file_name = f.name

#     # this for send image other type we need to change maintype='application', subtype=octet-stream
#     msg.add_attachment(file_date, maintype='image', subtype=file_type, filename=file_name)

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

# Using smtp_ssl better than smtp bcz no need ehlo and starlls
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

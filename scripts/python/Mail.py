# Send Mail from Python
# Below is an example of sending an otp for registering in a Website

import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from random import randint
import time

host = "smtp.gmail.com"
port = 587
username = "xxxxxxxxxx@gmail.com"
password = "XXXXXXXX"
from_email = username

class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """Hi {name}! 
Thank you for the signing up on xyz.com.
Use otp {otp} to confirm your account.
We hope you are exicted about using it.
Have a great day!
{date}
Team XYZ
"""
    def generate_otp(self,email):
        otp=randint(1000,9999)
        print(otp)
        return(str(email[0:3])+str(otp))
    
    def add_user(self, name, email=None):
        name = name[0].upper() + name[1:].lower() 
        detail = {
            "name": name,
        } 
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail["email"] = email
            detail["otp"]=self.generate_otp(email)
            
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                date = detail["date"]
                otp  = detail["otp"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    otp=otp
                )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []
    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                user_message = detail['message']
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Confirmation Mail"
                    the_msg["From"] = from_email
                    the_msg["To"]  = user_email
                    part_1 = MIMEText(user_message, 'plain')
                    the_msg.attach(part_1)
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print("error sending message")
            return True
        return False


obj = MessageUser()
obj.add_user("YYY", email='yyy@gmail.com')
obj.get_details()

obj.send_email()

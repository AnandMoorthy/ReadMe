""" Email Handler """
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

base_url = "http://127.0.0.1:8000/api/v0.0.1/user"

# html = """\
#     <html>
#         <head>
#         </head>
#         <body>
#             <h3>This is link</h3>
#             <p>http://localhost/phpmyadmin</p>
#         </body>
#     </html>
#     """
# name = "Anand Moorthy"
# subject = "verification"
# to_addr_list = ['anand@kabadiwallaconnect.in']

def send_email(name, subject, html, to_addr_list):
    """ To send email verification"""
    msg = MIMEMultipart()
    msg['From'] = "ReadMe App"
    msg['To'] = ", ".join(to_addr_list)
    msg['Subject'] = subject
    msg.attach(MIMEText(html, 'html'))
    mail_ack = False
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587) #check smtp service and port
        server.starttls()#start smtp
        server.login('janandhamoorthy@gmail.com', "blackpepper12#)")#login gmail
        text = msg.as_string()
        server.sendmail('ReadMe App', to_addr_list, text)
        server.quit()
        mail_ack = True
    except Exception as e:
        print e
        mail_ack = False
    return mail_ack

def send_signup_email(email, name, token):
    """ Module to send signup email """
    url = base_url+"/verify/email?token=%s"%token
    subject = "Email Verification"
    html = """
            <html>
                <head>
                </head>
                <body>
                    <h3>
                        Signup Email
                    </h3>
                    <p>%s</p>
                </body>
            </html
            """%(url)
    to_addr = [email]
    ack = send_email(name, subject, html, to_addr)
    return ack

def send_forgot_password_email(email, name, token):
    """ Send Email to change password """
    html = """
            <html>
                <head>
                </head>
                <body>
                    <h3>Forgot Password Link</h3>
                    <p>%s</p>
                </body>
            </html>
            """%(token)
    to_list = [email]
    subject = "Reset Password"
    email_ack = send_email(name, subject, html, to_list)
    return email_ack

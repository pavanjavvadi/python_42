import smtplib

sender_mail = "pavan.javvadi04@gmail.com"
rec_mail = 'rukminijavvadi13@gmail.com'
password = 'Aj14PYlgm'
message = "sample mesage"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_mail,password)
print("login success")
server.sendmail(sender_mail,rec_mail,message)
print('email sent')
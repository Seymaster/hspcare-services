import smtplib,ssl

port = 465 
smtp_server = "smtp.gmail.com"
sender_email = "myers12919@gmail.com"
password = "English2018"
receiver_email = "alugbinoluwaseyi1@gmail.com"
mesbody = "How are you doing"
message = f"Subject : Hello  \n\n  {mesbody}"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)
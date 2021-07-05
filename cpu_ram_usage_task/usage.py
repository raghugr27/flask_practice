import csv
import os
import smtplib
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

now = datetime.now()
with open("input.csv", "r") as f:
    r = csv.reader(f)
    for i in r:
        cpu_usage = os.popen(
            "ssh {}@{} {}".format(
                i[0], i[1], "top -b -n1 | grep \"Cpu(s)\" | awk '{print $2 + $4}'"
            )
        )
        ram_usage = os.popen(
            "ssh {}@{} {}".format(
                i[0], i[1], "free -t | awk 'FNR == 2 {print $3/$2*100}'"
            )
        )
        lst = [
            i[0],
            (i[1]),
            cpu_usage.read().rstrip("\n"),
            ram_usage.read().rstrip("\n"),
            now.strftime("%m:%d:%Y:%H:%M:%S"),
        ]
        fields = ["hostname", "ip_address", "cpu_usage", "ram_usage", "time stamp"]
with open("record.csv", "w") as c1:
    csvwriter = csv.writer(c1)
    csvwriter.writerow(fields)
    csvwriter.writerow(lst)

fromaddr = "raghutheperfect@gmail.com"
toaddr = "raghutheperfect@gmail.com"
# instance of MIMEMultipart
msg = MIMEMultipart()

msg["From"] = fromaddr

# storing the receivers email address
msg["To"] = toaddr

# storing the subject
msg["Subject"] = "csv file"

# string to store the body of the mail
body = "hi this is raghu"

# attach the body with the msg instance
msg.attach(MIMEText(body, "plain"))

# open the file to be sent
filename = "record.csv"
attachment = open("record.csv", "rb")

# instance of MIMEBase and named as p
p = MIMEBase("application", "octet-stream")

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)

p.add_header("Content-Disposition", "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP("smtp.gmail.com", 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "$RamVij@6399$")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()

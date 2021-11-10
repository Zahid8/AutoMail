import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def read_template(filename):
 with open(filename, "r", encoding="utf-8") as template_file:
  template_file_content = template_file.read()
 return Template(template_file_content)
def main():
 message_template = read_template("template.txt")
 MY_ADDRESS = "xxxxxx@xxxx.com"
 PASSWORD = "xxxxxxxx"
 s = smtplib.SMTP(host="smtp.gmail.com", port=587)
 s.starttls()
 s.login(MY_ADDRESS, PASSWORD)
 
 with open("test_mail.csv", "r") as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")
  next(csv_reader)
  for row in csv_reader:
   msg = MIMEMultipart() 
   message = message_template.substitute(company_name=row[0])
   print(message)
   msg["From"]=MY_ADDRESS
   msg["To"]=row[1]
   msg["Subject"]="test_mail"
   msg.attach(MIMEText(message, "plain"))
   s.send_message(msg)
   del msg
 s.quit()
if __name__ == "__main__":
 main()

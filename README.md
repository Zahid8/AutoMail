# AutoMail
Automated mail sending script based on python

As the python script will access the Gmail account the send out emails, we need to turn Allow less secure apps to ON in that account. This makes it easier for others to gain access to your account.

###Template.txt file
This text file contains the format for the email body. The personal details from the details.csv file are each placed in the placeholder defined by ‘${}’ in this text file.

###test_mail.csv file
The test_mail.csv file contains the details that must populate the placeholders in the template file. It contains the details that must be sent to the recipients.it can be an excel file or CSV file.

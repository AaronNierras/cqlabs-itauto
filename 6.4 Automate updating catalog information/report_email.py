#!/usr/bin/env python3

import os
import datetime

from run import get_desc
import reports
import emails


# info
src = "./supplier-data/descriptions/"
attachment = "/tmp/processed.pdf"
current_time = datetime.datetime.now().strftime("%B %d, %Y")
title = "Processed Update on {}".format(current_time)
paragraph = get_desc(src)

if __name__ == "__main__":
    # Generate the PDF report
    reports.generate_report(attachment, title, paragraph)
    # Send the email with the PDF report attached
    From = "automation@example.com"
    To = "student@example.com"
    Subject = "Upload Completed - Online Fruit Store"
    Body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(From, To, Subject, Body, attachment)
    emails.send_email(message)

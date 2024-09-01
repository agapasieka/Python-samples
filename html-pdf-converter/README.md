# Manual execution: 

Install python external package: pyhtml2pdf 

```
pip install pyhtml2pdf
```

Run the script: html-pdf-converter.py

```
python3 html-pdf-converter.py
```

# Run worklflow and email the file converted to pdf 
<!-- Overview -->
Explanation

1. Install dependencies:

* Installs pyhtml2pdf for converting HTML to PDF and yagmail for sending emails with attachments.

2. Convert HTML to PDF and Send Email:

* Runs a Python script inline to:
 * Convert a webpage (https://example.com) to a PDF and save it as cv.pdf.
 * Use yagmail to send an email with cv.pdf as an attachment.

3. Email Settings:

* sender_email: The sender's email address (stored in the EMAIL_ADDRESS secret).
* receiver_email: The recipient's email address. You should replace 'recipient@example.com' with the actual recipient's email.
* subject: The email subject line.
* body: The email body content.

4. Secrets:

EMAIL_ADDRESS and EMAIL_PASSWORD are secrets stored in your GitHub repository. The EMAIL_PASSWORD can be an App Password if you're using Gmail with 2-Step Verification enabled.

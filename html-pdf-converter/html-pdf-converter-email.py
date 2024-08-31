import yagmail
from pyhtml2pdf import converter

# Convert HTML to PDF
converter.convert('https://agapasieka.github.io/resume/', 'agnieszka-pasieka-cv.pdf')

# Email settings
sender_email = '${{ secrets.EMAIL_ADDRESS }}'
receiver_email = 'agipasieka79"gmail.com' 
subject = 'Your updated CV in PDF'
body = 'Please find attached your CV in PDF format.'

# Send the email with the attachment
yag = yagmail.SMTP(sender_email, '${{ secrets.EMAIL_PASSWORD }}')
yag.send(
    to=receiver_email,
    subject=subject,
    contents=body,
    attachments='agnieszka-pasieka-cv.pdf'
)

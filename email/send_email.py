import os
import smtplib
from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Load environment variables
load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVERS = os.getenv("EMAIL_RECEIVERS").split(",")

# HTML Report Path
REPORT_PATH = "reports/report.html"

# Create Email
message = MIMEMultipart()

message["From"] = EMAIL_SENDER
message["To"] = ", ".join(EMAIL_RECEIVERS)
message["Subject"] = "Playwright Automation HTML Report"

# Email Body
body = """
Hello Team,

Please find the attached Playwright Automation HTML Report.

Regards,
Playwright Automation Framework
"""

message.attach(MIMEText(body, "plain"))

# Attach HTML Report
try:
    with open(REPORT_PATH, "rb") as attachment:

        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename={os.path.basename(REPORT_PATH)}"
    )

    message.attach(part)

except FileNotFoundError:
    print("❌ HTML Report not found!")
    exit()

# Send Email
try:

    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(
            EMAIL_SENDER,
            EMAIL_PASSWORD
        )

        server.sendmail(
            EMAIL_SENDER,
            EMAIL_RECEIVERS,
            message.as_string()
        )

    print("✅ Email sent successfully!")

except Exception as e:
    print(f"❌ Failed to send email: {e}")
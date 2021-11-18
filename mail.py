import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "comp.workshop@cusat.ac.in"

password = 'abc'

context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
server.login(sender_email, password)

receiver_email = "tprohit9@gmail.com"
body = f'''
<p><strong>Dear rohit,</strong></p>

<p>Greetings from the&nbsp;Department of Applied Chemistry, Cochin University of Science and Technology!.We welcome you to the virtual workshop on &#39;Computational Modeling in Chemistry, Biology and.Materials- making it mainstream&rsquo; from Nov 22nd -28th, 2021.Below are some of the technical information/instructions regarding the Workshop. We recommend you go&nbsp;through every instruction carefully.</p>

<ol>
	<li>&nbsp;All the lectures will be held on the Zoom platform. The meeting ID and passcode will be sent to&nbsp;the registered e-mail Id. Please note to sign in using the registered e-mail Id only.</li>
	<li>&nbsp;Make sure you have installed the latest version of ZOOM (recommended). Or if you are planning&nbsp;&nbsp;use a web browser, then make sure you are using the latest version of Chrome/Firefox.</li>
	<li>&nbsp;You should have a Windows/Linux based laptop or desktop for participating in the tutorial sessions.</li>
	<li>&nbsp;Kindly see the website for the programme schedule.</li>
	<li>&nbsp;Please join the WhatsApp group by clicking the link below for future updates.<a href="https://chat.whatsapp.com/KBwg2XZg7iA1EBP7kdshk7" rel="noreferrer" target="_blank">&nbsp;https://chat.whatsapp.com/KBwg2XZg7iA1EBP7kdshk7</a></li>
	<li>&nbsp;Download link and password for the software package required will be sent to your registered email id. The participants will be given free access to the softwares for the workshop.</li>
</ol>

<p>Kindly see the website for further updates.&nbsp;<a href="https://sites.google.com/cusat.ac.in/workshop/home" rel="noreferrer" target="_blank">https://sites.google.com/cusat.ac.in/workshop/home</a></p>

<p>If you have any queries, please do not hesitate to contact us. Looking forward to seeing you on Day-1 of&nbsp;the workshop</p>
'''

filename = "certificate.pdf"
message = MIMEMultipart()

attachment = open(filename, "rb")
# Add file as application/octet-stream
# Email client can usually download this automatically as attachment
part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())

message["Subject"] = 'testing mail'
message["From"] = sender_email
message["To"] = receiver_email

message.attach(MIMEText(body, "html"))

encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Log in to server using secure context and send email

# message.attach(part)
text = message.as_string()
server.ehlo()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, text)
server.close()

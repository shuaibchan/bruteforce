import pycrack
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

hash_ = "86775fe0718f57c5bcc3c32c198ece3e6a732406e3f32e3aa285059247da6652"
charset = pycrack.get_charset("L")# utk lowercse (L) lowercse & uppercase (LU) & lowercase uppercase digit (LUD)
min_length = 6
max_length = 6
algo = pycrack.get_algorithm("sha256")

print("\n"*80)
r = pycrack.bruteforce(hash_, charset, min_length, max_length, algo, True)


if r is None:
    print("No matches.")
else:
    print(f"Match: {'wgmy{h3r3_1s_y0ur_'}{r}{'_br0!}'}")


fromaddr = "yyshu18@gmail.com"
toaddr = "yyshu18@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Match: wgmy{h3r3_1s_y0ur_"+r+"_br0!"
 
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "YOUR PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

input("Press enter to exit ;)")
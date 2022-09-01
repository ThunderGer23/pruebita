from fastapi import APIRouter
import random
import string
import smtplib
from routes.apis_net_pe import ApisNetPe

dni = APIRouter()
peapi = ApisNetPe()

@dni.get('/dates')
def get_info(DNI: str):
    person = peapi.get_person(DNI)
    return person

@dni.get('/token')
def get_token(email: str):
    print(email)
    str = string.ascii_lowercase+"1234567890"
    token = ''.join(random.choice(str) for i in range(50))

    credentials = {"email": "proculturamx98@gmail.com",
                   "password": "2012010273.Well"}

    conect = smtplib.SMTP(host='smtp.gmail.com', port=587)
    conect.ehlo()

    conect.starttls()
    conect.login(user=credentials["email"], password=credentials["password"])
    message = "Subject: Token for login in stdl\n"+token
    conect.sendmail(from_addr=credentials["email"], to_addrs=email, msg=message)
    conect.quit()
    return {token}
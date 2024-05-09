import requests
import smtplib
from creds import *

URL_WEB = 'https://waw-cinema-assistant-mtfo73rvoa-lm.a.run.app/final'


def html(url):
    response = requests.get(url)
    return response.status_code


def send_mail(status):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=SENDER, password=PASSWORD)
        connection.sendmail(from_addr=SENDER,to_addrs=ADDRESS,
                            msg=f"In waw-cinema-assistant there is an error number {status}")


def what_does_code_mean(url):
    respond = html(url)
    if respond != 200:
        send_mail(respond)
    else:
        pass


what_does_code_mean(URL_WEB)


import requests
import smtplib
from creds import *
URL_WEB = 'https://waw-cinema-assistant-mtfo73rvoa-lm.a.run.app/final'


def make_request(url):
    response = requests.get(url)
    return response.status_code


def send_mail(response_code):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=SENDER, password=PASSWORD)
        connection.sendmail(from_addr=SENDER,to_addrs=ADDRESS,
                            msg=f"In waw-cinema-assistant there is an error number {response_code}")


def if_problem_send_mail(url):
    response_code = make_request(url)
    if response_code != 200:
        send_mail(response_code)
    else:
        pass


if_problem_send_mail(URL_WEB)
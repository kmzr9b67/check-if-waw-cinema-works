from concurrent.futures.thread import ThreadPoolExecutor
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from creds import *
import time

URL_WEB = 'https://waw-cinema-assistant-mtfo73rvoa-lm.a.run.app/'
LISTA = ['TODAY', 'TOMORROW', 'DAY AFTER TOMORROW']

def make_driver():
    option = Options()
    option.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=option)
    return browser


def web_check(lista):
    browser = make_driver()
    browser.get(URL_WEB)
    element = browser.find_element(By.ID, 'input')
    down = Select(element)
    down.select_by_visible_text(lista)
    time.sleep(2)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.send_keys(Keys.ENTER)
    return browser.find_element(By.TAG_NAME, 'h1').text


def make_request(url):
    with ThreadPoolExecutor(len(LISTA)) as executor:
        for result in executor.map(web_check, LISTA):
            if result != 'Movie recommendations in Warsaw':
                send_mail(result)


def send_mail(day):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=SENDER, password=PASSWORD)
        connection.sendmail(from_addr=SENDER, to_addrs=ADDRESS,
                            msg=f"In waw-cinema-assistant there is an error in sheet: {day}")


make_request(URL_WEB)
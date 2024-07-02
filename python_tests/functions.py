import datetime
import allure
import imaplib
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from random import randint
from selenium.webdriver.common.keys import Keys
import urllib
import urllib.request
import json
import requests
import codecs
from bs4 import BeautifulSoup as bs

import os, glob
import xlrd

print(os.getcwd())
d = {'User-Agent': 'QA-TEST-200-sdgsgsdgsggsgsdgsdgdgs'}

class Screenshots:
    def __init__(self):
        pass

    def screenshot(screen_name, browser_type):
        today = datetime.datetime.today()
        at_the_moment = str(today.strftime("%Y-%m-%d-%H.%M.%S"))
        browser_type.save_screenshot('./results/screens/' + at_the_moment + '.png')
        allure.attach.file('./results/screens/' + at_the_moment + '.png', screen_name,
                           attachment_type=allure.attachment_type.PNG)


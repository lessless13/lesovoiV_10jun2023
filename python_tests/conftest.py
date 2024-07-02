
import pytest
from selenium import webdriver
import allure
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from python_tests.functions import Screenshots
PERMISSIBLE_TIME_TO_WAIT = 30

DESKTOP_RESOLUTION_HORIZONTAL = 1920
DESKTOP_RESOLUTION_VERTICAL = 1080

MOBILE_RESOLUTION_HORIZONTAL = 375
MOBILE_RESOLUTION_VERTICAL = 812
mobile_emulation = {"deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}


def pytest_addoption(parser):
    """
    Метод добавляет кастомные ключи в запуск тестов
    Ключи:
    --browser: chrome/firefox - браузер для тестирования
    :param parser: парсер ключей pytest
    """
    parser.addoption('--browser', action='store',
                     default='desktop', help="Browser to run tests on")
    parser.addoption("--user_agent", action="store",
                     default="default_user_agent", help="User agent string")




@pytest.fixture(scope="session")
def web_driver(request):
    global browser
    """
    Инициализация веб драйвера в зависимости от ключа "--browser"
    :return: объект класса webdriver
    """
    browser = request.config.getoption('--browser')
    user_agent = request.config.getoption('--user_agent')
    from python_tests.functions import d
    d['User-Agent'] = user_agent



    if browser == 'desktop' or browser == 'default':
        CHROME_PATH = '/usr/bin/chromium-browser'
        CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

        chrome_options = Options()
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless=new")
        # chrome_options.add_argument("--remote-debugging-port=9222 https://chromium.org")
        # chrome_options.add_argument("--disable-gpu")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("user-agent=" + user_agent)
        print("У нас тут " + user_agent + ' ')

        chrome_options.binary_location = CHROME_PATH
        service = Service(executable_path=CHROMEDRIVER_PATH)
        browser = webdriver.Chrome(service=service, options=options)


        yield browser
        browser.quit()



    elif browser == 'mobile':
        CHROME_PATH = '/usr/bin/chromium-browser'
        CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

        chrome_options = Options()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        # chrome_options.add_argument("--remote-debugging-port=9222 https://chromium.org")
        # chrome_options.add_argument("--disable-gpu")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("user-agent=" + user_agent)
        print("У нас тут " + user_agent + ' ')
        print(host)
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
        chrome_options = Options()
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options = Options()
        chrome_options.binary_location = CHROME_PATH
        service = Service(executable_path=CHROMEDRIVER_PATH)
        browser = webdriver.Chrome(service=service, options=options)

        yield browser
        browser.quit()



    elif browser == 'desktop-ff-no-js':
        profile = webdriver.FirefoxProfile()
        profile.DEFAULT_PREFERENCES['frozen']['javascript.enabled'] = False
        profile.set_preference("app.update.auto", False)
        profile.set_preference("app.update.enabled", False)
        profile.update_preferences()
        options = Options()
        options.headless = False
        browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', options=options, firefox_profile=profile)
        yield browser
        browser.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        allure.attach(rep.longreprtext, name="errr_log")

# def pytest_exception_interact(node, call, report):
#    Screenshots.screenshot('Снимок, на чем упал тест', browser)

class Globals:
    PERMISSIBLE_TIME_TO_WAIT = 10



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.read_properties import Read_Config
from selenium.webdriver.firefox.options import Options as FirefoxOptions


aut_url = Read_Config.getApplicationURL()


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser == 'chromeheadless':
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser == 'firefoxheadless':
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.maximize_window()
    driver.get(aut_url)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Swag Labs'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Cyril'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

import pytest
from selenium import webdriver

from Test_Data.config import TestData

driver = None # initialize a driver for screenshot plugin


'''Adding hook for command line fetching'''
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

    parser.addoption(
        "--url", action="store", default="dev"
    )


'''Declaration of Fixture for setup and teardown'''
@pytest.fixture(scope="class") # we can run in method level when we remove the scope parameter
def setup(request):
    global driver   # This is the partner of driver = None

    ''' To read the browser name in command line'''
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=TestData.CHROME)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=TestData.FIREFOX)

    ''' To read the environment in command line'''
    url = request.config.getoption("url")
    if url == "dev":
        driver.get(TestData.BASED_URL)
    elif url == "staging":
        driver.get("https://www.google.com")

    driver.maximize_window()
    request.cls.driver = driver # cls.driver (Class level "to access this user self keyword") = driver (local driver)
    yield
    driver.quit()


'''********   This is for the screenshot plugin *********'''


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file("../Reports/"+name)


"""*************   END OF PLUGIN     ****************"""












from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# here from the above def , we will modify to make it flexible for any browser
@pytest.fixture(scope="class")
def setup(request):

    # this will fetch the value of the key browser_name ( from CLI ) and run respective condition
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\RakeshE-1763\\PycharmProjects\\PythonSelFramework\\driver\\chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Chrome(executable_path="C:\\Users\\RakeshE-1763\\PycharmProjects\\PythonSelFramework\\driver\\geckodriver.exe")

    else:
        driver = webdriver.Chrome(executable_path="C:\\Users\\RakeshE-1763\\PycharmProjects\\PythonSelFramework\\driver\\IEdriver.exe")


    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver

    # yield part will be executed after the test case
    yield
    driver.close()

import pytest
from utils.browser import get_driver

@pytest.fixture(scope="class")
def setup(request):
    driver = get_driver()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
email = "email.for.autotests"
correct_password = "Ui88))PooL"

def test_login_positive_right_password(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector("[type='email']").send_keys(email)
    browser.find_element_by_id("identifierNext").click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='password']")))
    browser.find_element_by_css_selector("[type='password']").send_keys(correct_password)
    browser.find_element_by_id("passwordNext").click()
    browser.find_element_by_css_selector(".gb_Ia.gbii").click()
    assert browser.find_element_by_class_name("gb_tb").text == "email.for.autotests@gmail.com", "Error during login"
    print('Succesfull login is completed')


@pytest.mark.parametrize('password', ["123456", "admin", "      "])
def test_login_negative_wrong_password(browser, password):
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector("[type='email']").send_keys(email)
    browser.find_element_by_id("identifierNext").click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='password']")))
    browser.find_element_by_css_selector("[type='password']").send_keys(password)
    browser.find_element_by_id("passwordNext").click()
    substring = "accounts.google.com/signin/v2/challenge/pwd"
    current_url = browser.current_url
    assert substring in current_url, f"ERROR! {substring} is not in {current_url}"
    print(f'Login was not completed with wrong password such as: "{password}"')






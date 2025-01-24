from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import sys

try:
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--reduce-security-for-testing')
    options.set_capability("acceptInsecureCerts", True)

    service = Service()
    service.creation_flags = 0x08000000  # Prevents command window from appearing

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(60)
    driver.get("http://rachacuca.com.br/palavras/palavras-cruzadas/1/")
    
    assert "Palavra Cruzada" in driver.title
    elem = driver.find_element(By.ID, "cell-0-0")
    
    #Find how many questions there are in the crossword:
    questions_horizontal = driver.find_elements(By.CSS_SELECTOR, 'ul.cross li')
    horizontal_num = [int(li.get_attribute('data-num')) for li in questions_horizontal]
    questions_vertical = driver.find_elements(By.CSS_SELECTOR, 'ul.down li')
    vertical_num = [int(li.get_attribute('data-num')) for li in questions_vertical]
    amount_of_question = max(max(horizontal_num), max(vertical_num))

    #Retrieve all questions:
    for i in range(1, amount_of_question):
        question = driver.find_element(By.XPATH, f'//li[@data-num="{i}"]')
        print(question.text)

    question1 = driver.find_element(By.XPATH, '//li[@data-num="1"]')
    print(question1.text)
    # Keep the browser open until user presses Enter
    input("Press Enter to close the browser...")

except WebDriverException as e:
    print(f"WebDriver error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
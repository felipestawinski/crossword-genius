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
    driver.set_page_load_timeout(30)
    
    driver.get("https://rachacuca.com.br/palavras/palavras-cruzadas/1/")
    print(driver.title)
    
    assert "Palavra Cruzada" in driver.title
    elem = driver.find_element(By.ID, "cell-0-0")
    elem.click()
    elem.send_keys("p")
    assert "No results found." not in driver.page_source

except WebDriverException as e:
    print(f"WebDriver error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import sys

def get_input_id_by_number(number):
    try:
        # Find the span with the specified number
        span = driver.find_element(By.XPATH, f"//span[@class='number' and text()='{number}']")
        
        # Find the associated input sibling in the same td
        input_element = span.find_element(By.XPATH, "./following-sibling::input")
        
        # Return the input's ID
        return input_element.get_attribute("id")
    except Exception as e:
        print(f"Error: {e}")
        return None

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
    
    #Find how many questions there are in the crossword:
    questions_horizontal = driver.find_elements(By.CSS_SELECTOR, 'ul.across li')
    print("questions_horizontal=", questions_horizontal)
    if len(questions_horizontal) != 0:
        horizontal_num = [int(li.get_attribute('data-num')) for li in questions_horizontal]

    
    questions_vertical = driver.find_elements(By.CSS_SELECTOR, 'ul.down li')
    print("questions_vertical=", questions_vertical)
    if len(questions_vertical) != 0:
        vertical_num = [int(li.get_attribute('data-num')) for li in questions_vertical]
    amount_of_question = max(max(horizontal_num), max(vertical_num))

    #Retrieve all questions:
    for i in range(1, amount_of_question+1):
        question = driver.find_element(By.XPATH, f'//li[@data-num="{i}"]')
        print(question.text)
        cell = get_input_id_by_number(i)

        elem = driver.find_element(By.ID, cell)
        #word_len
        #Iterate throught the word lenght and write the answer
        for i in range(len())

    #Write the answer
    elem = driver.find_element(By.ID, "cell-0-0")
    elem.send_keys("ABC")
    # Keep the browser open until user presses Enter
    input("Press Enter to close the browser...")

except WebDriverException as e:
    print(f"WebDriver error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
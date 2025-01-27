from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import re
import sys


def extract_number(input_string):
    # Use a regular expression to find a number at the end of the string within parentheses
    match = re.search(r'\((\d+)\)$', input_string)
    if match:
        return int(match.group(1))
    return None


def extract_column_row(input_string):
    # Use a regular expression to extract the column (x) and row (y)
    match = re.match(r'cell-(\d+)-(\d+)', input_string)
    if match:
        column = int(match.group(1))
        row = int(match.group(2))
        return column, row
    return None, None  # Return None if the input doesn't match the expected format

def get_cell_by_number(number):
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
    if len(questions_horizontal) != 0:
        horizontal_num = [int(li.get_attribute('data-num')) for li in questions_horizontal]

    
    questions_vertical = driver.find_elements(By.CSS_SELECTOR, 'ul.down li')
    if len(questions_vertical) != 0:
        vertical_num = [int(li.get_attribute('data-num')) for li in questions_vertical]

    print(f"Horizontal: {horizontal_num}")
    print(f"Vertical: {vertical_num}")

    example = "abcde"
    #Solve horizontal questions:
    print("Solving horizontal questions")
    for num in horizontal_num:
        question = driver.find_element(By.XPATH, f'//li[@data-num="{num}"]')
        print(question.text)
        cell = get_cell_by_number(num)
        answer_len = extract_number(question.text)
        column, row = extract_column_row(cell)

        #Iterate throught the answer length and write the answer
        example_index = 0
        for i in range(column, column + answer_len-1):
            cell = "cell-" + str(i) + "-" + str(row)
            elem = driver.find_element(By.ID, cell)
            if (elem) and example_index < len(example):
                elem.send_keys(example[example_index])
            else:
                print(f"Cell {cell} not found")
                break

            example_index += 1

    # Solve vertical questions
    print("Solving vertical questions")
    #Question 5 is both vertical and horizontal - problem
    for num in vertical_num:
        question = driver.find_element(By.XPATH, f'//ul[@class="down"]/li[@data-num="{num}"]')
        print(question.text)
        cell = get_cell_by_number(num)
        answer_len = extract_number(question.text)
        column, row = extract_column_row(cell)

        #Iterate throught the answer length and write the answer
        example_index = 0
        for i in range(row, row + answer_len-1):
            cell = "cell-" + str(column) + "-" + str(i)
            elem = driver.find_element(By.ID, cell)
            if (elem) and example_index < len(example):
                elem.send_keys(example[example_index])
            else:
                print(f"Cell {cell} not found")
                break

            example_index += 1

    #Write the answer
    #elem = driver.find_element(By.ID, "cell-0-0")
    #elem.send_keys("ABC")
    # Keep the browser open until user presses Enter
    input("Press Enter to close the browser...")

except WebDriverException as e:
    print(f"WebDriver error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv

# Path to your ChromeDriver executable
chromedriver_path = "C:/Users/khushal sharma/Downloads/chromedriver-win64/chromedriver.exe"

# Create a Chrome driver service
chrome_service = ChromeService(executable_path=chromedriver_path)

# Create a Chrome driver using the service
driver = webdriver.Chrome(service=chrome_service)

# Read URLs from a CSV file
urls = []
with open('C:/Users/khushal sharma/PycharmProjects/myproject/venv/Urlforemails.csv', 'r') as file:
    reader = csv.reader(file)
    urls = [row[0] for row in reader]

print(f"First URL to be opened: {urls[0]}")
# Iterate through each URL
for url in urls:
    # Load the webpage
    driver.get(url)

    # Wait for dynamic content to load (you may need to adjust the wait time)
    wait = WebDriverWait(driver, 5)

    try:
        # Extract the company name
        company_name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.bizTitleContainer h1')))
        company_name = company_name_element.text.strip()

        # Locate and click the "Show Mail" button
        show_mail_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[ng-repeat="button in sidebarButtons | limitTo:4"] div[ng-if="!emailShown"]')))
        show_mail_button.click()

        # Wait for the email element to be present after clicking the button
        email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[ng-if="emailShown"]')))
        email = email_element.get_attribute("ng-href").split(":")[1]

        # Save the email and company name to a CSV file (append mode)
        with open('email_and_company_data.csv', 'a', newline='') as csv_file:
            fieldnames = ['Email', 'Company']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write data
            writer.writerow({'Email': email, 'Company': company_name})

        print(f"Email and Company extracted from {url} and saved to 'email_and_company_data.csv': {email}, {company_name}")
    except TimeoutException:
        print(f"Timed out waiting for elements to be present on {url}.")
    except Exception as e:
        print(f"Error extracting data from {url}: {str(e)}")

# Close the browser
driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
# import csv
#
# # Path to your ChromeDriver executable
# chromedriver_path = "C:/Users/khushal sharma/Downloads/chromedriver-win64/chromedriver.exe"
#
# # Create a Chrome driver service
# chrome_service = ChromeService(executable_path=chromedriver_path)
#
# # Create a Chrome driver using the service
# driver = webdriver.Chrome(service=chrome_service)
#
# # Read URLs from a CSV file
# urls = []
# with open('C:/Users/khushal sharma/PycharmProjects/myproject/venv/Urlforemails.csv', 'r') as file:
#     reader = csv.reader(file)
#     urls = [row[0] for row in reader]
#
# print(f"First URL to be opened: {urls[0]}")
# # Iterate through each URL
# for url in urls:
#     # Load the webpage
#
#     driver.get(url)
#
#     # Wait for dynamic content to load (you may need to adjust the wait time)
#     wait = WebDriverWait(driver, 10)
#
#     try:
#         # Locate and click the "Show Mail" button
#         show_mail_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[ng-repeat="button in sidebarButtons | limitTo:4"] div[ng-if="!emailShown"]')))
#         ActionChains(driver).move_to_element(show_mail_button).click().perform()
#
#         # Wait for the email element to be present after clicking the button
#         email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[ng-if="emailShown"]')))
#         email = email_element.get_attribute("ng-href").split(":")[1]
#
#         # Save the email to a CSV file (append mode)
#         with open('email_data.csv', 'a', newline='') as csv_file:
#             fieldnames = ['Email', 'URL']
#             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#             # Write data
#             writer.writerow({'Email': email, 'URL': url})
#
#         print(f"Email extracted from {url} and saved to 'email_data.csv': {email}")
#     except TimeoutException:
#         print(f"Timed out waiting for the email element to be present on {url}.")
#     except Exception as e:
#         print(f"Error extracting email from {url}: {str(e)}")
#
# # Close the browser
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import csv

# Website URL
url = "https://www.hidubai.com/businesses/z-best-car-rental-transport-vehicle-services-car-rental-services-hor-al-anz-east-dubai"

# Path to your ChromeDriver executable
chromedriver_path = "C:/Users/khushal sharma/Downloads/chromedriver-win64/chromedriver.exe"

# Create a Chrome driver service
chrome_service = ChromeService(executable_path=chromedriver_path)

# Create a Chrome driver using the service
driver = webdriver.Chrome(service=chrome_service)

# Load the webpage
driver.get(url)

# Wait for dynamic content to load (you may need to adjust the wait time)
wait = WebDriverWait(driver, 10)

try:
    # Locate and click the "Show Mail" button
    show_mail_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[ng-repeat="button in sidebarButtons | limitTo:4"] div[ng-if="!emailShown"]')))
    ActionChains(driver).move_to_element(show_mail_button).click().perform()

    # Wait for the email element to be present after clicking the button
    email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[ng-if="emailShown"]')))
    email = email_element.get_attribute("ng-href").split(":")[1]

    # Save the email to a CSV file (append mode)
    with open('email_data.csv', 'a', newline='') as csv_file:
        fieldnames = ['Email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write data
        writer.writerow({'Email': email})

    print(f"Email extracted and saved to 'email_data.csv': {email}")
except TimeoutException:
    print("Timed out waiting for the email element to be present.")
except Exception as e:
    print(f"Error extracting email: {str(e)}")

# Close the browser
driver.quit()





# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# import csv
#
# # Website URL
# url = "https://www.hidubai.com/businesses/hekaya-car-rental-transport-vehicle-services-car-rental-services-international-city-warsan-1-dubai"
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
# # Load the webpage
# driver.get(url)
#
# # Wait for dynamic content to load (you may need to adjust the wait time)
# wait = WebDriverWait(driver, 10)
#
# try:
#     email_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[ng-if="emailShown"]')))
#     email = email_element.get_attribute("ng-href").split(":")[1]
#
#     # Save the email to a CSV file (append mode)
#     with open('email_data.csv', 'a', newline='') as csv_file:
#         fieldnames = ['Email']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#         # Write data
#         writer.writerow({'Email': email})
#
#     print(f"Email extracted and saved to 'email_data.csv': {email}")
# except TimeoutException:
#     print("Timed out waiting for the email element to be present.")
# except Exception as e:
#     print(f"Error extracting email: {str(e)}")
#
# # Close the browser
# driver.quit()

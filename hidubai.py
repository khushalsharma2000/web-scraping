
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import csv

# Website URL
url = "https://www.hidubai.com/search?resource=localBusiness&q=art%20restoration&lat=25.197965&lon=55.273985&place=All%20of%20Dubai"

# Path to your ChromeDriver executable
chromedriver_path = "path/to/chromedriver.exe"

# Create a Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without opening a browser window)
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Load the webpage
driver.get(url)

# Wait for dynamic content to load (you may need to adjust the wait time)
driver.implicitly_wait(10)

# Find the email address using Selenium
try:
    email_element = driver.find_element(By.CSS_SELECTOR, 'a[ng-if="emailShown"]')
    email = email_element.get_attribute("ng-href").split(":")[1]

    # Save the email to a CSV file
    with open('email_data.csv', 'w', newline='') as csv_file:
        fieldnames = ['Email']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write data
        writer.writerow({'Email': email})

    print(f"Email extracted and saved to 'email_data.csv': {email}")
except Exception as e:
    print(f"Error extracting email: {str(e)}")

# Close the browser
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace the following variables with the URL of the website and the path to the chromedriver executable on your machine
website_url = "https://github.com/facebook/react/pulls"
chromedriver_path = "/path/to/chromedriver"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
# Run Chrome in headless mode to avoid opening a browser window
chrome_options.add_argument("--headless")

# Create a new Chrome WebDriver instance
browser = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Navigate to the website
browser.get(website_url)

# pulls_single_page = []
# elements = browser.find_elements(By.XPATH, "//a[@class='Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title']")
# for element in elements:
#     pull = element.text
#     pulls_single_page.append(pull)
# print(pulls_single_page)

# --------------------------------------------------------------------------------------------

button = browser.find_element(By.CLASS_NAME, 'next_page') 
# Move up to the parent element
parent_element = button.find_element(By.XPATH ,'..')
# Get the text content of the parent element
text_before_button = parent_element.text
# Extract the number before "Next" using string manipulation
number_before_next = text_before_button.split(' ')[-2]
# Print the number before "Next"
# print("Number before 'Next':", number_before_next)
# print(type(number_before_next))
last_page_no = int(number_before_next)
# print(type(last_page_no))

pulls=[]

elements = browser.find_elements(By.XPATH, "//a[@class='Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title']")
for element in elements:
    pull = element.text
    # print(pull)
    pulls.append(pull)

for i in range(0,last_page_no):
    button = browser.find_element(By.CLASS_NAME, 'next_page')  # Replace with the appropriate XPath for the next paginated button
    button.click()

    # Wait for the data to load (you may need to adjust the wait time based on the web page)
    time.sleep(2)

    # Scrape the loaded data
    elements = browser.find_elements(By.XPATH, "//a[@class='Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title']")
    for element in elements:
        pull = element.text
        # print(pull)
        pulls.append(pull)

print(pulls)
print(len(pulls))

# --------------------------------------------------------------------------------------------

# Close the browser
browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace the following variables with the URL of the website
# and the path to the chromedriver executable on your machine
website_url = "https://github.com/facebook/react/commits"
chromedriver_path = "/path/to/chromedriver"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
# Run Chrome in headless mode to avoid opening a browser window
chrome_options.add_argument("--headless")

# Create a new Chrome WebDriver instance
browser = webdriver.Chrome(
    executable_path=chromedriver_path, options=chrome_options)

# Navigate to the website
browser.get(website_url)

commits = []
elements = browser.find_elements(By.XPATH, "//a[@class='Link--primary text-bold js-navigation-open markdown-title']")
for element in elements:
    commit = element.text
    commits.append(commit)
print(commits)

# Close the browser
browser.quit()
